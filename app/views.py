"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
<<<<<<< HEAD

=======
>>>>>>> ff70fe011bdd3fa076a6fd0198eb637de3b471ab
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
<<<<<<< HEAD
from datetime import datetime, date
import time
from time import strftime 

=======
>>>>>>> ff70fe011bdd3fa076a6fd0198eb637de3b471ab


###
# Routing for your application.
###

<<<<<<< HEAD
@app.route ('/profile/')
def profile ():
    
     time_info =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     
     """Render profile"""
     
     return render_template('profile.html')
    
@app.route ('/timeinfo/')
def timeinfo ():
    
    """ Render timeinfo"""
    
    time_info =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return time_info
    
=======
>>>>>>> ff70fe011bdd3fa076a6fd0198eb637de3b471ab
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
<<<<<<< HEAD
    return render_template('about.html')
=======
    return render_template('about.html', name="Mary Jane")
>>>>>>> ff70fe011bdd3fa076a6fd0198eb637de3b471ab


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True,host="0.0.0.0",port="8080")


=======
    app.run(debug=True,host="0.0.0.0",port="8080")
>>>>>>> ff70fe011bdd3fa076a6fd0198eb637de3b471ab
