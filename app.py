from flask import Flask, render_template, request
from ciphers import (
    simple_caesar_cipher, 
    atbash_cipher, 
    xor_cipher,
    reverse_text,
    simple_transposition,
    columnar_transposition
)

app = Flask(__name__)

substitution_ciphers = {
    "caesar": "Caesar Cipher",
    "atbash": "Atbash Cipher",  # Replaced substitution
    "xor": "XOR Cipher"
}

transposition_ciphers = {
    "reverse_text": "Reverse Text",
    "simple_transposition": "Simple Transposition",
    "columnar": "Columnar Transposition"  # Replaced rail fence
}

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html",
        substitution=substitution_ciphers,
        transposition=transposition_ciphers
    )

@app.route("/process", methods=["POST"])
def process():
    text = request.form["text"]
    action = request.form["action"]
    sub_method = request.form["substitution"]
    trans_method = request.form["transposition"]
    key1 = request.form.get("key1", "")
    key2 = request.form.get("key2", "")

    processed_text = text
    
    try:
        # Substitution ciphers
        if sub_method == "caesar":
            processed_text = simple_caesar_cipher(processed_text, int(key1 or 3), action == "encrypt")
        elif sub_method == "atbash":
            processed_text = atbash_cipher(processed_text)
        elif sub_method == "xor":
            processed_text = xor_cipher(processed_text, int(key1 or 42))

        # Transposition ciphers
        if trans_method == "reverse_text":
            processed_text = reverse_text(processed_text)
        elif trans_method == "simple_transposition":
            processed_text = simple_transposition(processed_text, int(key2 or 3), action == "encrypt")
        elif trans_method == "columnar":
            processed_text = columnar_transposition(processed_text, int(key2 or 3), action == "encrypt")

    except Exception as e:
        processed_text = f"Error: {str(e)}"

    return render_template(
        "result.html",
        action=action,
        original_text=text,
        processed_text=processed_text,
        substitution_name=substitution_ciphers.get(sub_method, "Unknown"),
        transposition_name=transposition_ciphers.get(trans_method, "Unknown")
    )

if __name__ == "__main__":
    app.run(debug=True)