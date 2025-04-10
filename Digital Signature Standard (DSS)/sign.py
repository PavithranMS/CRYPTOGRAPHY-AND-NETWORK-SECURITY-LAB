import socket
import random

p = 288 
q = 47 
g = 60  
h = 41
k = 18
x = 24 

y = pow(g, x, p)  

print("Server Private Key (x): ",x)
print("Server Public Key (y): ",y)

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)

conn, addr = server_socket.accept()

r = pow(g, k, p) % q  
s = (pow(k, -1, q) * (h + x * r)) % q  

print(f"Signature (r): {r}")
print(f"Signature (s): {s}")

conn.send(f"{r},{s},{y}".encode())  

conn.close()
server_socket.close()
