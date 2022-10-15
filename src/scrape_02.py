"""
Simple scraping with beautifulsoup + requests. Spoofing machine + browser information
is necessary in order to extract data from amazon and perhaps other major
companies.

This file's purpose is to extract data from a given URL
"""
# lib for scraping + formatting retrieved data
from bs4 import BeautifulSoup as bs
# python binding for C libs libxml libxslt, handling html xml files
import lxml
# lib for HTTP requests
import requests


class product:
    """
    product class that will provide easier use of inheritance for other classes
    relying off the data collected from this class. 
    Functions:
        - name()
        - details()
        - desc()
        - price()
        - ratings()
        - num_ratings()
    """

    """
    create a constructor for this class. could save every field value collected
    to a dataframe, list, dict, etc...

    def __init__(self):
    """
    def name(soup):
        """
        Finds the name of the product by parsing the webpage. Inspect the 
        desired webpage and the value to save
            - 'span' = the starting inline container
            - 'id' = unique ID for an HTML element
            - 'productTitle' = the HTML we want to save
        """
        try:
            # declare the outer span inline container tag as starting parse point
            product = soup.find('span', attrs = {'id': 'productTitle'})

            # convert product to a string
            product_name = product.string
            
            #formatting, neglecting commas and whitespace
            product_fmt = product_name.strip().replace(',', '')

        except AttributeError:
            product_fmt = "PRODUCT NAME NOT FOUND"

        # print the product name
        print("Product: \n", product_fmt)

        
    def details(soup):
        """
        function to retrieve details of an amazon product
            - 'div' = the starting division to begin parsing
            - 'id' = unique ID for an HTML element
            - 'productOverview_feature_div' = the HTML we want to save
        """
        try:
            details = soup.find('div', attrs = {'id': 'productOverview_feature_div'})

            product_details = details.string

            details_fmt = product_details.strip().replace(',', '')   

        except AttributeError:
            details_fmt = "PRODUCT DETAILS NOT FOUND"
            
        print("Product Details: \n", details_fmt)


    def desc(soup):
        """
        function to retrieve the description from of amazon product
            - 'li' = the starting list to begin parsing
            - 'id' = unique ID for an HTML element
            - 'a-spacing-small' = the HTML we want to save
        """
        try:
            desc = soup.find('li', attrs = {'id': 'a-spacing-small'})

            product_desc = desc.string

            desc_fmt = product_desc.strip().replace(',', '') 

        except AttributeError:
            desc_fmt = "PRODUCT DESC NOT FOUND"

        print("Product Description: \n", desc_fmt)


    def price(soup):
        """
        function to retrieve the price info of an amazon product
            - 'span' = the starting inline container
            - 'class' = class our HTML element will belong to
            - 'a-offscreen' = the HTML we want to save
        """
        try:
            price = soup.find('span', attrs = 
                              {'class': 'a-offscreen'}).string.strip().replace(',', '')
        
        except AttributeError:
            price = "PRICE NOT FOUND"
        
        print("Price (USD): \n", price)

        
    def ratings(soup):
        """
        function to retrieve the rating of an amazon product
            - 'span' = the starting inline container
            - 'class' = class our element belongs to
            - 'a-icon-alt' = element to save
        """
        try:
            rating = soup.find("span", attrs =
                               {'class': 'a-icon-alt'}).string.strip().replace(',', '')
        except AttributeError:
                rating = "RATING NOT FOUND"
        
        print("Rating: \n", rating)


    def num_ratings(soup):
        """
        function to retrieve the number of ratings an amazon product has been
        given
            - 'span' = the starting inline container
            - 'id' = unique ID for an HTML element
            - 'acrCustomerReviewText' = the HTML we want to save
        """
        try:
            ratings_num = soup.find('span', attrs = 
                        {'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

        except AttributeError:
            ratings_num = "NUMBER OF RATINGS NOT FOUND"
        
        print("Number of Ratings: \n", ratings_num)



def main():
    """
    specifying user agent, other user agents available online  
    for something stable or server-based, think of a function to parse a list
    of user agents and swap on a time-based interval
    """
    #user_agent = ({'User-Agent': 
    #               'Mozilla/5.0 (X11; Linux x86_64) \
    #               AppleWebKit/537.36 (KHTML, like Gecko) \
    #               Chrome/44.0.2403.157 Safari/537.36', \
    #               'Accept-Language': 'en-US, en;q=0.5'
    #               })
    user_agent = ({'User-Agent': 
                    'Mozilla/5.0 (X11; Linux x86_64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/72.0.3626.121 Safari/537.36', \
                    'Accept-Language': 'en-US, en;q=0.5'
                   })

    # source file
    link = 'https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_1?crid=1B7QEPTT5XCBH&keywords=amd+ryzen+5000&qid=1665786908&qu=eyJxc2MiOiIzLjA1IiwicXNhIjoiMi44NCIsInFzcCI6IjIuMTUifQ%3D%3D&sprefix=amd%2520ryzen%25205000%2Caps%2C114&sr=8-1&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0'

    # HTTP request 
    page = requests.get(link, headers = user_agent)

    # soup object that stores our data
    soup = bs(page.content, "lxml")

    """
    Call our functions that will return the required fields:
        - Product Name
        - Product Details
        - Product Description
        - Product Price
        - Product Ratings
        - Product # of Ratings
    """
    product.name(soup)
    product.details(soup)
    product.desc(soup)
    product.price(soup)
    product.ratings(soup)
    product.num_ratings(soup)


if __name__ == '__main__':
    main()

