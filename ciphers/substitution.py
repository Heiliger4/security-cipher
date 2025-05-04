# substitution.py

def simple_caesar_cipher(text, key, encrypt=True):
    shift = int(key)
    result = []
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            offset = shift if encrypt else -shift
            result.append(chr((ord(char) - base + offset) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def simple_substitution_cipher(text, substitution_map, encrypt=True):
    result = []
    for char in text:
        if char.isalpha():
            result.append(substitution_map.get(char.lower(), char))  # Using lowercase for uniformity
        else:
            result.append(char)
    return ''.join(result)

def xor_cipher(text, key):
    key = int(key)
    return ''.join([chr(ord(c) ^ key) for c in text])
