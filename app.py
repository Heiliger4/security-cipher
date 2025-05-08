from flask import Flask, render_template, request
from ciphers import simple_caesar_cipher, atbash_cipher, xor_cipher, reverse_text, simple_transposition, rail_fence_cipher

app = Flask(__name__)

# Define the available ciphers
substitution_ciphers = {
    "caesar": "Caesar Cipher",
    "atbash": "Atbash Cipher",  # Changed from substitution to atbash
    "xor": "XOR Cipher"
}

transposition_ciphers = {
    "reverse_text": "Reverse Text",
    "simple_transposition": "Simple Transposition",
    "rail_fence": "Rail Fence Cipher"
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
    substitution_method = request.form["substitution"]
    transposition_method = request.form["transposition"]
    key1 = request.form.get("key1", "")  # Substitution key
    key2 = request.form.get("key2", "")  # Transposition key

    # Process the text
    processed_text = text
    
    try:
        if action == "encrypt":
            # Apply substitution cipher
            if substitution_method == "caesar":
                processed_text = simple_caesar_cipher(processed_text, int(key1 or 3))
            elif substitution_method == "atbash":  # Changed from substitution to atbash
                processed_text = atbash_cipher(processed_text, key1)
            elif substitution_method == "xor":
                processed_text = xor_cipher(processed_text, int(key1 or 42))

            # Apply transposition cipher
            if transposition_method == "reverse_text":
                processed_text = reverse_text(processed_text)
            elif transposition_method == "simple_transposition":
                processed_text = simple_transposition(processed_text, int(key2 or 3))
            elif transposition_method == "rail_fence":
                processed_text = rail_fence_cipher(processed_text, int(key2 or 3))
        else:
            # Apply reverse transposition cipher first
            if transposition_method == "reverse_text":
                processed_text = reverse_text(processed_text)
            elif transposition_method == "simple_transposition":
                processed_text = simple_transposition(processed_text, int(key2 or 3), encrypt=False)
            elif transposition_method == "rail_fence":
                processed_text = rail_fence_cipher(processed_text, int(key2 or 3), encrypt=False)
            
            # Apply reverse substitution cipher
            if substitution_method == "caesar":
                processed_text = simple_caesar_cipher(processed_text, int(key1 or 3), encrypt=False)
            elif substitution_method == "atbash":  # Atbash is its own inverse
                processed_text = atbash_cipher(processed_text, key1, encrypt=False)
            elif substitution_method == "xor":
                processed_text = xor_cipher(processed_text, int(key1 or 42))
    except Exception as e:
        processed_text = f"Error during processing: {e}"

    return render_template(
        "result.html", 
        action=action, 
        original_text=text, 
        processed_text=processed_text,
        substitution_name=substitution_ciphers.get(substitution_method, "Unknown"),
        transposition_name=transposition_ciphers.get(transposition_method, "Unknown")
    )

if __name__ == "__main__":
    app.run(debug=True)