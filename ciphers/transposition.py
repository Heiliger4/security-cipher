def reverse_text(text):
    """Ultra-simple reversal"""
    return text[::-1]

def simple_transposition(text, key, encrypt=True):
    """Columnar transposition (simplest practical transposition)"""
    if key < 1:
        key = 1  # Default to 1 if invalid
    
    if encrypt:
        # Pad text if needed
        pad_length = (key - len(text) % key) % key
        padded = text + (' ' * pad_length)
        # Write in rows, read by columns
        return ''.join(padded[i::key] for i in range(key))
    else:
        # Calculate original rows
        rows = (len(text) + key - 1) // key
        # Rebuild by reading columns
        return ''.join(text[i::rows] for i in range(rows)).strip()

def columnar_transposition(text, key, encrypt=True):
    """Even simpler version (single method for both operations)"""
    if not encrypt:
        rows = -(-len(text) // key)  # Ceiling division
        return columnar_transposition(text, rows, True)
    return ''.join(text[i::key] for i in range(key))