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
    substitution_map = substitution_map or "zyxwvutsrqponmlkjihgfedcba"  # Default reverse alphabet
    sub_map = {chr(i+97): substitution_map[i].lower() for i in range(26)}
    
    if not encrypt:
        # Create reverse mapping for decryption
        sub_map = {v: k for k, v in sub_map.items()}
    
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in sub_map:
                new_char = sub_map[lower_char]
                result.append(new_char.upper() if char.isupper() else new_char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)

def xor_cipher(text, key, encrypt=True):
    key = int(key)
    return ''.join([chr(ord(c) ^ key) for c in text])