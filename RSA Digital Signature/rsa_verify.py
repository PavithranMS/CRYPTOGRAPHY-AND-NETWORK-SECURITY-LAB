import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12355))
print("Connected to server.")

p = 17
q = 11
n = p * q
e = 7

msg = int(client_socket.recv(1024).decode())
print(f"Received Message: {msg}")

# Acknowledge message received
client_socket.send("ACK".encode())

signature = int(client_socket.recv(1024).decode())
print(f"Received Signature: {signature}")

decrypted_msg = pow(signature, e, n)
print(f"Decrypted Message from Signature: {decrypted_msg}")

if decrypted_msg == msg:
    print("Signature is valid!")
else:
    print("Signature is invalid.")

client_socket.close()
