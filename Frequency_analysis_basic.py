from collections import Counter
import matplotlib.pyplot as plt
import string

# === Step 0: Load and clean ciphertext ===
with open("input/cipher_8.txt", "r") as f:
    ciphertext = f.read().replace(" ", "").replace("\n", "").upper()

key_length = 9
groups = [""] * key_length

# === Step 1: Split into Caesar columns ===
for i, char in enumerate(ciphertext):
    groups[i % key_length] += char

# === Print shifted rows for visualization ===
print("\nShifted Cipher Rows for Key Length = " + str(key_length))
row_preview_len = 100

for row in range(key_length):
    print(f"Group {row + 1} (key[{row}]):")
    print(groups[row][:row_preview_len])  # print first 100 characters of that column
    print()

# === Step 2: Frequency Analysis for each group ===
for i, group in enumerate(groups):
    freq = Counter(group)
    total = sum(freq.values())
    print(f" Frequency Table for Group {i+1} (Key[{i}])")
    print("-" * 30)
    for letter, count in freq.most_common():
        percentage = round((count / total) * 100, 2)
        print(f"{letter}: {count} ({percentage}%)")
    print()

# === Step 3: Frequency Distribution Diagram ===
for i, group in enumerate(groups):
    freq = Counter(group)
    # Create lists for all letters A-Z, using 0 if the letter is missing
    letters = list(string.ascii_uppercase)
    counts = [freq.get(letter, 0) for letter in letters]

    plt.figure()
    plt.bar(letters, counts)
    plt.title(f"Letter Frequency in Column {i + 1}")
    plt.show()

# === Step 4: Guess the Caesar Shift
# For the purpose of an initial test, we assume 'E' is the most frequent letter in English.
most_frequent_letter = ['E']
# list of observed most frequent letter per group
encrypted_letters = ['V', 'A', 'V', 'I', 'G', 'H', 'B', 'O', 'N']

# Guess the shift for each group based on the assumption
for i in range(key_length):
    shift = (ord(encrypted_letters[i]) - ord(most_frequent_letter[0])) % 26
    key_letter = chr((26 - shift) % 26 + ord('A'))
    print(f"Key letter for Group {i+1}: {key_letter}")















# # keyword - 1 [test]
# shift = (ord(encrypted_letters[0]) - ord(most_frequent_letter[0])) % 26
# key_letter = chr((26 - shift) % 26 + ord('A'))
# print(key_letter)