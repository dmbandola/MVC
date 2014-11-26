#redirect function is used to forward user to full url 
#if he came from shortened
#Request us used to encapsulate HHTP request. IT will contain request
#methids, request arguments and other related information from flask
#import redirect, render_template, request, Flask
#from werkzeug.exceptions import BadRequest, NotFound

import models

#Initialize Flask application
app = Flask(__name__, template_folder='views')

@app.route("/")
def index():
    """Renders main page."""
    return render_template('main_page.html')

@app.route("/shorten/")

