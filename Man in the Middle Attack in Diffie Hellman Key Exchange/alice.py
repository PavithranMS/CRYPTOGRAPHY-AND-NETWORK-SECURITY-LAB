import socket

P = 41
G = 7
ALICE_PRIVATE = 11 

alice_public = pow(G, ALICE_PRIVATE, P)  

alice_socket = socket.socket()
alice_socket.connect(('127.0.0.1', 9999)) 

alice_socket.send(str(alice_public).encode())  
fake_bob_public = int(alice_socket.recv(1024).decode()) 

shared_secret = pow(fake_bob_public, ALICE_PRIVATE, P)  

print(f"Alice's Private Key: {ALICE_PRIVATE}")
print(f"Alice's Public Key: {alice_public}")
print(f"Alice's Shared Secret Key: {shared_secret}")

alice_socket.close()
