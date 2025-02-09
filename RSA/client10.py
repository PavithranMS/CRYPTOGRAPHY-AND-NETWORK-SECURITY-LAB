import socket

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo //= 2
    return res

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1  

def decrypt(c, d, n):
    return power(c, d, n)

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12355))
print("Connected to server.")

e_n_data = client_socket.recv(1024).decode()
e, n = map(int, e_n_data.split(','))

p = 17
q = 11
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)

while True:
    encrypted_msg = client_socket.recv(1024).decode()
    if encrypted_msg.lower() == 'exit':
        break
    
    print(f"Received Cipher Text: {encrypted_msg}")

    decrypted_msg = decrypt(int(encrypted_msg), d, n)
    print(f"Decrypted Message: {decrypted_msg}")

client_socket.close()
