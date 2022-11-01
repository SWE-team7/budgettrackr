#!/usr/bin/python3
"""
Publishing to web using Flask
"""

# import main
from main import *
# import scrape
from scrape import *
# import flask_classful
#from flask_classful import FlaskView, route
# import flask views
from flask.views import View


class Website:
    def __init__(self):
        self.home_page = home_page()
        self.product_page = product_page()

    @app.route('/', methods=['GET'])
    def home_page():
        return render_template('index.html')

    @app.route('/ryzen_55600x/index.html', methods=['POST', 'GET'])
    def product_page():

        #product_name = p_attrs
        user_agent = ({'User-Agent':
                       'Mozilla/5.0 (X11; Linux x86_64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/72.0.3626.121 Safari/537.36',
                       'Accept-Language': 'en-US, en;q=0.5'
                       })
        # source file
        link = 'https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_1?crid=1B7QEPTT5XCBH&keywords=amdryzen+5000&qid=1665786908&qu=eyJxc2MiOiIzLjA1IiwicXNhIjoiMi44NCIsInFzcCI6IjIuMTUifQ%3D%3D&sprefix=amd%2520ryzen%25205000%2Caps%2C114&sr=8-1&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0'

        # call product class
        p = Product(user_agent, link)

        # return product page filling in the necessary elements
        page = render_template('ryzen_55600x/index.html',
                               name=p.name,
                               price=p.price,
                               reviews=p.rating)
        return page


# fun flask app
app.run(host='0.0.0.0', threaded=False)
