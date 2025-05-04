# transposition.py

def reverse_text(text):
    return text[::-1]

def columnar_transposition(text, key, encrypt=True):
    key = int(key)
    if key <= 0:
        return text
        
    if encrypt:
        # Pad the text if needed
        padding = (-len(text)) % key
        if padding:
            text += ' ' * padding
            
        num_columns = key
        num_rows = (len(text) + num_columns - 1) // num_columns
        
        # Write by rows, read by columns
        grid = [text[i*num_columns:(i+1)*num_columns] for i in range(num_rows)]
        encrypted = ''.join([''.join([grid[row][col] for row in range(num_rows)]) 
                          for col in range(num_columns)])
        return encrypted
    else:
        num_columns = key
        num_rows = (len(text) + num_columns - 1) // num_columns
        
        # Reconstruct the grid
        grid = []
        for row in range(num_rows):
            start = row * num_columns
            end = (row + 1) * num_columns
            grid.append(text[start:end])
            
        # Read by rows
        decrypted = ''.join([''.join([grid[row][col] for col in range(num_columns)]) 
                          for row in range(num_rows)])
        return decrypted.strip()

def rail_fence_cipher(text, key, encrypt=True):
    key = int(key)
    if key <= 1:
        return text
        
    if encrypt:
        rails = [[] for _ in range(key)]
        rail = 0
        direction = 1
        
        for char in text:
            rails[rail].append(char)
            rail += direction
            if rail == 0 or rail == key - 1:
                direction *= -1
                
        return ''.join([''.join(rail) for rail in rails])
    else:
        # Calculate the pattern
        pattern = []
        rail = 0
        direction = 1
        for _ in range(len(text)):
            pattern.append(rail)
            rail += direction
            if rail == 0 or rail == key - 1:
                direction *= -1
                
        # Reconstruct rails
        rail_lengths = [pattern.count(i) for i in range(key)]
        rails = []
        pos = 0
        for length in rail_lengths:
            rails.append(text[pos:pos+length])
            pos += length
            
        # Read following the pattern
        result = []
        rail_positions = [0] * key
        for rail_num in pattern:
            result.append(rails[rail_num][rail_positions[rail_num]])
            rail_positions[rail_num] += 1
            
        return ''.join(result)