import json
from flask import Flask
from flask_cors import CORS

data = json.load(open("allCountriesV3.json","r",  encoding="utf8"))
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return json.dumps(data)


@app.route('/country/<country_name>')


def country_by_name(country_name):
    country = {}
    for c in data:
        if c["name"]["common"].lower() == country_name.lower():
            country = c
            break
    return json.dumps(country)
