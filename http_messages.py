import requests

r = requests.get('https://www.google.com')
request_object = r.request.headers
response_object = r.headers

print("Request Header:")
for key, value in request_object.items():
    print(f"{key}: {value}")

print("\nResponse Header:")
for key, value in response_object.items():
    print(f"{key}: {value}")
