def left_rotate(value, shift, size=32):
    return ((value << shift) | (value >> (size - shift))) & 0xFFFFFFFF

def sha1(message):
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'

    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    message += original_bit_len.to_bytes(8, 'big')

    h0, h1, h2, h3, h4 = (
        0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
    )

    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        w = [int.from_bytes(chunk[j:j+4], 'big') for j in range(0, 64, 4)]

        for j in range(16, 80):
            w.append(left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if 0 <= j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e, d, c, b, a = d, c, left_rotate(b, 30), a, temp

            print(f"Round {j+1}: A={a:08x} B={b:08x} C={c:08x} D={d:08x} E={e:08x}")

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return f'{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}'

input_string = input("Enter text to hash with SHA-1: ")
sha1_result = sha1(input_string.encode())

print(f"\nFinal SHA-1 Hash: {sha1_result}")
