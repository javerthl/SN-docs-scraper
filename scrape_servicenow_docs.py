import os
import time
from urllib.parse import urljoin, urlparse
from collections import deque
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

START_URL = "https://www.servicenow.com/docs/bundle/zurich-intelligent-experiences/page/administer/model-context-protocol-client/reference/mcp-client.html"
BASE_BUNDLE_PREFIX = "/docs/bundle/zurich-intelligent-experiences/page/administer/model-context-protocol-client/concept/"
OUTPUT_DIR = "servicenow_docs_mcpc"

def is_valid_doc_link(url):
    p = urlparse(url)
    return p.netloc == "www.servicenow.com" and p.path.startswith(BASE_BUNDLE_PREFIX)

def url_to_path(url):
    p = urlparse(url)
    path = p.path.lstrip("/")
    if path.endswith(".html"):
        path = path[:-5] + ".txt"
    else:
        if not path.endswith("/"):
            path += "/"
        path += "index.txt"
    return os.path.join(OUTPUT_DIR, path)

def save_text(url, text):
    out = url_to_path(url)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print("[SAVED]", out)

def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
    main = soup.find("main") or soup
    return main.get_text("\n", strip=True), soup

def crawl():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-features=IsolateOrigins,site-per-process",
                "--disable-web-security",
                "--disable-dev-shm-usage",
                "--no-sandbox",
            ],
        )

        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120 Safari/537.36",
            locale="en-US",
            viewport={"width": 1400, "height": 900},
        )

        page = ctx.new_page()

        queue = deque([START_URL])
        visited = set()

        while queue:
            url = queue.popleft()
            if url in visited:
                continue
            visited.add(url)

            print("[OPEN]", url)

            try:
                page.goto(url, timeout=120000, wait_until="load")
            except Exception as e:
                print("    [FAIL]", e)
                continue

            time.sleep(2)  # allow hydration

            html = page.content()
            text, soup = extract_text(html)

            if len(text) > 100:
                save_text(url, text)
            else:
                print("[SKIP] Not enough readable text.")

            # collect valid internal doc links
            for a in soup.find_all("a", href=True):
                child = urljoin(url, a["href"].split("#")[0])
                if is_valid_doc_link(child) and child not in visited:
                    queue.append(child)

        print("Done. Pages visited:", len(visited))
        browser.close()

if __name__ == "__main__":
    crawl()
