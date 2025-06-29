import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# ENCRYPT
plain_text = input("Enter your message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("Encrypted message:", cipher_text)

# DECRYPT
cipher_text = input("Enter your message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print("Decrypted message:", plain_text)
