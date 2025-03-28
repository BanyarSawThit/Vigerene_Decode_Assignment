from collections import Counter
import string

# English letter frequency
english_freq = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
    'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
    'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
    'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074
}


def chi_squared_stat(observed_freq, expected_freq, group_len):
    """Calculate chi-squared statistic for a given frequency distribution."""
    return sum(
        ((observed_freq.get(c, 0) / group_len - expected_freq[c]) ** 2) / expected_freq[c]
        for c in string.ascii_uppercase
    )


def guess_caesar_key_letter_verbose(group):
    """
    For a given group of characters, try all 26 Caesar shifts and print a detailed
    report including chi-squared scores and shifted frequency distributions.
    Returns the key letter corresponding to the shift with the lowest chi-squared statistic.
    """
    group_len = len(group)
    group_freq = Counter(group)
    chi_scores = []

    print(f"\nAnalyzing group (first 50 chars): {group[:50]}... (Total length: {group_len})")

    for shift in range(26):
        shifted_freq = {}
        # Prepare a textual representation of the frequency distribution for this shift
        distribution_str = []
        for c in string.ascii_uppercase:
            # Calculate the letter in the group that would be shifted to letter c by this shift.
            shifted_c = chr((ord(c) - shift - 65) % 26 + 65)
            count = group_freq.get(shifted_c, 0)
            shifted_freq[c] = count
            distribution_str.append(f"{c}:{count}")
        chi = chi_squared_stat(shifted_freq, english_freq, group_len)
        chi_scores.append((chi, shift))
        # Print out the shift's results in a single line.
        print(f"Shift {shift:2d}: Chi-Squared = {chi:8.2f} | ")

    best_shift = min(chi_scores)[1]
    key_letter = chr((26 - best_shift) % 26 + ord('A'))
    print(f"--> Best shift: {best_shift} leads to key letter: {key_letter}\n")
    return key_letter


# Insert groups here
g0 = 'KVAIIWETNVQABVBKMVQVZDBUVTPGQUQVVIBWPTZWIMQIBQVBQLQEBTQIMZTJTVPQAZGVBNBBZPLJLVQMIMMZG'
g1 = 'UQNAAEARVBTGVGJRAJAPTRHNBQGBFVAUQAVYJLVEASBAVAIUBIABUVAEEYFLGPRARQBRQRUUYPGHRGBZFXFYB'
g2 = 'VWIVYWAOMICCXCZIVVDTCHMBACAMHGVDHDJDVVIWVJIYJQVZIZXMOOBDBDJKMGFBLZPQZXMDDJJOQJIZJZDTA'
g3 = 'VIEZMISMWWXISIRXZWXPWIIMXMVOEIZWERRRWTKYHVWMRSVVVRPOLEAMLJQIEYMEYVRIIXSWRRGIIJEQRCRLJ'
g4 = 'YEZVAFEAGGNNPRGHVFFVNAQAUFBGEFVGQGNQAVNGINNAUYVNRGHVREBYFRNETQQARBTACRHPQGBGYNAORSGVY'
g5 = 'XZXTOMVZLHVMXTBKTMBGVMMTXYFHDMTHXXEUHHOTHOYGXOHOENWGNRKBEPKLXBGWGYLMEWZTUBGHHOWXHBALB'
g6 = 'APZBMSWBWXZTIZMGBQVLPKPBETVXMWBZPZPMBVQTKQMWEMCQIZQOALTVIISWLVIABPWBGPPZMVBBXQQZNOMBO'
g7 = 'ZKWCBBAVZTCOBZHKWZTPWOSWCWSORBWMWBSFCSOGOOHJORGOHSBKAIRRHGSBMUDIAWBVOWCSFIFVAOGSHISCV'
g8 = 'VNPEGBCRBYFAVLUUBYNRRCVBETJENRBNZNETARGBGGLNFVBGRFTVVEJORNQNVGCOHFNNSZHRTRVRRGEQUENEG'

groups = [g0, g1, g2, g3, g4, g5, g6, g7, g8]

# === Guess the full keyword from the groups with detailed visualization ===
keyword = ""
for i, group in enumerate(groups):
    key_letter = guess_caesar_key_letter_verbose(group)
    print(f"Key[{i + 1}]: {key_letter}")
    keyword += key_letter

print("\nGuessed Keyword:", keyword)
