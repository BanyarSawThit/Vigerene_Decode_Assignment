from collections import Counter
import string

# English letter frequency (relative to 1)
english_freq = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
    'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
    'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
    'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074
}

def chi_squared_stat(observed_freq, expected_freq, group_len):
    return sum(
        ((observed_freq.get(c, 0)/group_len - expected_freq[c]) ** 2) / expected_freq[c]
        for c in string.ascii_uppercase
    )

def guess_caesar_key_letter(group):
    group_len = len(group)
    group_freq = Counter(group)

    # Try all 26 Caesar shifts
    chi_scores = []
    for shift in range(26):
        shifted_freq = {}
        for c in string.ascii_uppercase:
            shifted_c = chr((ord(c) - shift - 65) % 26 + 65)
            shifted_freq[c] = group_freq.get(shifted_c, 0)
        chi = chi_squared_stat(shifted_freq, english_freq, group_len)
        chi_scores.append((chi, shift))

    # Get best shift (lowest chi-square)
    best_shift = min(chi_scores)[1]
    key_letter = chr((26 - best_shift) % 26 + ord('A'))
    return key_letter
g1 = 'KVAIIWETNVQABVBKMVQVZDBUVTPGQUQVVIBWPTZWIMQIBQVBQLQEBTQIMZTJTVPQAZGVBNBBZPLJLVQMIMMZG'
g2 = 'UQNAAEARVBTGVGJRAJAPTRHNBQGBFVAUQAVYJLVEASBAVAIUBIABUVAEEYFLGPRARQBRQRUUYPGHRGBZFXFYB'
g3 = 'VWIVYWAOMICCXCZIVVDTCHMBACAMHGVDHDJDVVIWVJIYJQVZIZXMOOBDBDJKMGFBLZPQZXMDDJJOQJIZJZDTA'
g4 = 'VIEZMISMWWXISIRXZWXPWIIMXMVOEIZWERRRWTKYHVWMRSVVVRPOLEAMLJQIEYMEYVRIIXSWRRGIIJEQRCRLJ'
g5 = 'YEZVAFEAGGNNPRGHVFFVNAQAUFBGEFVGQGNQAVNGINNAUYVNRGHVREBYFRNETQQARBTACRHPQGBGYNAORSGVY'
g6 = 'XZXTOMVZLHVMXTBKTMBGVMMTXYFHDMTHXXEUHHOTHOYGXOHOENWGNRKBEPKLXBGWGYLMEWZTUBGHHOWXHBALB'
g7 = 'APZBMSWBWXZTIZMGBQVLPKPBETVXMWBZPZPMBVQTKQMWEMCQIZQOALTVIISWLVIABPWBGPPZMVBBXQQZNOMBO'
g8 = 'ZKWCBBAVZTCOBZHKWZTPWOSWCWSORBWMWBSFCSOGOOHJORGOHSBKAIRRHGSBMUDIAWBVOWCSFIFVAOGSHISCV'
g9 = 'VNPEGBCRBYFAVLUUBYNRRCVBETJENRBNZNETARGBGGLNFVBGRFTVVEJORNQNVGCOHFNNSZHRTRVRRGEQUENEG'

groups = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
# === Guess the full keyword from 9 groups ===
keyword = ""
for i, group in enumerate(groups):
    key_letter = guess_caesar_key_letter(group)
    print(f"Key[{i+1}]: {key_letter}")
    keyword += key_letter

print("\nGuessed Keyword:", keyword)
