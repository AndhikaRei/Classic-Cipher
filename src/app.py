from flask import Flask, render_template, request, redirect, url_for
from Playfair import PlayfairCipher
from Vigenere import VigenereCipher, FullVigenereCipher, ExtendedVigenereCipher, AutoKeyVigenereCipher
from Utility import alphabets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# Generate random vigenere encrypt table for handling full vigenere.
randomEncipherTable = VigenereCipher.generateRandomVigenereTable()

"""
--------------------------------------------------------------
# Default Route
--------------------------------------------------------------
"""
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('vigenere'))


"""
--------------------------------------------------------------
# Route for Vigenere Cipher
--------------------------------------------------------------
"""
@app.route('/vigenere-cipher')
def vigenere():
    return render_template('pages/vigenere-cipher.html', encrypt=True)

@app.route('/vigenere-cipher/encrypt', methods=['POST', 'GET'])
def vigenereEncrypt():
    if request.method == 'POST':
        key = request.form['key']
        plaintext = request.form['plaintext']
        try:
            vigenere = VigenereCipher(key=key, plaintext=plaintext)
            vigenere.encrypt()
            return render_template('pages/vigenere-cipher.html', encrypt=True, 
                result_ciphertext = vigenere, form = request.form)            
        except (Exception) as e:
            return render_template('pages/vigenere-cipher.html', encrypt=True, error = e, 
                form = request.form)
    else:
        return render_template('pages/vigenere-cipher.html', encrypt=True)

@app.route('/vigenere-cipher/decrypt', methods=['POST', 'GET'])
def vigenereDecrypt():
    if request.method == 'POST':
        key = request.form['key']
        ciphertext = request.form['ciphertext']
        try:
            vigenere = VigenereCipher(key=key, ciphertext=ciphertext)
            vigenere.decrypt()
            return render_template('pages/vigenere-cipher.html', encrypt=False, 
                result_plaintext = vigenere, form = request.form)            
        except (Exception) as e:
            return render_template('pages/vigenere-cipher.html', encrypt=False, 
                error = e, form = request.form)
    else:
        return render_template('pages/vigenere-cipher.html', encrypt=False)


"""
--------------------------------------------------------------
# Route for Auto-key Vigenere Cipher
--------------------------------------------------------------
"""
@app.route('/auto-key-vigenere-cipher')
def autoKeyVigenere():
    return render_template('pages/auto-key-vigenere-cipher.html', encrypt=True)

@app.route('/auto-key-vigenere-cipher/encrypt', methods=['POST', 'GET'])
def autoKeyVigenereEncrypt():
    if request.method == 'POST':
        key = request.form['key']
        plaintext = request.form['plaintext']
        try:
            autoVigenere = AutoKeyVigenereCipher(key=key, plaintext=plaintext)
            autoVigenere.encrypt()
            return render_template('pages/auto-key-vigenere-cipher.html', encrypt=True, 
                result_ciphertext = autoVigenere, form = request.form)            
        except (Exception) as e:
            return render_template('pages/auto-key-vigenere-cipher.html', encrypt=True, 
                error = e, form = request.form)
    else:
        return render_template('pages/auto-key-vigenere-cipher.html', encrypt=True)

@app.route('/auto-key-vigenere-cipher/decrypt', methods=['POST', 'GET'])
def autoKeyVigenereDecrypt():
    if request.method == 'POST':
        key = request.form['key']
        ciphertext = request.form['ciphertext']
        try:
            autoVigenere = AutoKeyVigenereCipher(key=key, ciphertext=ciphertext)
            autoVigenere.decrypt()
            return render_template('pages/auto-key-vigenere-cipher.html', encrypt=False, 
                result_plaintext = autoVigenere, form = request.form)            
        except (Exception) as e:
            return render_template('pages/auto-key-vigenere-cipher.html', encrypt=False, 
                error = e, form = request.form)
    else:
        return render_template('pages/auto-key-vigenere-cipher.html', encrypt=False)


