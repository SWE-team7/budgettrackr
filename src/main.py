#/usr/bin/python3
"""
This file serves as 'MAIN' for budgettrackr. Here we will spoof our machine,
declare a link to scrape and a corresponding BeautifulSoup object, and finally
calling our scrape file to retrieve the 
"""
# python binding for C libs libxml libxslt, handling html xml files
#import lxml
# lib for HTTP requests
import requests
# lib for scraping + formatting retrieved data
from bs4 import BeautifulSoup as bs
# import our scrape file
from scrape import *
# import Flask for web publishing
from flask import Flask, render_template, request, session

# declare our flask app with our static dir
app = Flask(__name__, static_url_path='/static')

# import our web file with our flask app specifications
from web import *


def main():
    """ 
    specifying user agent, other user agents available online for something 
    stable or server-based, think of a function to parse a list of user 
    agents and swap on a time-based interval
    """
    user_agent = ({'User-Agent': 
                    'Mozilla/5.0 (X11; Linux x86_64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/72.0.3626.121 Safari/537.36', \
                    'Accept-Language': 'en-US, en;q=0.5'
                   })
    # source file
    link = 'https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_1?             crid=1B7QEPTT5XCBH&keywords=amd+ryzen+                                                                       5000&qid=1665786908&qu=eyJxc2MiOiIzLjA1IiwicXNhIjoiMi44NCIsInFzcCI6IjIuMTUifQ%3D%3D&sprefix=amd%2520ryzen%25205000%2Caps%2C114&sr=8-1&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0'
    
    # HTTP request 
    page = requests.get(link, headers = user_agent)

    # soup object that stores our data
    soup = bs(page.content, "lxml")
    
    """ 
    call to our class which calls our constructor simultaneously calls the 
    functions to fill in our product, passing in the soup object. within the 
    construct we call the following functions:
        - get_name()
        - get_details() 
        - get_desc()
        - get_price()
        - get_rating()
        - get_num_ratings()
        - print_contents() 
    """
    p_attrs = []
    p_attrs = Product(soup)
    print("<------------ DEBUG ------------>")
    print(p_attrs.name)
    p_name = p_attrs.name

    # run our website passing in the Product class object
    wh = home_page()
    wp = product_page(p_attrs)

if __name__ == '__main__':
    main()

