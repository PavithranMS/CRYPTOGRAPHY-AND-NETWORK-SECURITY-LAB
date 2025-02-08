import socket
from Crypto.Cipher import DES
import base64

KEY = b'8bytekey'  
IV = b'12345678'  

def decrypt_message(encrypted_message):
    cipher = DES.new(KEY, DES.MODE_CBC, IV)
    decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_bytes.decode().rstrip()

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12395))
print("Connected to server.")

while True:
    encrypted_msg = client_socket.recv(1024).decode()
    if encrypted_msg.lower() == 'exit':
        print("Server closed the connection.")
        break
    decrypted_msg = decrypt_message(encrypted_msg)
    print(f"Received encrypted message: {encrypted_msg}")
    print(f"Decrypted message: {decrypted_msg}")

client_socket.close()
