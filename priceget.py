import requests
import json
import priceget

def get(name):
  response_API = requests.get('https://nasfaq.biz/api/getMarketInfo?all&saleValue=false&inCirculation=false')
  
  data = response_API.text
  parse_json = json.loads(data)
  
  price = parse_json['coinInfo']['data'][name]['price']
  coinname = parse_json['coinInfo']['data'][name]['coin']
  


