import csv
from collections import defaultdict
from itertools import combinations
import pandas as pd

# === STEP 1: Load and clean the ciphertext ===
with open("input/cipher_8.txt", "r") as f:
    ciphertext = f.read().replace(" ", "").replace("\n", "").upper()
print("\nStep 1 Ciphertext Preview:")
print(ciphertext[:100])

# === Visual Analysis Example ===
print("\nStep 1.1 for explanation purpose:")
for i in range(0,20):
    if i < 10:
        print(str(i) + "-"*9, end="")
    else:
        print(str(i) + "-"*8, end="")
print()
for i in range(0, 20):
    for x in range(0, 10):
        print(x, end="")
print()
print(ciphertext[:200])

# === STEP 2: Find repeated trigrams and their positions ===
trigram_positions = defaultdict(list)

for i in range(len(ciphertext) - 2):
    trigram = ciphertext[i:i+3]
    trigram_positions[trigram].append(i)

# Keep only trigrams that occur more than once
repeated_trigrams = {k: v for k, v in trigram_positions.items() if len(v) > 1}

# Display first 10 repeated trigrams for verification:
print("\nStep 2 - Repeated Trigrams and Positions:")
for trigram in list(repeated_trigrams.keys())[:10]:
    print(f"{trigram}: Positions {repeated_trigrams[trigram]}")

# === STEP 3: Compute spacing and modulo values ===
output_rows = []
for trigram, positions in repeated_trigrams.items():
    for i, j in combinations(positions, 2):
        spacing = abs(j - i)
        row = {
            "Trigram": trigram,
            "Position 1": i,
            "Position 2": j,
            "Spacing": spacing
        }
        # checking mod 2 through mod 20
        for mod in range(2, 21):
            row[f"Mod {mod}"] = "0" if spacing % mod == 0 else ""
        output_rows.append(row)

# Preview first few rows:
df = pd.DataFrame(output_rows)
print("\nStep 3 - Preview of Spacing and Modulo Calculation:")
print(df.head())

# #=== STEP 4: Write to CSV for Excel ===
# with open("input/trigram_analysis.csv", "w", newline="") as csvfile:
#     fieldnames = ["Trigram", "Position 1", "Position 2", "Spacing"] + [f"Mod {i}" for i in range(2, 21)]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerows(output_rows)
#
# print("CSV file 'trigram_analysis.csv' created successfully!")