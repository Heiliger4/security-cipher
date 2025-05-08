def simple_caesar_cipher(text, shift, encrypt=True):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26 + 97))
            result.append(new_char.upper() if char.isupper() else new_char)
        else:
            result.append(char)
    return ''.join(result)

def atbash_cipher(text, _=None, encrypt=True):
    result = []
    for char in text:
        if char.isupper():
            result.append(chr(90 - (ord(char) - 65)))
        elif char.islower():
            result.append(chr(122 - (ord(char) - 97)))
        else:
            result.append(char)
    return ''.join(result)

def xor_cipher(text, key, encrypt=True):
    return ''.join(chr(ord(c) ^ key) for c in text)