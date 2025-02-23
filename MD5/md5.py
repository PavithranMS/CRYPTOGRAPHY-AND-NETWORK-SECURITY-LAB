import math

def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def md5(message):
    A, B, C, D = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476
    message = bytearray(message, 'utf-8')
    message.append(0x80)

    while (len(message) * 8) % 512 != 448:
        message.append(0)

    message += (len(message) * 8).to_bytes(8, 'little')
    T = [int(2**32 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

    for i in range(0, len(message), 64):
        X = [int.from_bytes(message[j:j+4], 'little') for j in range(i, i+64, 4)]
        a, b, c, d = A, B, C, D

        for j in range(64):
            if j < 16: f, k, s = (b & c) | (~b & d), j, [7, 12, 17, 22][j % 4]
            elif j < 32: f, k, s = (d & b) | (~d & c), (5*j + 1) % 16, [5, 9, 14, 20][j % 4]
            elif j < 48: f, k, s = b ^ c ^ d, (3*j + 5) % 16, [4, 11, 16, 23][j % 4]
            else: f, k, s = c ^ (b | ~d), (7*j) % 16, [6, 10, 15, 21][j % 4]

            temp = (a + f + X[k] + T[j]) & 0xFFFFFFFF
            a, b, c, d = d, (left_rotate(temp, s) + b) & 0xFFFFFFFF, b, c

        A, B, C, D = (A + a) & 0xFFFFFFFF, (B + b) & 0xFFFFFFFF, (C + c) & 0xFFFFFFFF, (D + d) & 0xFFFFFFFF

    return f'{A:08x}{B:08x}{C:08x}{D:08x}'

user_input = input("Enter text to hash: ")
print("MD5 Hash:", md5(user_input))
