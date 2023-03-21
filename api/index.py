import json
from flask import Flask
from flask_cors import CORS

countries = json.load(open("allCountriesV3.json", "r",  encoding="utf8"))
app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return json.dumps(countries)


@app.route('/name/<country_name>')
def country_by_name(country_name):
    country_name = country_name.replace("%20", " ")

    def select_name(c): return True if c["name"]["common"].lower(
    ) == country_name.lower() else False

    countries_by_name = list(filter(select_name, countries))
    return json.dumps(countries_by_name)
