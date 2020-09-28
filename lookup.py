#!/usr/bin/env python
import json
import argparse
import sys
import optparse
from optparse import OptionParser

# Load the json data
with open('./data.json') as jsondata:
  countrycodes = json.load(jsondata)

def main(args):
        get_country_names(args)

def get_country_names(args):
# Get country codes
  list = args.countryCode.split(',')

  # Output country name based on country codes
  for val in list:
      #print ("Country code: %s" % val)
      if val in countrycodes['data']:
       if 'name' in countrycodes['data'][val]:
         print(val, "is country code for: ", countrycodes['data'][val]['name'])
      else:
         print("Invalid country code")


if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Get country name(s) ')
   parser.add_argument('--countryCode', required=True, help='Enter comma delimited country code(s)')
   args = parser.parse_args()
   main(args)
