import requests

url = "https://pay.wasu.com/wasuPay/mapi/v2/cashierdesk.do"

payload = "{\r\"tradeMoney\":\"1\",\r\"charset\":\"utf-8\",\r\"businessCode\":\"wasu_mshop\",\r\"certType\":\"3\"," \
          "\r\"certValue\":\"111800609120F0C24CD1A3FF\",\r\"tradeBillNo\":\"766\"," \
          "\r\"merchantId\":\"00000018121700239\",\r\"subject\":\"有机蔬菜宅配体验卡\"," \
          "\r\"sign\":\"18191e41af23b175971fbb9ee416d0dc\"," \
          "\r\"notifyURL\":\"http://125.210.127.99:6761/payCallBack\",\r\"deviceCode\":\"111800609120F0C24CD1A3FF\"," \
          "\r\"serviceName\":\"payment.request.cashierdesk.jsapi\",\r\"areaCode\":\"010101\"\r} "
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.content)


