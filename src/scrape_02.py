"""
Simple scraping with beautifulsoup + requests. Spoofing machine + browser information
is necessary in order to extract data from amazon and perhaps other major
companies.

This file's purpose is to extract data from a given URL
"""

# lib for scraping + formatting retrieved data
from bs4 import BeautifulSoup 

import lxml
# lib for HTTP requests
import requests


def parse(link):
    """
    function that parses the link pased in and stores the necessary values
    """
    
    """
    specifying user agent, You can use other user agents available on the 
    internet
    """
    profile_headers = ({'User-Agent': \
                'Mozilla/5.0 (X11; Linux x86_64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/44.0.2403.157 Safari/537.36', \
                'Accept-Language': 'en-US, en;q=0.5'})

    # HTTP request 
    page = requests.get(link, headers = profile_headers)
    
    # soup object that stores our data
    soup = BeautifulSoup(page.content, "lxml")

    """
    this section of try + catch statements parses the requested URL for the specific
    element id's and classes we want to save: product, price, rating, num of ratings
    and converts them to a string
    """
    
    # product name
    try:

        # declare the outer span inline container tag as starting parse point
        product = soup.find('span', attrs = {'id': 'productTitle'})

        # convert product to a string
        product_name = product.string

        """
        represet our title as a string value + formatting, neglecting 
        commas and whitespace
        """
        product_fmt = product_name.strip().replace(',', '')

    except AttributeError:
        product_fmt = "PRODUCT NAME NOT FOUND"

    # print the product name
    print("Product: \n", product_fmt)

    
    # product details
    try:
        details = soup.find('div', attrs = {'id': 'productOverview_feature_div'})

        product_details = details.string

        details_fmt = product_details.strip().replace(',', '')   

    except AttributeError:
        details_fmt = "PRODUCT DETAILS NOT FOUND"
        
    print("Product Details: \n", details_fmt)


    # product description
    try:
        desc = soup.find('div', attrs = {'id': 'featurebullets_feature_div'})

        product_desc = desc.string

        #desc_fmt = product_desc.strip().replace(',', '') 

    except AttributeError:
        product_desc = "PRODUCT DESC NOT FOUND"
        
    print("Product Description: \n", product_desc)


    # product price
    try:

        price = soup.find('span', attrs = 
                          {'class': 'a-offscreen'}).string.strip().replace(',', '')
    
    except AttributeError:
        price = "PRICE NOT FOUND"
    
    print("Price (USD): \n", price)

    
    # product ratings
    try:
        rating = soup.find("span", attrs =
                           {'class': 'a-icon-alt'}).string.strip().replace(',', '')
    except AttributeError:
            rating = "RATING NOT FOUND"
    
    print("Rating: \n", rating)


    # number of product ratings
    try:
        ratings_num = soup.find('span', attrs = 
                    {'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

    except AttributeError:
        ratings_num = "NUMBER OF RATINGS NOT FOUND"
    
    print("Number of Ratings: \n", ratings_num)



def main():
    # source file
    link = 'https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_1?crid=1B7QEPTT5XCBH&keywords=amd+ryzen+5000&qid=1665786908&qu=eyJxc2MiOiIzLjA1IiwicXNhIjoiMi44NCIsInFzcCI6IjIuMTUifQ%3D%3D&sprefix=amd%2520ryzen%25205000%2Caps%2C114&sr=8-1&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0'

    # call the parse function passing in the above link
    parse(link)

if __name__ == '__main__':
    main()

