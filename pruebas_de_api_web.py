import requests
'''
response = requests.get("https://api.frankfurter.app/latest")
print(response)

response = requests.get("https://api.frankfurter.app/latest")
print(response.json())

params = {"from":"USD", "to":"GBP", "amount":20}
res = requests.get("https://api.frankfurter.app/latest", params=params)
print(res.json())
'''

response = requests.get("https://api.frankfurter.app/latest")

print(response.headers['Server'])
print(response.headers['Content-Type'])
print(response.headers['Content-Encoding'])