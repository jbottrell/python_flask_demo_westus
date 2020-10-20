from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__)

@app.route('/home')
def homepage():
    #Print("Is this thing on?")
    return "<h1>Hello World!</h1>"

@app.route('/')
def test():
    response = requests.get("https://api.weather.gov/gridpoints/DTX/53,38/forecast")
    text = response.text
    json_string = json.loads(text)
    properties = json_string['properties']
    periods = properties['periods']
    ## periods is a list
    ##day1
    day1 = periods[0]
    name1 = day1["name"]
    temp1 = day1["temperature"]
    cast1 = day1["shortForecast"]
    ##day2
    day2 = periods[1]
    name2 = day2["name"]
    temp2 = day2["temperature"]
    cast2 = day2["shortForecast"]
    ##day3
    day3 = periods[2]
    name3 = day3["name"]
    temp3 = day3["temperature"]
    cast3 = day3["shortForecast"]
    ##day4
    day4 = periods[3]
    name4 = day4["name"]
    temp4 = day4["temperature"]
    cast4 = day4["shortForecast"]
    ##day5
    day5 = periods[4]
    name5 = day5["name"]
    temp5 = day5["temperature"]
    cast5 = day5["shortForecast"]
    return render_template("east.html", day1name=name1, day2name=name2, day3name=name3, day4name=name4, day5name=name5, day1temp=temp1, day2temp=temp2, day3temp=temp3, day4temp=temp4, day5temp=temp5, day1cast=cast1, day2cast=cast2, day3cast=cast3, day4cast=cast4,day5cast=cast5)

if __name__ == '__main__':
    app.run()
#this is a comment