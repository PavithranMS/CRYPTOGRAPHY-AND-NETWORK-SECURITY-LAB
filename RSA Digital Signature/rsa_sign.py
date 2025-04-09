import socket

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

p = 17
q = 11
n = p * q
phi = (p - 1) * (q - 1)
e = 7
d = mod_inverse(e, phi)

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12355))
server_socket.listen(1)

conn, addr = server_socket.accept()
print("Client connected.")

msg = int(input("Enter a number to sign: "))
signature = pow(msg, d, n)

print(f"Original Message: {msg}")
print(f"Signature: {signature}")

conn.send(str(msg).encode())
conn.recv(1024)  # wait for acknowledgment before sending signature
conn.send(str(signature).encode())

conn.close()
server_socket.close()
