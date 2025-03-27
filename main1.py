from collections import Counter
import matplotlib.pyplot as plt

# === Step 0: Load and clean ciphertext ===
with open("input/cipher_8.txt", "r") as f:
    ciphertext = f.read().replace(" ", "").replace("\n", "").upper()

key_length = 9
groups = [""] * key_length

# === Step 1: Split into Caesar columns ===
for i, char in enumerate(ciphertext):
    groups[i % key_length] += char
# print(groups)

# === Step 2: Print shifted rows for visualization ===
print("\nShifted Cipher Rows for Key Length = " + str(key_length))
row_preview_len = 1000  # limit row print to keep it short and readable

for row in range(key_length):
    print(f"Group {row + 1} (key[{row}]):")
    print(groups[row][:row_preview_len])  # print first 100 characters of that column
    print()

# === Step 3: Frequency Analysis ===
for i, group in enumerate(groups):
    freq = Counter(group)
    total = sum(freq.values())
    print(f" Frequency Table for Group {i+1} (Key[{i}])")
    print("-" * 30)
    for letter, count in freq.most_common():
        percentage = round((count / total) * 100, 2)
        print(f"{letter}: {count} ({percentage}%)")
    print()

# for i, group in enumerate(groups):
#     freq = Counter(group)
#     letters, counts = zip(*sorted(freq.items()))
#     plt.figure()
#     plt.bar(letters, counts)
#     plt.title(f"Letter Frequency in Column {i+1}")
#     plt.xlabel("Letter")
#     plt.ylabel("Count")
#     plt.show()

most_frequent_letter = 'R'
encrypted_letters = ['V', 'A', 'V', 'I', 'G', 'H', 'B', 'O', 'N']


# keyword - 1
shift = (ord(encrypted_letters[0]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)


# keyword - 2
shift = (ord(encrypted_letters[1]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)

# keyword - 3
shift = (ord(encrypted_letters[2]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)

# keyword - 4
shift = (ord(encrypted_letters[3]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)

# keyword - 5
shift = (ord(encrypted_letters[4]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)

# keyword - 6
shift = (ord(encrypted_letters[5]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)

# keyword - 7
shift = (ord(encrypted_letters[6]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)

# keyword - 8
shift = (ord(encrypted_letters[7]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)

# keyword - 9
shift = (ord(encrypted_letters[8]) - ord(most_frequent_letter)) % 26
key_letter = chr((26 - shift) % 26 + ord('A'))
print(key_letter)