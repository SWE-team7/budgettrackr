#!/usr/bin/python3
import unittest
# from path import src as module_0
#from path import src as Product
import src
from src import scrape
from src.scrape import Product

class TestProduct(unittest.TestCase):

    def test_fetch_name(self):

        user_agent = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/72.0.3626.121 Safari/537.36',
                   'Accept-Language': 'en-US, en;q=0.5'
                   })
        
        # source file
        link = 'https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_1?crid=1B7QEPTT5XCBH&keywords=amdryzen+5000&qid=1665786908&qu=eyJxc2MiOiIzLjA1IiwicXNhIjoiMi44NCIsInFzcCI6IjIuMTUifQ%3D%3D&sprefix=amd%2520ryzen%25205000%2Caps%2C114&sr=8-1&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0'
        
        prod_info = Product(user_agent, link)
        
        product_name = 'AMD Ryzen 5 5600X 6-core 12-Thread Unlocked Desktop Processor with Wraith Stealth Cooler'

        fetched_name = prod_info.name
        # expected, actual
        self.assertEqual(product_name, fetched_name)

    def test_fetch_price(self):


        self.assertEqual(product_price, fetched_price)



if __name__ == '__main__':
    unittest.main()
