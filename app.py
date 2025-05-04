from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

SUBSTITUTION_CIPHERS = {
    'caesar': 'Caesar Cipher',
    'reverse': 'Reverse Alphabet Cipher',
    'modular': 'Modular Arithmetic Cipher'
}

TRANSPOSITION_CIPHERS = {
    'rail_fence': 'Rail Fence Cipher',
    'columnar': 'Columnar Transposition',
    'route': 'Route Cipher'
}

def caesar_cipher(text, shift, encrypt=True):
    result = []
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            offset = shift if encrypt else -shift
            result.append(chr((ord(char) - base + offset) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def reverse_cipher(text):
    result = []
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result.append(chr(155 - ord(char)) if char.isupper() else chr(219 - ord(char)))
        else:
            result.append(char)
    return ''.join(result)

def modular_cipher(text, encrypt=True):
    result = []
    for idx, char in enumerate(text):
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shift = idx + 1 if encrypt else -(idx + 1)
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

@app.route('/')
def index():
    return render_template('index.html', 
                         substitution_ciphers=SUBSTITUTION_CIPHERS,
                         transposition_ciphers=TRANSPOSITION_CIPHERS)

@app.route('/process', methods=['POST'])
def process():
    action = request.form.get('action')
    text = request.form.get('text')
    substitution = request.form.get('substitution')
    transposition = request.form.get('transposition')
    key1 = request.form.get('key1', '')

    try:
        key1 = int(key1) if key1 else 3
    except ValueError:
        key1 = 3

    processed_text = text

    if substitution == 'caesar':
        processed_text = caesar_cipher(text, key1, encrypt=(action == 'encrypt'))
    elif substitution == 'reverse':
        processed_text = reverse_cipher(text)
    elif substitution == 'modular':
        processed_text = modular_cipher(text, encrypt=(action == 'encrypt'))

    return render_template('result.html', 
                         original_text=text,
                         processed_text=processed_text,
                         action=action)

if __name__ == '__main__':
    app.run(debug=True)
