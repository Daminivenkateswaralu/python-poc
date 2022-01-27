import re
from django.http import response
import requests
# Simple Get Request to return response body as json
# response = requests.get("http://127.0.0.1:5000/result/?query=https://www.jiosaavn.com/song/venmathiye/CSMEWkd,bkQ&lyrics=true")
# print(response.json())

# # download an image
# response = requests.get("https://images.app.goo.gl/yepmL3dYLF2VNpsM7")
# with open("image.png", "wb") as f:
#     f.write(response.content)

# # pass query params as payload
# payload = {'page': 3, 'count':10}
# response = requests.get("http://httpbin.org/get", params=payload)
# print(response.url)
# print(response.json())
# print(response.text)

# # post data to an url
# postData = {'name': 'Damini', 'email': 'dams@gmail.com'}
# response = requests.post("http://httpbin.org/post", data= postData)
# response_dict = response.json()
# print(response_dict['form'])

# basic auth
response = requests.get("http://httpbin.org/basic-auth/damini/dams", auth=('damini', 'dams'))
print(response.text)
