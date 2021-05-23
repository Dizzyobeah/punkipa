from flask import Flask, render_template, abort, url_for
import html
from punkrequest import PunkIPA
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('punkbeers.json', 'r') as beerfile:
        beers = beerfile.read()
        beerdata =json.loads(beers)
        # return render_template('index.html', title="Punk IPA", records=beers)
        return render_template('index.html', title="Punk IPA", records=beerdata)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)