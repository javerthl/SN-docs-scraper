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
5. That last line navigates you to the folder you just created. Now create a virtual environment from which to run your Python scripts.
   ```python3 -m venv venv```
   
   ```source venv/bin/activate```
6. Your terminal should now show: ```(venv) %```
7. Install dependencies. If you haven't yet, youll need to install pip too. Visit https://pip.pypa.io/en/stable/installation/ to learn more. 
   ```pip install playwright beautifulsoup4``` (or pip3). 

   ```python3 -m playwright install chromium```
8. Run the "scraper" script. You should see Chrome automatically open the various docs page while the terminal shows its progress. After the scraping is complete, you should see the folders and sub-folders with the scraped docs pages as individual text files.
   ```python3 scraper.py``` 
10. Now we want to combine all these individual text files into one large text files. This is useful for when you want to use the text to be searchable or in an LLM project. Run the "combine" script.
    ```python3 combine.py```
11. Now you should have one large text file. Now let's clean it up. This removes text such as the table of contents and miscellaneous navigation text like "Login here" that was scraped from every page. Removing these elements will improve the search quality of your project. Run the "cleanup" script.
    ```python3 cleanup.py```
12. You now have a text file that is ready to be used in a search or LLM project.

## Optional - Prompt for Claue Agent

   
