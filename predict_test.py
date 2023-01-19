import requests
from flask import Response

url = 'http://localhost:9696/predict'

img_url = {"url": "https://img.medscapestatic.com/pi/meds/ckb/39/15939tn.jpg"}


#response = requests.post(url, json=img).json()
response = requests.post(url, json = img_url).json()#, stream = True
print(response)

if response == 'Benign':
    print("Pretty sure that's Benign Cancer")
else:
    print("Pretty sure that's Malignant Cancer")