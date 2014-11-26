#redirect function is used to forward user to full url 
#if he came from shortened
#Request us used to encapsulate HHTP request. IT will contain request
#methids, request arguments and other related information from flask
#import redirect, render_template, request, Flask
#from werkzeug.exceptions import BadRequest, NotFound

import models
from flask import Flask, render_template, request

#Initialize Flask application
app = Flask(__name__, template_folder='views')

@app.route("/")
def index():
    """Renders main page."""
    return render_template('main_page.html')

@app.route("/shorten/")
def shorten():
    """Returns short_url of requested full_url."""
    # Vaidate user input
    full_url = request.args.get('url')
    if not full_url:
        raise BadRequest()

    #Model returns object with short_url_property
    url_model = models.Url.shorten(full_url)
    url_model.short_url

    #Pass data to view and call its render method
    short_url = request.host + '/' + url_model.short_url
    return render_template('success.html', short_url=short_url)

@app.route('/<path:path>')
def redirect_to_full(path=''):
    """Gets short url and redirects user to correspondun full url if found."""
    #Model returns object with full_url property
    url_model = models.Url.get_by_short_url(path)

    #Validate model return
    if not url_model:
        raise NotFound()

    return redirect(url_model.full_url)

if __name__ == "__main__":
    app.run(debug=True)

