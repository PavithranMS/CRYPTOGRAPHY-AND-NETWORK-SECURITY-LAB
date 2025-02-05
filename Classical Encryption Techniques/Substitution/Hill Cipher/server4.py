import socket
import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"  
    
    plaintext_numeric = [ord(char) - ord('A') for char in plaintext]
    encrypted_text = ""
    
    for i in range(0, len(plaintext_numeric), 2):
        pair = np.array(plaintext_numeric[i:i+2])
        encrypted_pair = np.dot(key_matrix, pair) % 26
        encrypted_text += ''.join(chr(num + ord('A')) for num in encrypted_pair)
    
    return encrypted_text

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 11345))
server_socket.listen(1)

conn, addr = server_socket.accept()
print("Client connected.")

while True:
    plaintext = input("Enter plaintext (letters only): ")
    print("Enter 2x2 key matrix (numbers only):")
    key_matrix = []
    for _ in range(2):
        row = list(map(int, input().split()))
        key_matrix.append(row)
    
    key_matrix = np.array(key_matrix)

    encrypted_message = hill_cipher_encrypt(plaintext, key_matrix)
    print(f"Encrypted message: {encrypted_message}")

    conn.send(encrypted_message.encode())
    conn.sendall(key_matrix.tobytes())

    if plaintext.lower() == 'bye':
        print("Server disconnected.")
        break

conn.close()
server_socket.close()
