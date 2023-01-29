import requests
import json

url = 'http://localhost:9696/predict'
data = 'https://upload.medbullets.com/question/103329/images/breastcyst.jpg'
img_url = {'img_url': data}
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json.dumps(img_url),headers=headers)
result = response.json()
print (result)
#print(response.status_code) #print status response code



