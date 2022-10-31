#/usr/bin/python3
"""
Publishing to web using Flask
"""

# import main 
from main import *
# import scrape
#from scrape import *
# import flask_classful
#from flask_classful import FlaskView, route
# import flask views
from flask.views import View


<<<<<<< HEAD
    @app.route('/ryzen_55600x/index.html', methods=['POST', 'GET'])
    def product_page(p):
        #TODO: Modify to allow for multiply possible products.
        # return product page filling in the necessary elements
        return render_template('ryzen_55600x/index.html', p.name=name)
=======
@app.route('/', methods=['GET'])
def home_page():
    #print("<--------- DEBUG --------->")
    #print(p.name)

    return render_template('index.html')
>>>>>>> 5698cd7 (Trying to bridge independent python code with flask-based python methods)

@app.route('/ryzen_55600x/<p_attrs>', methods=['POST', 'GET'])
def product_page(p_attrs):
    product_name = p_attrs
    print("<------------ DEBUG ------------>")
    print (product_name)
    name = 'TEST'
    print(name)

    # return product page filling in the necessary elements
    #return render_template('ryzen_55600x/index.html', product_name='name')
    page = render_template('ryzen_55600x/index.html', name=product_name)
    return page

# fun flask app
app.run(debug=True)
        
