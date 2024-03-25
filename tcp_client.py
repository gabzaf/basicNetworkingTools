import socket

target_host = "google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

client.connect((target_host,target_port))

client.send(b"GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")

response = client.recv(4096)
print(response.decode())
client.close()