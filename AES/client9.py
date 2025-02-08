import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY = b"mysecurekey12345"  

def aes_decrypt(encrypted_data):
    iv = encrypted_data[:16]  
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    
    decrypted_data = cipher.decrypt(encrypted_data[16:])  
    unpadded_data = unpad(decrypted_data, AES.block_size)
    
    return unpadded_data.decode('utf-8')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12348))

message_size = int(client_socket.recv(4).decode('utf-8').strip())
encrypted_message = client_socket.recv(message_size)

print(f"Encrypted message received: {encrypted_message.hex()}")

decrypted_message = aes_decrypt(encrypted_message)
print(f"Decrypted message: {decrypted_message}")

client_socket.close()
