import json

# comment out below line when you deploy to spring cloud data flow 
#payload = '{ "InvoiceNo":536365, "StockCode":"85123A", "Description":"WHITE HANGING HEART T-LIGHT HOLDER", \
#        "Quantity":6, "InvoiceDate": "12/1/2010  8:26:00 AM" , "UnitPrice": 2.55 , "BuyPrice": 3, "CustomerID": 1780, "Country": "United Kingdom"}'

data = json.loads(payload)

#Transforming data  - price * quantity
TotalUnitPrice = data["Quantity"] * data["UnitPrice"]

#Transforming data  - price * quantity
TotalBuyPrice = data["Quantity"] * data["BuyPrice"]
Deviation = TotalBuyPrice - TotalUnitPrice

data["TotalUnitPrice"] = TotalUnitPrice
data["TotalBuyPrice"]  = TotalBuyPrice
data["Deviation"]      = Deviation

result = data 

 