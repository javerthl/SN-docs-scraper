# SN-docs-scraper

This repository contains scripts that can traverse and scrape data from [servicenow.com/docs](https://www.servicenow.com/docs), combine the outputs, and clean up the results. This can then be used as context for a Claude Q&A agent or Search. All the scripts are written in Python and were run in MacOS.

---

## 📦 What's included in the repo
* **Scraping script**: `scrape_servicenow_docs.py`.
* **Combine + cleaning script**: `combine_and_clean_servicenow_scrape_docs.py`.
* **Example text**: A single docs page (uncleaned) scraped from ServiceNow's documentation on the MCP client.
* **Final result**: An example of a combined and cleaned text file.
* **Example prompt**: Instructions for a Claude Q&A agent using the text file as context.

---

## 🛠 Pre-requisites
* **Python 3.11+**
* **PIP**

---

## 🚀 High-level steps
1. **Install** Python, PIP, Beautiful Soup, and Playwright packages.
2. **Run the scraper** script with the desired ServiceNow docs URL to generate folders of text files.
3. **Run the combine and clean script** to merge files and remove non-relevant text like navigation menus.

---

## 📖 Detailed steps

### 1. Environment Setup
Install **Python 3.11** and ensure it is added to your **PATH** when prompted. Open your terminal and verify the installation:
```bash
python3 --version
```
(Note: All code blocks below are to be run in the terminal.)

### 2. Create Workspace
Create a folder called servicenow_scraper to store your scripts and documents:

```Bash

mkdir servicenow_scraper
cd servicenow_scraper
```
### 3. Virtual Environment
Create and activate a virtual environment to manage your dependencies:

```Bash

python3 -m venv venv
source venv/bin/activate
```
Your terminal should now show the (venv) % prefix.

### 4. Install Dependencies
Ensure you have pip installed, then run the following commands:

```Bash

pip install playwright beautifulsoup4
python3 -m playwright install chromium
```
(This downloads a playwright-managed version of Chromium.)

### 5. Run the Scraper
Open `scrape_servicenow_docs.py` and enter your starting URL and base prefix in lines 8 and 9. Then execute:

```Bash

python3 scrape_servicenow_docs.py
```
Chrome will automatically open and navigate through the docs while progress is shown in the terminal.

### 6. Combine and Clean Data
Merge the individual files and remove navigation noise (like "Login" or Table of Contents). Open `combine_and_clean_servicenow_scrape_docs.py` and update lines 64 and 65 with your folder name and output filename:

```Bash

python3 combine_and_clean_servicenow_scrape_docs.py
```
The source file name acts as a delimiter, which is useful for Q&A citations.

### 7. Final Result
You now have a text file ready for use in a search or LLM project.

---

## 🤖 Optional - Prompt for Claude Agent
The output can be used to create a Claude Q&A bot. Refer to `Claude_instructions.md` for the specific prompt used.
