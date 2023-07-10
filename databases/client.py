# Step 1: Get current machine name
# Step 2: Client wants to connect to server
# Step 3: Get port number above 1024
# 1024 is buf size or max amount of data can be received at once
# Step 5: close connection

from socket import socket

server = "172.20.10.3" #This was my hotpost ip address
port = 9999
client = socket()
client.connect((server, port))

server_msg = client.recv(1024)
print(server_msg.decode())

client.close()