from flask import Flask, render_template, request, redirect, url_for
from Playfair import PlayfairCipher
from Vigenere import VigenereCipher, FullVigenereCipher, ExtendedVigenereCipher, AutoKeyVigenereCipher
from Affine import AffineCipher
from Hill import HillCipher
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
# Route for Extended Vigenere Table
--------------------------------------------------------------
"""
@app.route('/extended-vigenere-cipher')
def extendedVigenere():
	return render_template('pages/extended-vigenere-cipher.html', encrypt=True,
		encryptTable=randomEncipherTable, alphabets= alphabets)

@app.route('/extended-vigenere-cipher/encrypt', methods=['POST', 'GET'])
def extendedVigenereEncrypt():
	if request.method == 'POST':
		try:
			choice = request.form["encrypt"]
			key = request.form['key']
			if (choice == "file"):
				plaintext = request.form['plaintext']
				extendedVigenere = ExtendedVigenereCipher(key=key, plaintext=plaintext)
				extendedVigenere.encrypt()
				return render_template('pages/extended-vigenere-cipher.html', encrypt=True,
					result_ciphertext = extendedVigenere, form = request.form)
			else:
				raise Exception("Encrypt file's byte not yet implemented")
		except (Exception) as e:
			return render_template('pages/extended-vigenere-cipher.html', encrypt=True,
				error = e, form = request.form)
	else:
		return render_template('pages/extended-vigenere-cipher.html', encrypt=True)

@app.route('/extended-vigenere-cipher/decrypt', methods=['POST', 'GET'])
def extendedVigenereDecrypt():
	if request.method == 'POST':
		try:
			choice = request.form["decrypt"]
			key = request.form['key']
			if (choice == "file"):
				ciphertext = request.form['ciphertext']
				extendedVigenere = ExtendedVigenereCipher(key=key, ciphertext=ciphertext)
				extendedVigenere.decrypt()
				return render_template('pages/extended-vigenere-cipher.html', encrypt=False,
					result_plaintext = extendedVigenere, form = request.form)
			else:
				raise Exception("Decrypt file's byte not yet implemented")
		except (Exception) as e:
			return render_template('pages/extended-vigenere-cipher.html', encrypt=False,
				error = e, form = request.form)
	else:
		return render_template('pages/extended-vigenere-cipher.html', encrypt=False)
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
# Route for Affine Cipher
--------------------------------------------------------------
"""
@app.route('/affine-cipher')
def affine():
	return render_template('pages/affine-cipher.html', encrypt=True)

@app.route('/affine-cipher/encrypt', methods=['POST', 'GET'])
def affineEncrypt():
	if request.method == 'POST':
		keyM = int(request.form['keyM'])
		keyB = int(request.form['keyB'])
		plaintext = request.form['plaintext']
		try:
			affine = AffineCipher(b=keyB, m=keyM, plaintext=plaintext)
			affine.encrypt()
			return render_template('pages/affine-cipher.html', encrypt=True,
				result_ciphertext = affine, form = request.form)
		except (Exception) as e:
			return render_template('pages/affine-cipher.html', encrypt=True,
				error = e, form = request.form)
	else:
			return render_template('pages/affine-cipher.html', encrypt=True)

@app.route('/affine-cipher/decrypt', methods=['POST', 'GET'])
def affineDecrypt():
	if request.method == 'POST':
		keyM = int(request.form['keyM'])
		keyB = int(request.form['keyB'])
		ciphertext = request.form['ciphertext']
		try:
			affine = AffineCipher(b=keyB, m=keyM, ciphertext=ciphertext)
			affine.decrypt()
			return render_template('pages/affine-cipher.html', encrypt=False,
				result_plaintext = affine, form = request.form)
		except (Exception) as e:
			return render_template('pages/affine-cipher.html', encrypt=False,
				error = e, form = request.form)
	else:
			return render_template('pages/affine-cipher.html', encrypt=False)

"""
--------------------------------------------------------------
# Route for Hill cipher
--------------------------------------------------------------
"""
@app.route('/hill-cipher')
def hill():
	return render_template('pages/hill-cipher.html', encrypt=True)

@app.route('/hill-cipher/encrypt', methods=['POST', 'GET'])
def hillEncrypt():
	if request.method == 'POST':
		try:
			matrixKey=[]
			for i in range(3):
				matrixRow = []
				for j in range(3):
					matrixCol = request.form['r-'+str(i+1)+'c-'+str(j+1)]
					if (not matrixCol):
						raise Exception("All matrix key must be filled")
					matrixRow.append(int(matrixCol))
				matrixKey.append(matrixRow)
			plaintext = request.form['plaintext']
			hill = HillCipher(m=matrixKey ,plaintext=plaintext)
			hill.encrypt()
			return render_template('pages/hill-cipher.html', encrypt=True, result_ciphertext = hill, 
				form = request.form)
		except (Exception) as e:
			return render_template('pages/hill-cipher.html', encrypt=True, error = e, 
				form = request.form)
	else:
			return render_template('pages/hill-cipher.html', encrypt=True)

@app.route('/hill-cipher/decrypt', methods=['POST', 'GET'])
def hillDecrypt():
	if request.method == 'POST':
		try:
			matrixKey=[]
			for i in range(3):
				matrixRow = []
				for j in range(3):
					matrixCol = request.form['r-'+str(i+1)+'c-'+str(j+1)]
					if (not matrixCol):
						raise Exception("All matrix key must be filled")
					matrixRow.append(int(matrixCol))
				matrixKey.append(matrixRow)
			ciphertext = request.form['ciphertext']
			hill = HillCipher(m=matrixKey, ciphertext=ciphertext)
			print(hill.decrypt())
			return render_template('pages/hill-cipher.html', encrypt=False, result_plaintext = hill, 
				form = request.form)
		except (Exception) as e:
			return render_template('pages/hill-cipher.html', encrypt=False, error = e, 
				form = request.form)
	else:
			return render_template('pages/hill-cipher.html', encrypt=False)

"""
--------------------------------------------------------------
# Flask Main Program
--------------------------------------
------------------------
"""
if __name__ == '__main__':
    app.run(debug=True,threaded=True)
    #    f = open('D:/Kulyeah/sem 5/Kripto/Classic-Cipher/src/static/images/Crypto Logo.png', "rb")
    # print(f.read())
