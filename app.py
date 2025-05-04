from flask import Flask, render_template, request
from ciphers import simple_caesar_cipher, simple_substitution_cipher, xor_cipher, reverse_text, columnar_transposition, rail_fence_cipher

app = Flask(__name__)

# Define the available ciphers
substitution = {
    "caesar": "Caesar Cipher",
    "substitution": "Substitution Cipher",
    "xor": "XOR Cipher"
}

transposition = {
    "reverse_text": "Reverse Text",
    "columnar": "Columnar Transposition",
    "rail_fence": "Rail Fence Cipher"
}

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", substitution=substitution, transposition=transposition)

@app.route("/process", methods=["POST"])
def process():
    text = request.form["text"]
    action = request.form["action"]
    substitution_method = request.form["substitution"]
    transposition_method = request.form["transposition"]
    key1 = request.form.get("key1", "")  # Substitution key
    key2 = request.form.get("key2", "")  # Transposition key

    # Encrypt or decrypt based on action
    if action == "encrypt":
        processed_text = encrypt(text, substitution_method, transposition_method, key1, key2)
    else:
        processed_text = decrypt(text, substitution_method, transposition_method, key1, key2)

    # Render the result page with original and processed text
    return render_template(
        "result.html", 
        action=action, 
        original_text=text, 
        processed_text=processed_text
    )

def encrypt(text, substitution_method, transposition_method, key1, key2):
    # Apply substitution cipher
    if substitution_method == "caesar" and key1:
        text = simple_caesar_cipher(text, int(key1))
    elif substitution_method == "substitution":
        text = simple_substitution_cipher(text, key1)
    elif substitution_method == "xor" and key1:
        text = xor_cipher(text, int(key1))

    # Apply transposition cipher
    if transposition_method == "reverse_text":
        text = reverse_text(text)
    elif transposition_method == "columnar" and key2:
        text = columnar_transposition(text, int(key2))
    elif transposition_method == "rail_fence" and key2:
        text = rail_fence_cipher(text, int(key2))

    return text

def decrypt(text, substitution_method, transposition_method, key1, key2):
    # Apply reverse transposition cipher
    if transposition_method == "reverse_text":
        text = reverse_text(text)
    elif transposition_method == "columnar" and key2:
        text = columnar_transposition(text, int(key2), encrypt=False)
    elif transposition_method == "rail_fence" and key2:
        text = rail_fence_cipher(text, int(key2), encrypt=False)

    # Apply reverse substitution cipher
    if substitution_method == "caesar" and key1:
        text = simple_caesar_cipher(text, int(key1), encrypt=False)
    elif substitution_method == "substitution":
        text = simple_substitution_cipher(text, key1, encrypt=False)
    elif substitution_method == "xor" and key1:
        text = xor_cipher(text, int(key1))

    return text

if __name__ == "__main__":
    app.run(debug=True)
