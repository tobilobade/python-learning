#This is how to set up a server
# Step 1: import the socket module
# Step 2: Create a socket object
# Step 3: Get current machine name
# Step 4: Get port number for connection
# Step 5:  Bind with address
# Step 6: listen for connection
# Step 7
#



import socket

# s= socket.socket()
# print(socket.gethostname())
# host= '0.0.0.0'#socket.gethostname()
# port=9999


# s.bind((host, port)) #joining the host and the port
# print("waiting for connection...")
# s.listen(5)

# while True:
#     conn,addr=s.accept()
#     print("Got Connection from", addr)
#     conn.send("Server saying hi".encode())
#     conn.close()

def server_program():
    
    host= '0.0.0.0'#socket.gethostname()
    port=9999

    s= socket.socket()

    s.bind((host, port)) #joining the host and the port
    s.listen(2)
    print("waiting for connection")
    conn,addr=s.accept()
    print("connection from..."+ str(addr))

    while True:
        data= conn.recv(1024).decode()
        if not data:
            break
        print ("from connected user: " +str(data))
        data= input('->')
        conn.send(data.encode())
    
    conn.close()

if __name__=='__main__':
    server_program()