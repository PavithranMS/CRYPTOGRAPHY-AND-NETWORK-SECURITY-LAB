import socket

def vernam_cipher(plaintext, key):
    ciphertext = ""
    if len(key) != len(plaintext):
        print("Error: Key must be the same length as the plaintext.")
        return None
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))
    return ciphertext

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12355))
server_socket.listen(1)

conn, addr = server_socket.accept()
print("Client connected.")

while True:
    plaintext = input("Enter plaintext: ") 
    key = input("Enter key: ")               
    
    ciphertext = vernam_cipher(plaintext, key)
    if ciphertext is None:
        continue

    print(f"Encrypted message: {ciphertext}")
    conn.send(ciphertext.encode())

    if plaintext.lower() == 'bye':
        print("Server disconnected.")
        break

conn.close()
server_socket.close()
