import sys, json

starting_price = [1,1] #here you add the prices at which you bought your bitcoin

for i in [" "," "]: #adds whitespace for curl
    print(i)

with open("btc_price.json", "r") as fp: #$curl will acces the coinbase price API and turn the response in a .json file
    obj = json.load(fp)                 #this will load the JSON file


btc_price_overview = obj["bpi"] #creats a new dictionary from the bitcoin price dictionary in JSON file

euro_price_overview=btc_price_overview["EUR"]  #creats a new dictionary from the bitcoin price dictionary in JSON file
euro_price=euro_price_overview["rate_float"]  #creats a new dictionary from the bitcoin price dictionary in JSON file

for i in starting_price:
    return_btc=(euro_price-i)/i     #this calculates the return on assets
    print("Return on Asset No."+str(starting_price.index(i)+1)+": "+str(round(return_btc,4)*100)+"%") #this is the output example: Return on Asset No. [1]: 27.33%

print("Bitcoin Price: "+ str(euro_price))