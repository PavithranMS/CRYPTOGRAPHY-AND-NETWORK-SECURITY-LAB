import socket
import random

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def simple_hash(message):
    hash_value = 0
    for char in message:
        hash_value = (hash_value * 31 + ord(char)) % q
    return hash_value

p = 23  
q = 11  
g = 4   

x = random.randint(1, q - 1)  
y = mod_exp(g, x, p)  

print(f"Server Private Key (x): {x}")
print(f"Server Public Key (y): {y}")

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)

conn, addr = server_socket.accept()
message = conn.recv(1024).decode()

print(f"Received Message: {message}")

h = simple_hash(message)  
print(f"Computed Hash (h): {h}")

k = random.randint(1, q - 1)  
print(f"Random k: {k}")

r = mod_exp(g, k, p) % q  
s = (pow(k, -1, q) * (h + x * r)) % q  

print(f"Signature (r): {r}")
print(f"Signature (s): {s}")

conn.send(f"{r},{s},{y}".encode())  

conn.close()
server_socket.close()
