def reverse_text(text, _=None, encrypt=True):
    return text[::-1]

def simple_transposition(text, key, encrypt=True):
    if key < 1:
        key = 1
    
    if encrypt:
        # Pad with spaces if needed (preserve length)
        pad_length = (key - len(text) % key) % key
        padded = text + (' ' * pad_length)
        return ''.join(padded[i::key] for i in range(key))
    else:
        # Calculate original rows
        rows = -(-len(text) // key)  # Ceiling division
        # Rebuild by reading columns
        return ''.join(text[i::rows] for i in range(rows)).rstrip()

def columnar_transposition(text, key, encrypt=True):
    if key < 1:
        key = 1
    
    if not encrypt:
        # For decryption, swap rows and columns
        rows = -(-len(text) // key)  # Ceiling division
        return columnar_transposition(text, rows, True)
    
    # Pad with spaces if needed
    pad_length = (key - len(text) % key) % key
    padded = text + (' ' * pad_length)
    return ''.join(padded[i::key] for i in range(key))