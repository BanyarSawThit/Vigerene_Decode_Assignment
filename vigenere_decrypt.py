def vigenere_decrypt(ciphertext, key):
    """
    Decrypts the provided ciphertext using the Vigenère cipher algorithm
    and the given key.

    :param ciphertext: A string representing the encrypted text (A-Z only).
    :param key: A string representing the decryption key (assumes A-Z only).
    :return: A string of the decrypted plaintext (A-Z).
    """

    plaintext = "" # This will hold the decrypted plaintext as it's built.
    key = key.upper() # Convert the key to uppercase for consistent ASCII calculations.
    key_length = len(key) # Store the length of the key to use for modular arithmetic.

    # Loop over each character in the ciphertext, using enumerate to get index (i) + char
    for i, char in enumerate(ciphertext):
        # Determine how much to shift for this position based on the key.
        # 'key[i % key_length]' cycles through key letters in a wrap-around manner
        # ord('A') is 65, so subtracting it gives us a 0-25 offset.
        shift = ord(key[i % key_length]) - ord('A')
        # print(char, end=" - ")
        # print(chr(ord(key[i % key_length])), end=" ")
        # print("(shift", shift, ")", end=' -> ')

        # Decrypt the character:
        # 1) Convert char to 0-25 by subtracting 65 (ord('A')).
        # 2) Subtract the shift to "reverse" the encryption.
        # 3) Use % 26 to ensure the result remains in [0..25].
        # 4) Convert back to ASCII by adding 65 again.
        decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
        # print(decrypted_char, "( index ", (ord(char) - shift - 65)%26,")")

        # Append the decrypted character to our plaintext string.
        plaintext += decrypted_char

    # Return the fully decrypted message.
    return plaintext


# === Load your cleaned ciphertext from file ===
print("Step 1: Load the cleaned ciphertext")
with open("input/cipher_8.txt", "r") as f:
    # Read the file, remove spaces and newlines, then convert to uppercase
    ciphertext = f.read().replace(" ", "").replace("\n", "").upper()
    print(ciphertext[:100])
    print()

# === Insert known keyword for decryption ===
key = "INVENTION"
plaintext = vigenere_decrypt(ciphertext, key)

# === Print the decrypted text ===
print(plaintext)
