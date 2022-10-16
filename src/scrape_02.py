#!/usr/bin/python3
"""
Simple scraping with beautifulsoup + requests. Spoofing machine + browser 
information is necessary in order to extract data from amazon and perhaps 
other major companies.

This file's purpose is to extract data from a given URL
"""

# lib for scraping + formatting retrieved data
from bs4 import BeautifulSoup as bs
# python binding for C libs libxml libxslt, handling html xml files
import lxml
# lib for HTTP requests
import requests
# lib for setting up the director for our jira template file
from jinja2 import Environment as j2_ENV
# lib for loading our jira template file
from jinja2 import FileSystemLoader as j2_FSL


class Product:
    """
    product class that will provide easier use of inheritance for other classes
    relying off the data collected from this class. 
    Functions:
        - name()
        - details()
        - desc()
        - price()
        - rating()
        - num_ratings()
    """

    def __init__(self, soup):
        """
        Product class constructor, each 'field' function of the class 
        is assigned to an attribute of the class
        """
        self.soup = soup
        self.name = self.get_name()
        self.details = self.get_details()
        self.desc = self.get_desc()
        self.price = self.get_price()
        self.rating = self.get_rating()
        self.num_ratings = self.get_num_ratings()
        self.display = self.print_contents()
    
    def print_contents(self):
        """
        takes care of formatting neatly with Jira + printing
        """
        # load the folder in which the template is located
        env = j2_ENV(loader = j2_FSL(''))
        # load the .j2 template
        template = env.get_template('product.j2')
        # define our fields to be rendered based on the .j2 file
        content_fmt = template.render(name=self.name, 
                                      details=self.details, 
                                      desc=self.desc, 
                                      price=self.price, 
                                      rating=self.rating, 
                                      num_ratings=self.num_ratings)
        # print our formatted content
        print(content_fmt)
        # print("Product: %s\nDetails: %s\nDescription: %s" % (self.name, self.details, self.desc))

    def get_name(self):
        """
        Finds the name of the product by parsing the webpage. Inspect the 
        desired webpage and the value to save
            - 'span' = the starting inline container
            - 'id' = unique ID for an HTML element
            - 'productTitle' = the HTML we want to save
        """
        try:
            # outer span inline container tag as starting parse point
            product = self.soup.find('span', attrs = {'id': 'productTitle'})
            # convert product to a string
            name = product.string
            #formatting, neglecting commas and whitespace
            name_fmt = name.strip().replace(',', '')

        except AttributeError:
            name_fmt = "PRODUCT NAME NOT FOUND"

        return name_fmt

    def get_details(self):
        """
        function to retrieve details of an amazon product
            - 'div' = the starting division to begin parsing
            - 'id' = unique ID for an HTML element
            - 'productOverview_feature_div' = the HTML we want to save
        the idea is to first iterate over the tag before our list in addition to 
        the list itself
        """
        details_fmt = []

        for x in self.soup.find_all('table', attrs={'class': 'a-normal a-spacing-none a-spacing-top-base'}):
            for tag in x.find_all('tr'):
                details_fmt = tag.get_text()

        return details_fmt

        """
        try:
            details = self.soup.find('div', attrs = {'id': 'productOverview_feature_div'})
            product_details = details.string
            details_fmt = product_details.strip().replace(',', '')   

        except AttributeError:
            details_fmt = "PRODUCT DETAILS NOT FOUND"
            
        return details_fmt
        """


    def get_desc(self):
        """
        function to retrieve the description from of amazon product
            - 'li' = the starting list to begin parsing
            - 'id' = unique ID for an HTML element
            - 'a-spacing-small' = the HTML we want to save
        """
        try:
            desc = self.soup.find('li', attrs = {'id': 'a-spacing-small'})

            product_desc = desc.string

            desc_fmt = product_desc.strip().replace(',', '') 

        except AttributeError:
            desc_fmt = "PRODUCT DESC NOT FOUND"

        return desc_fmt

    def get_price(self):
        """
        function to retrieve the price info of an amazon product
            - 'span' = the starting inline container
            - 'class' = class our HTML element will belong to
            - 'a-offscreen' = the HTML we want to save
        """
        try:
            price = self.soup.find('span', 
                                    attrs = {'class': 'a-offscreen'})\
                                    .string.strip().replace(',', '')
        
        except AttributeError:
            price = "PRICE NOT FOUND"
        
        return price
        
    def get_rating(self):
        """
        function to retrieve the rating of an amazon product
            - 'span' = the starting inline container
            - 'class' = class our element belongs to
            - 'a-icon-alt' = element to save
        """
        try:
            rating = self.soup.find("span", 
                                    attrs = {'class': 'a-icon-alt'})\
                                    .string.strip().replace(',', '')

        except AttributeError:
                rating = "RATING NOT FOUND"
        
        return rating

    def get_num_ratings(self):
        """
        function to retrieve the number of ratings an amazon product has been 
        given
            - 'span' = the starting inline container
            - 'id' = unique ID for an HTML element
            - 'acrCustomerReviewText' = the HTML we want to save
        """
        try:
            ratings_num = self.soup.find('span', attrs = {'id': \
                                        'acrCustomerReviewText'})\
                                        .string.strip().replace(',', '')

        except AttributeError:
            ratings_num = "NUMBER OF RATINGS NOT FOUND"
        
        return ratings_num

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
    link = 'https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_1?crid=1B7QEPTT5XCBH&keywords=amd+ryzen+5000&qid=1665786908&qu=eyJxc2MiOiIzLjA1IiwicXNhIjoiMi44NCIsInFzcCI6IjIuMTUifQ%3D%3D&sprefix=amd%2520ryzen%25205000%2Caps%2C114&sr=8-1&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0'
    
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
    p = Product(soup)

if __name__ == '__main__':
    main()


