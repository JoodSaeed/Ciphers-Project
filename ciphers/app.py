# import needed libraries from flask
#Flask is the main library to run the app
# request because we will get the text and key from the user interface to the server
# render_template to use a seprate html file fill with data from the app
from flask import Flask, request, render_template
# import texts from data.py to use it in the template
from ciphers import cipher, texts

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if the request method is a POST request
    if request.method == 'POST':
        # Get the plaintext, key, type of cipher, and mode (encrypt/decrypt) from the form
        text = request.form['plaintext']
        key_ceaser = request.form['key_ceaser'] 
        key_vigenere = request.form['key_vigenere']
        key_rail_fence = request.form['key_rail_fence']
        key_autokey = request.form['key_autokey']
        key_playfair = request.form['key_playfair']
        key_beaufort = request.form['key_beaufort']
        type = request.form['type']
        mode = request.form['mode']

        # If the selected cipher is Vigenere Cipher
        if type == "vigenere_cipher":
            result = cipher.vigenere(text, key_vigenere, mode)

        # If the selected cipher is Caesar Cipher
        elif type == "ceaser_cipher":
            # Convert the key from string to integer
            key = int(key_ceaser)
            result = cipher.ceaser(text, key, mode)

        # If the selected   cipher is Rail Fence Cipher
        elif type == "rail_fence_cipher":
            # Convert the key from string to integer
            key = int(key_rail_fence)
            result = cipher.rail_fence(text, key, mode)

        # If the selected cipher is Autokey Cipher
        elif type == "autokey_cipher":
            result = cipher.autokey(text, key_autokey, mode)

        elif type == "playfair_cipher":
            result = cipher.playfair(text, key_playfair, mode)

        elif type == "beaufort_cipher":
            result = cipher.beaufort(text, key_beaufort)
         
        # Write the result to a file named "file.txt" in the "static" folder
        with open("static/file.txt", "w") as f:
            f.write(result)
        # Render the "index.html" template and pass the result to the template
        return render_template('index.html', texts = texts, result=result)
    # If the request method is not POST, render the "index.html" template without passing any result
    return render_template('index.html', texts = texts)
# If the script is being run directly, run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
