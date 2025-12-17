# SN-docs-scraper
This repo contains scripts that can traverse and scrape data from servicenow.com/docs, combine the outputs, and clean up the results. All the scripts are written in Python. This was run in MacOS. 

# Pre-requisites
Python 3.11+

# High-level steps
1. Install Beautiful Soup and Playwright packages
2. Run the scraper script with the desired ServiceNow docs URL. The output is a folder(s) of text files per page that was scraped, following the URL structure. 
3. Run the combine script that combines all the text files into a single file.
4. Run the cleanup script(s) that removes non-relevant text such as the table of contents and navigation text contained on every page.

## Detailed steps
1. Install Python 3.11. 
2. Open terminal and check that Python is installed.
   Type: ```python3 --version```
3. Create a folder called "servicenow_scraper" to store your scraped documents (also a good place to store your scripts.)
   ```mkdir servicenow_scraper```
   ```cd servicenow_scraper```
4. That last line navigates you to the folder you just created. Now create a virtual environment from which to run your Python scripts.
   ```python3 -m venv venv``` \n
   ```source venv/bin/activate```
5. Your terminal should now show: ```(venv) %```
   
