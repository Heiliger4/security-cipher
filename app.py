from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Substitution ciphers (to be implemented)
SUBSTITUTION_CIPHERS = {
    'caesar': 'Caesar Cipher',
    'atbash': 'Atbash Cipher',
    'keyword': 'Keyword Substitution'
}

# Transposition ciphers (to be implemented)
TRANSPOSITION_CIPHERS = {
    'rail_fence': 'Rail Fence Cipher',
    'columnar': 'Columnar Transposition',
    'route': 'Route Cipher'
}

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
    key2 = request.form.get('key2', '')
    
    # Process the text with selected ciphers (to be implemented)
    # For now, just pass through the original text
    processed_text = f"Processed ({action}): {text}"
    
    return render_template('result.html', 
                         original_text=text,
                         processed_text=processed_text,
                         action=action)

if __name__ == '__main__':
    app.run(debug=True)