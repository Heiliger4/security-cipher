def reverse_text(text):
    return text[::-1]

def simple_transposition(text, key, encrypt=True):
    # Ensure that the key is at least 1
    if key < 1:
        raise ValueError("Key must be greater than 0")
    
    result = []
    length = len(text)

    if encrypt:
        # Encryption: Rearrange the characters in chunks of size 'key'
        for i in range(0, length, key):
            result.append(text[i:i + key][::-1])  # Reverse the characters in the chunk
        return ''.join(result)
    else:
        # Decryption: Reverse the encryption logic, reversing each chunk again
        # We need to ensure we correctly reconstruct the original order
        result = []
        for i in range(0, length, key):
            result.append(text[i:i + key][::-1])  # Reverse each chunk back
        return ''.join(result)

def rail_fence_cipher(text, key, encrypt=True):
    if key == 1:
        return text
    if encrypt:
        fence = [''] * key
        row = 0
        going_down = False

        for char in text:
            fence[row] += char
            if row == 0 or row == key - 1:
                going_down = not going_down
            row += 1 if going_down else -1
        return ''.join(fence)
    else:
        fence = [''] * key
        row = 0
        going_down = False
        index = 0
        for i in range(len(text)):
            fence[row] += text[i]
            if row == 0 or row == key - 1:
                going_down = not going_down
            row += 1 if going_down else -1

        result = [''] * len(text)
        current_pos = 0
        for i in range(key):
            for char in fence[i]:
                result[current_pos] = char
                current_pos += 1
        return ''.join(result)
