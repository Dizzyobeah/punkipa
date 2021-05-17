import requests
import os
from flask import Flask, render_template, abort, url_for
import html
import json


class PunkIPA:
    def __init__(self):
        self.url = os.getenv('punk_url')

    def punk_request(self):
        result = requests.get(self.url)
        beers = result.json()
        return beers
       
app = Flask(__name__)


@app.route("/")
def index():
    brew = punk.punk_request()
    return render_template('index.html', title="Punk IPA", records=brew)


if __name__ == '__main__':
    punk = PunkIPA()
    
    app.run(host='localhost', debug=True)