# src
This folder serves as the main directory for all functionality related
to budgettrackr. 

* `scrape.py`: data mining functionality, web scraping utility parsing 
HTML elements for specifed values
* `web.py`: formats collected values from `scrape.py` for our respective
HTML files for the website. 
* `main.py`: main driver for the project. calls `scrape.py` and `web.py`,
collecting values and publishing to localhost. 
* `static/`: contains images and all things that will remain constant 
throughout the project. 
* `templates/`: constains all things related to our website 

