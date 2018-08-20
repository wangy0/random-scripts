import requests
import datetime
import re
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

now = datetime.datetime.now()

date = str(now.month) + "%2F" + str(now.day) + "%2F" + str(now.year)

headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

request = "https://usa.visa.com/support/consumer/travel-support/exchange-rate-calculator.html/?amount=1&fee=0&fromCurr=USD&toCurr=MXN&exchangedate=" + date + "&submitButton=Calculate+exchange+rate"

r = requests.get(request,headers=headers)

pattern = re.compile("Mexican Peso = <strong class=\"converted-amount-value\"> ........ ")

m = pattern.search(r.text)

pattern2 = re.compile("0.+ ")

m2 = pattern2.search(m.group(0))

pesoValue = float(m2.group(0))

visaExchangePrice = 1/pesoValue

print(visaExchangePrice)

