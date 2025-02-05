import socket

def caesar_cipher_decrypt(text, shift):
    decrypted = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted += char
    return decrypted

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12347))
print("Connected to server.")

shift = 3  # Caesar Cipher shift value
while True:
    encrypted_message = client_socket.recv(1024).decode()
    if encrypted_message.lower() == 'bye':
        print("Server disconnected.")
        break
    print("Encrypted Message Received:", encrypted_message)
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print("Decrypted Message:", decrypted_message)

client_socket.close()
