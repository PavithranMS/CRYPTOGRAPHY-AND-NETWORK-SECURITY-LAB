import socket
import numpy as np

def mod_inverse_matrix(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  
    det_inv = pow(det, -1, mod)  
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  
    return (det_inv * adjugate) % mod

def hill_cipher_decrypt(encrypted_text, key_matrix):
    key_matrix_inv = mod_inverse_matrix(key_matrix, 26)
    
    encrypted_numeric = [ord(char) - ord('A') for char in encrypted_text]
    decrypted_text = ""
    
    for i in range(0, len(encrypted_numeric), 2):
        pair = np.array(encrypted_numeric[i:i+2])
        decrypted_pair = np.dot(key_matrix_inv, pair) % 26
        decrypted_text += ''.join(chr(num + ord('A')) for num in decrypted_pair)
    
    return decrypted_text

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 11345))
print("Connected to server.")

while True:
    encrypted_message = client_socket.recv(1024).decode()

    if encrypted_message.lower() == 'bye':
        break

    key_matrix_data = client_socket.recv(1024)
    key_matrix = np.frombuffer(key_matrix_data, dtype=int).reshape(2, 2)

    print(f"Encrypted message from server: {encrypted_message}")

    decrypted_message = hill_cipher_decrypt(encrypted_message, key_matrix)
    print(f"Decrypted message: {decrypted_message}")

client_socket.close()
