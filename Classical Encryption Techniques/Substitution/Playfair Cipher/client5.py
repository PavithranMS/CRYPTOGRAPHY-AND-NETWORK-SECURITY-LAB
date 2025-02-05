import socket

def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j

def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 0:
        char1 = matr[e1r][4]
    else:
        char1 = matr[e1r][e1c-1]

    char2 = ''
    if e2c == 0:
        char2 = matr[e2r][4]
    else:
        char2 = matr[e2r][e2c-1]

    return char1, char2

def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 0:
        char1 = matr[4][e1c]
    else:
        char1 = matr[e1r-1][e1c]

    char2 = ''
    if e2r == 0:
        char2 = matr[4][e2c]
    else:
        char2 = matr[e2r-1][e2c]

    return char1, char2

def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2

def decryptByPlayfairCipher(Matrix, CipherList):
    PlainText = []
    for i in range(0, len(CipherList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, CipherList[i][0])
        ele2_x, ele2_y = search(Matrix, CipherList[i][1])
        if ele1_x == ele2_x:
            c1, c2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = decrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        cipher = c1 + c2
        PlainText.append(cipher)
    return PlainText

def removeFillerLetters(decryptedText, filler='x'):
    return decryptedText.replace(filler, '')

def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 19345))

print("Connected to server.")
cipherText = client_socket.recv(1024).decode()
print("Cipher Text from Server:", cipherText)

key = client_socket.recv(1024).decode()
print("Key for Playfair cipher:", key)

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Matrix = generateKeyTable(key, list1)

plainTextList = Diagraph(cipherText)

decryptedList = decryptByPlayfairCipher(Matrix, plainTextList)

decryptedText = "".join(decryptedList)
decryptedText = removeFillerLetters(decryptedText)

print("Decrypted Text:", decryptedText)

client_socket.close()
