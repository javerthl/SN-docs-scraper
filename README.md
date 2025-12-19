# SN-docs-scraper
This repo contains scripts that can traverse and scrape data from servicenow.com/docs, combine the outputs, and clean up the results. All the scripts are written in Python. This was run in MacOS. 

## What's included in the repo
- A scraping script
- A combine + cleaning script
- Example text of a single docs page that was scraped from ServiceNow's documentation on MCP client (uncleaned): https://www.servicenow.com/docs/bundle/zurich-intelligent-experiences/page/administer/model-context-protocol-client/concept/add-mcp-client-on-ai-agent-studio.html 
- Example of combined and cleaned text file, final result.
- Example prompt that can be used a Claude Q&A agent using the text file as context. 

# Pre-requisites
Python 3.11+

PIP

# High-level steps
1. Install Python and Beautiful Soup and Playwright packages
2. Run the scraper script with the desired ServiceNow docs URL. The output is a folder(s) of text files per page that was scraped, following the URL structure. 
3. Run the combine and clean script that combines all the text files into a single file and removes non-relevant text such as the table of contents and navigation text contained on every page.

## Detailed steps
1. Install Python 3.11. 
2. Open terminal and check that Python is installed.
   Type: ```python3 --version```
3. Create a folder called "servicenow_scraper" to store your scraped documents (also a good place to store your scripts.)
   ```mkdir servicenow_scraper```
   
   ```cd servicenow_scraper```
4. That last line navigates you to the folder you just created. Now create a virtual environment from which to run your Python scripts.
   ```python3 -m venv venv```
   
   ```source venv/bin/activate```
5. Your terminal should now show: ```(venv) %``` You want to run the following commands in the venv in your directory.
6. Install dependencies. If you haven't yet, you'll need to install pip too. Visit https://pip.pypa.io/en/stable/installation/ to learn more.
   
   ```pip install playwright beautifulsoup4``` (or pip3). 

   ```python3 -m playwright install chromium```

9. Run the "scrape_servicenow_docs.py" script. You should see Chrome automatically open the various docs page while the terminal shows its progress. After the scraping is complete, you should see the folders and sub-folders with the scraped docs pages as individual text files.

   In lines 8 and 9, enter your starting URL and the base prefix for which to start navigating through the doc tree and scraping. 

   ```python3 scrape_servicenow_docs.py```

10. Now we want to combine all these individual text files into one large text files. This is useful for when you want to use the text to be searchable or in an LLM project. This script also removes text such as the table of contents in the beginning and miscellaneous navigation text like "Login" that was captured in every page. Removing these elements will improve the search quality of your project. Run the "combine_and_clean_servicenow_scrape_docs.py" script.

   In lines 64 and 65, enter the folder name where your docs are located and a filename for your final output respectively. 

   ```python3 combine_and_clean_servicenow_scrape_docs.py```

11. You now have a text file that is ready to be used in a search or LLM project.

## Optional - Prompt for Claude Agent
The output text file of the scraped ServiceNow documentation can be used in LLM projects such as for Claude to create a Q&A bot to answer questions based on the scraped documentation. See "prompt.txt" for the prompt used to create the Q&A bot. 
   