"""
--------------------------------------------------------------
# Route for Full Vigenere Cipher
--------------------------------------------------------------
"""
@app.route('/full-vigenere-cipher')
def fullKeyVigenere():
    return render_template('pages/full-vigenere-cipher.html', encrypt=True, 
        encryptTable=randomEncipherTable, alphabets= alphabets)

@app.route('/full-vigenere-cipher/encrypt', methods=['POST', 'GET'])
def fullKeyVigenereEncrypt():
    if request.method == 'POST':
        key = request.form['key']
        plaintext = request.form['plaintext']
        try:
            fullVigenere = FullVigenereCipher(key=key, plaintext=plaintext, 
                encryptTable=randomEncipherTable)
            fullVigenere.encrypt()
            return render_template('pages/full-vigenere-cipher.html', encrypt=True, 
                result_ciphertext = fullVigenere, form = request.form, encryptTable=randomEncipherTable
                , alphabets= alphabets)            
        except (Exception) as e:
            return render_template('pages/full-vigenere-cipher.html', encrypt=True, 
                error = e, form = request.form, encryptTable=randomEncipherTable, alphabets= alphabets)
    else:
        return render_template('pages/full-vigenere-cipher.html', encrypt=True, 
            encryptTable=randomEncipherTable, alphabets= alphabets)

@app.route('/full-vigenere-cipher/decrypt', methods=['POST', 'GET'])
def fullVigenereDecrypt():
    if request.method == 'POST':
        key = request.form['key']
        ciphertext = request.form['ciphertext']
        try:
            fullVigenere = FullVigenereCipher(key=key, ciphertext=ciphertext, 
                encryptTable=randomEncipherTable)
            fullVigenere.decrypt()
            return render_template('pages/full-vigenere-cipher.html', encrypt=False, 
                result_plaintext = fullVigenere, form = request.form, encryptTable=randomEncipherTable
                , alphabets= alphabets)            
        except (Exception) as e:
            return render_template('pages/full-vigenere-cipher.html', encrypt=False, 
                error = e, form = request.form, encryptTable=randomEncipherTable, alphabets= alphabets)
    else:
        return render_template('pages/full-vigenere-cipher.html', encrypt=False, 
            encryptTable=randomEncipherTable, alphabets= alphabets)

"""
--------------------------------------------------------------
# Route for Playfair Cipher
--------------------------------------------------------------
"""
@app.route('/playfair-cipher')
def playfair():
    return render_template('pages/playfair-cipher.html', encrypt=True)

@app.route('/playfair-cipher/encrypt', methods=['POST', 'GET'])
def playfairEncrypt():
    if request.method == 'POST':
        key = request.form['key']
        plaintext = request.form['plaintext']
        try:
            playfair = PlayfairCipher(key=key, plaintext=plaintext)
            playfair.encrypt()
            return render_template('pages/playfair-cipher.html', encrypt=True, 
                result_ciphertext = playfair, form = request.form)            
        except (Exception) as e:
            return render_template('pages/playfair-cipher.html', encrypt=True, 
                error = e, form = request.form)
    else:
        return render_template('pages/playfair-cipher.html', encrypt=True)

@app.route('/playfair-cipher/decrypt', methods=['POST', 'GET'])
def playfairDecrypt():
    if request.method == 'POST':
        key = request.form['key']
        ciphertext = request.form['ciphertext']
        try:
            playfair = PlayfairCipher(key=key, ciphertext=ciphertext)
            playfair.decrypt()
            return render_template('pages/playfair-cipher.html', encrypt=False, 
                result_plaintext = playfair, form = request.form)            
        except (Exception) as e:
            return render_template('pages/playfair-cipher.html', encrypt=False, 
                error = e, form = request.form)
    else:
        return render_template('pages/playfair-cipher.html', encrypt=False)




"""
--------------------------------------------------------------
# Flask Main Program
--------------------------------------------------------------
"""
if __name__ == '__main__':
    app.run(debug=True,threaded=True)
    #    f = open('D:/Kulyeah/sem 5/Kripto/Classic-Cipher/src/static/images/Crypto Logo.png', "rb")
    # print(f.read())