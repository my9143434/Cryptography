
def rsa_encrypt(plaintext):

    e = 69
    n = 781

    aes_key = str(plaintext)

    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** e) % n for char in aes_key]

    print(cipher)
    # Return the array of bytes
    return cipher


def rsa_decrypt(encrypted_text):

    d = 629
    n = 781

    print("before decrypting:", encrypted_text)
    print(type(encrypted_text))

    plain = [chr((char ** d) % n) for char in encrypted_text]

    decrypted_text = ''.join(plain)
    print(decrypted_text)
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    cipher_text = rsa_encrypt("test")
    rsa_decrypt(cipher_text)

