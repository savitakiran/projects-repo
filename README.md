# projects-repo

# Craft Demo

This is a simple python script to quickly lookup country codes. It supports multiple country codes separated by commas as input.

Usage: lookup.py [-h] --countryCode COUNTRYCODE

Enter comma delimited country codes

Example:
  lookup.py --countryCode=AU,AL
  
# Bonus part
Expose craft demo functionality via REST with three routes

1. /diag - returns the status of api https://www.travel-advisory.info/api

2. /health - returns basic Liveness health check of the service

3. /convert - returns country name(s) for a given country code(s)

# Deploy the service to local k8s cluster
Use the YAML file deploy the service
  kubectl apply -f deployment-craft-demo-v2.yaml
  
Execute the following command to see the pods running:
  kubectl get pods
 
Navigate to http://localhost:7001/diag, http://localhost:7001/health, http://localhost:7001/convert?countrycode=AU,AL


