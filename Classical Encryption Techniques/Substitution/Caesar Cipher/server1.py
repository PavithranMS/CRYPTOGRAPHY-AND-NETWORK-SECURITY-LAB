import socket

def caesar_cipher_encrypt(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12347))
server_socket.listen(1)

conn, addr = server_socket.accept()
print("Client connected.")

shift = 3  # Caesar Cipher shift value
while True:
    message = input("Enter Plaintext: ")
    encrypted_message = caesar_cipher_encrypt(message, shift)
    conn.send(encrypted_message.encode())
    if message.lower() == 'bye':
        break
    print("Encrypted Message Sent:", encrypted_message)

conn.close()
server_socket.close()
