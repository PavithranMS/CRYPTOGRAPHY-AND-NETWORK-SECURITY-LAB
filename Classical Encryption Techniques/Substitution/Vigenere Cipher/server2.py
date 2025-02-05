import socket

def encrypt(plaintext, key):
    ciphertext = ""
    key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i].lower()) - ord('a')
            if plaintext[i].isupper():
                ciphertext += chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += plaintext[i]
    
    return ciphertext

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12349))
server_socket.listen(1)

conn, addr = server_socket.accept()
print("Client connected.")

while True:
    plaintext = input("Enter plaintext: ")
    key = input("Enter encryption key: ")

    ciphertext = encrypt(plaintext, key)
    print(f"Encrypted message: {ciphertext}")
    
    conn.send(ciphertext.encode())

    if plaintext.lower() == 'bye':
        print("Server disconnected.")
        break

conn.close()
server_socket.close()
