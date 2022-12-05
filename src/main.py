#!/usr/bin/python3
"""
This file serves as 'MAIN' for budgettrackr where we import our necessary
libraries, define a Flask application, and call our Website class to run
the project.
"""
# python binding for C libs libxml libxslt, handling html xml files
import lxml
# import the py file taking care of routing collected data
from web import *
# lib for HTTP requests
import requests
# lib for scraping + formatting retrieved data
from bs4 import BeautifulSoup as bs
# import our scrape file
from scrape import *
# import Flask for web publishing
from flask import Flask, render_template, request, session

# declare our flask app with our static directory
app = Flask(__name__, static_url_path='/static')


def main():
    """
    run our Website class, within it renders templates and stores the
    collected values from the Product class in our specified HTML elements
    """
    render_web = Website()


if __name__ == '__main__':
    main()
