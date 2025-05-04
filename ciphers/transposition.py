# transposition.py

def reverse_text(text):
    return text[::-1]

def columnar_transposition(text, key, encrypt=True):
    key = int(key)
    if encrypt:
        grid = [''] * key
        for i in range(len(text)):
            grid[i % key] += text[i]
        return ''.join(grid)
    else:
        num_rows = len(text) // key
        extra = len(text) % key
        columns = []
        start = 0
        for i in range(key):
            length = num_rows + 1 if i < extra else num_rows
            columns.append(text[start:start+length])
            start += length
        result = ''
        for i in range(num_rows + 1):
            for col in columns:
                if i < len(col):
                    result += col[i]
        return result

def rail_fence_cipher(text, key, encrypt=True):
    key = int(key)
    if key <= 1:
        return text
    if encrypt:
        rail = ['' for _ in range(key)]
        row, step = 0, 1
        for char in text:
            rail[row] += char
            if row == 0:
                step = 1
            elif row == key - 1:
                step = -1
            row += step
        return ''.join(rail)
    else:
        pattern = list(range(key)) + list(range(key-2, 0, -1))
        pattern = (pattern * ((len(text) // len(pattern)) + 1))[:len(text)]
        indexes = sorted(range(len(pattern)), key=lambda i: pattern[i])
        result = [''] * len(text)
        for i, idx in enumerate(indexes):
            result[idx] = text[i]
        return ''.join(result)
