import socket

def vernam_cipher(ciphertext, key):
    plaintext = ""
    if len(key) != len(ciphertext):
        print("Error: Key must be the same length as the ciphertext.")
        return None
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i]))
    return plaintext

# Client setup
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12355))
print("Connected to server.")

while True:
    encrypted_message = client_socket.recv(1024).decode()

    if encrypted_message.lower() == 'bye':
        break

    print(f"Encrypted message from server: {encrypted_message}")

    key = input("Enter decryption key (must be the same length as the encrypted message): ")

    decrypted_message = vernam_cipher(encrypted_message, key)
    if decrypted_message is None:
        continue

    print(f"Decrypted message: {decrypted_message}")

client_socket.close()
