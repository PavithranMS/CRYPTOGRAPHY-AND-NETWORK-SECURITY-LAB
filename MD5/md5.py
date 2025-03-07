import math

T = [int(4294967296 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]
s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

def F(x, y, z): return (x & y) | (~x & z)
def G(x, y, z): return (x & z) | (y & ~z)
def H(x, y, z): return x ^ y ^ z
def I(x, y, z): return y ^ (x | ~z)

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5(message):
    original_length = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message += b'\x80'
    while (len(message) % 64) != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, byteorder='little')

    A, B, C, D = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476

    for chunk_index in range(0, len(message), 64):
        chunk = message[chunk_index:chunk_index + 64]
        M = [int.from_bytes(chunk[i:i + 4], byteorder='little') for i in range(0, 64, 4)]

        a, b, c, d = A, B, C, D

        for i in range(64):
            if 0 <= i <= 15:
                f = F(b, c, d)
                g = i
            elif 16 <= i <= 31:
                f = G(b, c, d)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = H(b, c, d)
                g = (3 * i + 5) % 16
            else:
                f = I(b, c, d)
                g = (7 * i) % 16

            temp = (a + f + M[g] + T[i]) & 0xFFFFFFFF
            new_b = (b + left_rotate(temp, s[i])) & 0xFFFFFFFF

            a, b, c, d = d, new_b, b, c

            print(f"Step {i + 1}: A = {a:#x}, B = {b:#x}, C = {c:#x}, D = {d:#x}")

        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(A, B, C, D)

user_message = input("Enter a message to hash: ").encode('utf-8')
hash_result = md5(user_message)
print("MD5 Hash:", hash_result)
