#/usr/bin/python3
"""
Publishing to web using Flask
"""

# import main 
from main import *
# import scrape

class Website:
    #def __init__(self, p):
    #    self.product = p
    """
    Website class routing our parsed values from scrape to our defined HTML
    elements defined in /template/
    """
    @app.route('/', methods=['GET'])
    def home():
        #print("<--------- DEBUG --------->")
        #print(p.name)
        # return home page
        return render_template('index.html')

    @app.route('/ryzen_55600x/index.html', methods=['POST', 'GET'])
    def product_page(p):

        # return product page filling in the necessary elements
        return render_template('ryzen_55600x/index.html', p.name=name)

