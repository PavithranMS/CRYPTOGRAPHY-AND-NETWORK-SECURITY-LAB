import socket
import math

key = "HACK"

def encryptMessage(msg):
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    
    col = len(key)
    row = int(math.ceil(msg_len / col))
    
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12365))
server_socket.listen(1)

conn, addr = server_socket.accept()
print("Client connected.")

message = input("Enter message to encrypt: ")
ciphertext = encryptMessage(message)
print("Encrypted message:", ciphertext) 
conn.send(ciphertext.encode())

conn.close()
server_socket.close()
