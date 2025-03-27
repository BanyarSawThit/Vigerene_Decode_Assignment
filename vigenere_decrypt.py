def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)

    for i, c in enumerate(ciphertext):
        if c.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            decrypted = chr((ord(c) - shift - 65) % 26 + 65)
            plaintext += decrypted
        else:
            plaintext += c  # keep non-letters as is

    return plaintext

# === Load your cleaned ciphertext
with open("input/cipher_8.txt", "r") as f:
    ciphertext = f.read().replace(" ", "").replace("\n", "").upper()

# === Try known keyword
key = "invention"
plaintext = vigenere_decrypt(ciphertext, key)

# === Print the first 500 characters of decrypted text
print(plaintext[:500])
