import socket
import random

P = 41
G = 7

XD1 = 9  
XD2 = 4  

YD1 = pow(G, XD1, P)  
YD2 = pow(G, XD2, P)  

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 9999))
server_socket.listen(1)
alice_conn, _ = server_socket.accept()  

Ya = int(alice_conn.recv(1024).decode())  

bob_socket = socket.socket()
bob_socket.connect(('127.0.0.1', 8888))
bob_socket.send(str(YD1).encode())  
Yb = int(bob_socket.recv(1024).decode()) 

alice_conn.send(str(YD2).encode())  

K1 = pow(Ya, XD2, P)  
K2 = pow(Yb, XD1, P)  

print(f"Darth's Private Key for Alice: {XD1}")
print(f"Darth's Private Key for Bob: {XD2}")
print(f"Darth's Fake Public Key for Alice: {YD1}")
print(f"Darth's Fake Public Key for Bob: {YD2}")
print(f"Darth's Shared Secret with Alice (K1): {K1}")
print(f"Darth's Shared Secret with Bob (K2): {K2}")

alice_conn.close()
bob_socket.close()
server_socket.close()
