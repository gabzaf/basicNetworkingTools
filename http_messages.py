import requests

r = requests.get('http://www.google.com')
request_header = r.request.headers
response_header = r.headers

print("Request Message:")
print("Method:",r.request.method)
for key, value in request_header.items():
    print(f"{key}: {value}")
print("\nResponse Message:")
print("Status Code:", r.status_code)
for key, value in response_header.items():
    print(f"{key}: {value}")
