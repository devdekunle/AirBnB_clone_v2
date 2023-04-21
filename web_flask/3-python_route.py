#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
/python/(<text>): display “Python ”,
followed by the value of the text variable
(replace underscore _ symbols with a space )
The default value of text is “is cool”
"""
from flask import Flask, url_for


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/c/<text>')
def display_c(text):
    return 'C {}'.format(text.replace('_', " "))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def display_python(text):
    'python page'
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
