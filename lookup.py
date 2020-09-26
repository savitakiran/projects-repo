#!/usr/bin/env python
# import json module
import json
import sys
from optparse import OptionParser

# Load the json data
with open('./data.json') as jsondata:
  countrycodes = json.load(jsondata)

def main():
  if len(sys.argv) < 2:
        print("Need country code parameter")
        print("Usage: ", sys.argv[0], "--countryCode=AU,AL")
  else:
        get_country_names()

def get_country_names():
# Get country codes
  keys = ["--countryCode="]                                                                                                    
  for i in range(1,len(sys.argv)):                                                                                             
    for key in keys:
        if sys.argv[i].find(key) == 0:
            arg_set = sys.argv[i][len(key):]
            list1 = arg_set.split(',')
            break

    # Output based on country codes
    for val in list1:
      print ("Country code: %s" % val)
      if val in countrycodes:
       if 'name' in countrycodes['data'][val]:
         print(countrycodes['data'][val]['name'])
      else:
         print("Invalid country code")


if __name__ == "__main__":
   main()