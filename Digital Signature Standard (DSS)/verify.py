import socket

p = 288 
q = 47 
g = 60   
k = 18
h = 41
x = 24

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12345))

response = client_socket.recv(1024).decode()
r, s, y = map(int, response.split(','))

print(f"Received Signature (r): {r}")
print(f"Received Signature (s): {s}")
print(f"Received Public Key (y): {y}")

w = pow(s, -1, q)  
print(f"Computed w: {w}")

u1 = (h * w) % q  
u2 = (r * w) % q  

print(f"Computed u1: {u1}")
print(f"Computed u2: {u2}")

v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q  

print(f"Computed v: {v}")

if v == r:
    print("Signature is VALID.")
else:
    print("Signature is INVALID.")

client_socket.close()
