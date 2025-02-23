import socket

P = 41
G = 7
BOB_PRIVATE = 13  

bob_public = pow(G, BOB_PRIVATE, P)  

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(1)
conn, addr = server_socket.accept()  

fake_alice_public = int(conn.recv(1024).decode()) 
conn.send(str(bob_public).encode())  

shared_secret = pow(fake_alice_public, BOB_PRIVATE, P)  

print(f"Bob's Private Key: {BOB_PRIVATE}")
print(f"Bob's Public Key: {bob_public}")
print(f"Bob's Shared Secret Key: {shared_secret}")

conn.close()
server_socket.close()
