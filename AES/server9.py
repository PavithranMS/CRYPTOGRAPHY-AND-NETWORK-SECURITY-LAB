import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

KEY = b"mysecurekey12345"  

def aes_encrypt(plaintext):
    iv = get_random_bytes(16)  
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    
    return iv + encrypted_data 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12348))
server_socket.listen(1)

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

plaintext = input("Enter plaintext: ")

encrypted_message = aes_encrypt(plaintext)
print(f"Encrypted message sent: {encrypted_message.hex()}")

conn.sendall(f"{len(encrypted_message):<4}".encode('utf-8'))
conn.sendall(encrypted_message)

conn.close()
server_socket.close()
