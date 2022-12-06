#!/usr/bin/python3
from behave import *
from nose.tools import *
import unittest
import re
import src
from src import scrape
from src.scrape import Product


user_agent = ({'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/72.0.3626.121 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'
               })

# source file
link = 'https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_1?crid=1B7QEPTT5XCBH&keywords=amdryzen+5000&qid=1665786908&qu=eyJxc2MiOiIzLjA1IiwicXNhIjoiMi44NCIsInFzcCI6IjIuMTUifQ%3D%3D&sprefix=amd%2520ryzen%25205000%2Caps%2C114&sr=8-1&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0'

prod_info = Product(user_agent, link)


class TestProduct(unittest.TestCase):

    @given('A name')
    def test_fetch_name(self):
        print("\nTesting Product.name")
        product_name = 'AMD Ryzen 5 5600X 6-core 12-Thread Unlocked Desktop Processor with Wraith Stealth Cooler'
        fetched_name = prod_info.name

        # expected, actual
        #name_check = self.assertEqual(product_name, fetched_name)
        name_check = assert_equal(product_name, fetched_name)

        # print results
        print("\nExpected  : " + product_name + "\n"
              + "Fetched   : " + fetched_name)

        if (name_check is None):
            print("Name Check:      PASSED\n")
        else:
            print("Name Check:      FAILED\n")

    @given('A price')
    def test_fetch_price(self):
        """
        this test case ensures our price fetching works repeatedly as well as
        checking our price format follows a regular expression for US + EU
        formatted prices
        """
        print("\nTesting Product.price")
        product_price = prod_info.price
        fetched_price = prod_info.price

        price_check = assert_equal(product_price, fetched_price)

        print("\nExpected  : " + product_price + "\n"
              + "Fetched   : " + fetched_price)

        if (price_check is None):
            print("Price Check:     PASSED\n")
        else:
            print("Price Check:     FAILED\n")

        # define regular expression
        price_regex = r'\$+\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})'
        # check regex against price
        regex_check = assert_regex(fetched_price, price_regex)

        if (regex_check is None):
            print("Price Regex Check:     PASSED\n")
        else:
            print("Price Regex Check:     FAILED\n")

    @given('A rating')
    def test_fetch_rating(self):
        print("\nTesting Product.rating")
        product_rating = prod_info.rating
        fetched_rating = prod_info.rating

        rating_check = assert_equal(product_rating, fetched_rating)

        print("\nExpected  : " + product_rating + "\n"
              + "Fetched   : " + fetched_rating)
        if (rating_check is None):
            print("Rating Check:    PASSED\n")
        else:
            print("Rating Check:    FAILED\n")

        # decimal {X.x} "out of 5 stars"
        rating_regex = r'^(?!.*\..*\.)[.\d]+ out of 5 stars'
        rating_regex_check = assert_regex(fetched_rating,
                                          rating_regex)
        if (rating_regex_check is None):
            print("Rating Regex Check:     PASSED\n")
        else:
            print("Rating Regex Check:     FAILED\n")

    @given('A rating count')
    def test_fetch_num_ratings(self):
        product_num_ratings = prod_info.num_ratings
        fetched_num_ratings = prod_info.num_ratings

        rating_num_check = assert_equal(
            product_num_ratings, fetched_num_ratings)

        if (rating_num_check is None):
            print("Rating Num Check:    PASSED\n")
        else:
            print("Rating Num Check:    FAILED\n")


if __name__ == '__main__':
    unittest.main()
