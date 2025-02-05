import socket

def decrypt(ciphertext, key):
    plaintext = ""
    key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i].lower()) - ord('a')
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(ciphertext[i]) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += ciphertext[i]
    
    return plaintext

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12349))
print("Connected to server.")

while True:
    encrypted_message = client_socket.recv(1024).decode()
    print(f"Encrypted message from server: {encrypted_message}")

    key = input("Enter decryption key: ")
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

    if encrypted_message.lower() == 'bye':
        break

client_socket.close()
