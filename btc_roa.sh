#!/bin/bash

#this accesses the coinbase API to request the current bitcoin price and creates file btc_price.json used in the python script
curl https://api.coindesk.com/v1/bpi/currentprice.json -sS -o btc_price.json #-sS hides the progress of CURL

#runs python script
python btc_roa.py 

#removes the JSON file. no unnecessary files
rm btc_price.json
