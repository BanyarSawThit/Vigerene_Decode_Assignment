import matplotlib.pyplot as plt
import numpy as np
import string

# Define the English letter frequency distribution
english_freq = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
    'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
    'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
    'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074
}

# Create lists for letters and their corresponding frequencies
letters = list(string.ascii_uppercase)
freq_values = [english_freq[letter] for letter in letters]

# Create a bar chart
x = np.arange(len(letters))
plt.figure()
plt.bar(x, freq_values)
plt.xticks(x, letters)
plt.title('English Letter Frequency Distribution')
plt.show()
