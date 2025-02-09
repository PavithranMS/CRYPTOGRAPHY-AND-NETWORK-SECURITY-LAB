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

def encrypt(m, e, n):
    return power(m, e, n)

p = 17
q = 11
n = p * q
phi = (p - 1) * (q - 1)
e = 7  

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12355))
server_socket.listen(1)

conn, addr = server_socket.accept()
print("Client connected.")

conn.send(f"{e},{n}".encode())

while True:
    msg = input("Enter a number to encrypt (or type 'exit' to quit): ")
    if msg.lower() == 'exit':
        conn.send("exit".encode())
        break

    try:
        msg_int = int(msg)
        encrypted_msg = encrypt(msg_int, e, n)
        print(f"Encrypted Message: {encrypted_msg}")
        conn.send(str(encrypted_msg).encode())
    except ValueError:
        print("Invalid input. Please enter a number.")

conn.close()
server_socket.close()
