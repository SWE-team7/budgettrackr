#!/usr/bin/python3

# import unit test module
import unittest
# import scrape file
from scrape import Product

class ScrapeTest(unittest.TestCase):
    """
    within here we will probably want to test each method of our class 
    individually. the biggest thing we can test is the formatting of each
    attribute we are collecting.

    test_get_name:

    test_get_details:

    test_get_desc:

    test_get_price:
    here we can check the formatting of our price and verify against a regular
    expression... for example: 
    /\$\d{1,9}(?:[.,]\d{3})*(?:[.,]\d{2})/g will cover the standard format of 
    amazon prices $XX.xx or $XX,xx for european prices
    OR something along the lines of val == '$' + {:.2f}

    test_get_rating:

    test_get_num_ratings:
    """


if __name__ == '__main__':
    unittest.main()

