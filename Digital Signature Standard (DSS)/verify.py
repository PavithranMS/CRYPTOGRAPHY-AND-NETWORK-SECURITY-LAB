import socket

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

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12345))

message = input("Enter the message to verify: ")  
client_socket.send(message.encode())  

response = client_socket.recv(1024).decode()
r, s, y = map(int, response.split(','))

print(f"Received Signature (r): {r}")
print(f"Received Signature (s): {s}")
print(f"Received Public Key (y): {y}")

h = simple_hash(message)  
print(f"Computed Hash (h): {h}")

w = pow(s, -1, q)  
print(f"Computed w: {w}")

u1 = (h * w) % q  
u2 = (r * w) % q  

print(f"Computed u1: {u1}")
print(f"Computed u2: {u2}")

v = ((mod_exp(g, u1, p) * mod_exp(y, u2, p)) % p) % q  

print(f"Computed v: {v}")

if v == r:
    print("Signature is VALID.")
else:
    print("Signature is INVALID.")

client_socket.close()
