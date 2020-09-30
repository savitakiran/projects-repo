from flask import Flask,request
import requests
import json
import time

app = Flask(__name__)

def convert(args):
# Load the json data
  with open('./data.json') as jsondata:
    countrycodes = json.load(jsondata)
 
    # Get country codes
    list = args.split(',')

    # Output country name based on country codes
    country = ''
    newline = '\n'

    for val in list:
        #print ("Country code: %s" % val)
        if val in countrycodes['data']:
            if 'name' in countrycodes['data'][val]:
                country = country + val + ", is country code for: " + countrycodes['data'][val]['name']
                country += newline
        else:
            country += val + ", is invalid country code"
            country += newline
    return country

@app.route('/diag')
def diag():
    url = 'https://www.travel-advisory.info/api'
    y = requests.get(url)
    obj = y.json()
    return(obj['api_status'])

@app.route("/convert", methods=['GET'])
def get_query():
    # return request.query_string
    req = request.query_string

    check_string = 'countycode='

    if (not req):
        return "Missing argument - enter this format /convert?countrycode=AL,AK"
    else:
        args1 = request.args['countrycode']
        if (not args1):
            return 'Enter country code(s) seperated by commas'
        else:
            return convert(args1)

@app.route('/health')
def health():
    time.sleep(1)
    return "Status: OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
