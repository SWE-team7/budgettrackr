#/usr/bin/python3
"""
Publishing to web using Flask
"""

# import main 
from main import *

# declare our flask app
#app = Flask(__name__)


class Website:
    """
    Website class routing our parsed values from scrape to our defined HTML
    elements defined in /template/
    """
    @app.route('/', methods=['GET'])
    def home():
        # return home page
        return render_template('index.html')

    @app.route('/ryzen_55600x/index.html', methods=['POST', 'GET'])
    def product_page():
        # return product page
        return render_template('ryzen_55600x/index.html')


