import socket
from Crypto.Cipher import DES
import base64

KEY = b'8bytekey'  
IV = b'12345678'  

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_message(message):
    cipher = DES.new(KEY, DES.MODE_CBC, IV)
    padded_text = pad(message).encode()
    encrypted_bytes = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_bytes).decode()

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12395))
server_socket.listen(1)

conn, addr = server_socket.accept()
print("Client connected.")

while True:
    message = input("Enter message to encrypt (or type 'exit' to stop): ")
    if message.lower() == 'exit':
        conn.send('exit'.encode())
        break
    encrypted_msg = encrypt_message(message)
    conn.send(encrypted_msg.encode())
    print(f"Sent encrypted message: {encrypted_msg}")

conn.close()
server_socket.close()
