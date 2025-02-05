import socket

def encryptRailFence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 17345))
    server.listen(1)
    client_socket, addr = server.accept()
    print("Client connected.")

    message = input("Enter the plaintext: ")
    rails = int(input("Enter the number of rails: "))
    encrypted_message = encryptRailFence(message, rails)
    print("Encrypted message:", encrypted_message)
    client_socket.send(f"{encrypted_message};{rails}".encode('utf-8'))
    
    client_socket.close()
    server.close()

if __name__ == "__main__":
    start_server()
