import socket
import math

key = "HACK"

def decryptMessage(cipher):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    
    col = len(key)
    row = int(math.ceil(msg_len / col))
    
    key_lst = sorted(list(key))
    dec_cipher = [[None] * col for _ in range(row)]
    
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    null_count = msg.count('_')
    
    if null_count > 0:
        return msg[: -null_count]

    return msg

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12365))
print("Connected to server.")

ciphertext = client_socket.recv(1024).decode()
print("Encrypted message from server:", ciphertext)

decrypted_message = decryptMessage(ciphertext)
print("Decrypted message:", decrypted_message)

client_socket.close()
