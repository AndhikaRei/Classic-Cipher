import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, current_app
from werkzeug.datastructures import FileStorage

from Playfair import PlayfairCipher
from Vigenere import VigenereCipher, FullVigenereCipher, ExtendedVigenereCipher, AutoKeyVigenereCipher
from Affine import AffineCipher
from Hill import HillCipher
from Utility import alphabets

# Flask Configuration.
app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
# Index route.
@app.route('/vigenere-cipher')
def vigenere():
	return render_template('pages/vigenere-cipher.html', encrypt=True)

# Encrypt route.
@app.route('/vigenere-cipher/encrypt', methods=['POST', 'GET'])
def vigenereEncrypt():
	if request.method == 'POST':
		# Get the request payload.
		key = request.form['key']
		plaintext = request.form['plaintext']
		# Catch exception when processing Vigenere Cipher.
		try:
			# Process Encrypt Vigenere Cipher.
			vigenere = VigenereCipher(key=key, plaintext=plaintext)
			vigenere.encrypt()
			# Render successfull webpage with data.
			return render_template('pages/vigenere-cipher.html', encrypt=True,
				result_ciphertext = vigenere, form = request.form)
		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/vigenere-cipher.html', encrypt=True, error = e,
				form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('vigenere'))

# Decrypt route.
@app.route('/vigenere-cipher/decrypt', methods=['POST', 'GET'])
def vigenereDecrypt():
	if request.method == 'POST':
		# Get the request payload.
		key = request.form['key']
		ciphertext = request.form['ciphertext']
	# Catch exception when processing Vigenere Cipher.
		try:
			# Process Decrypt Vigenere Cipher.
			vigenere = VigenereCipher(key=key, ciphertext=ciphertext)
			vigenere.decrypt()
			# Render successfull webpage with data.
			return render_template('pages/vigenere-cipher.html', encrypt=False,
					result_plaintext = vigenere, form = request.form)
		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/vigenere-cipher.html', encrypt=False,
				error = e, form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('vigenere'))


"""
--------------------------------------------------------------
# Route for Auto-key Vigenere Cipher
--------------------------------------------------------------
"""
# Index route.
@app.route('/auto-key-vigenere-cipher')
def autoKeyVigenere():
		return render_template('pages/auto-key-vigenere-cipher.html', encrypt=True)

# Encrypt route.
@app.route('/auto-key-vigenere-cipher/encrypt', methods=['POST', 'GET'])
def autoKeyVigenereEncrypt():
	if request.method == 'POST':
		# Get the request payload.
		key = request.form['key']
		plaintext = request.form['plaintext']
		# Catch exception when processing Auto-key Vigenere Cipher.
		try:
			# Process Encrypt Auto-key Vigenere Cipher.
			autoVigenere = AutoKeyVigenereCipher(key=key, plaintext=plaintext)
			autoVigenere.encrypt()
			# Render successfull webpage with data.
			return render_template('pages/auto-key-vigenere-cipher.html', encrypt=True,
					result_ciphertext = autoVigenere, form = request.form)
		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/auto-key-vigenere-cipher.html', encrypt=True,
				error = e, form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('autoKeyVigenere'))

# Decrypt route.
@app.route('/auto-key-vigenere-cipher/decrypt', methods=['POST', 'GET'])
def autoKeyVigenereDecrypt():
	if request.method == 'POST':
		# Get the request payload.
		key = request.form['key']
		ciphertext = request.form['ciphertext']
		# Catch exception when processing Auto-key Vigenere Cipher.
		try:
			# Process Decrypt Auto-key Vigenere Cipher.
			autoVigenere = AutoKeyVigenereCipher(key=key, ciphertext=ciphertext)
			autoVigenere.decrypt()
			# Render successfull webpage with data.
			return render_template('pages/auto-key-vigenere-cipher.html', encrypt=False,
				result_plaintext = autoVigenere, form = request.form)
		except (Exception) as e:
			# Render error webpage.
			return render_template('pages/auto-key-vigenere-cipher.html', encrypt=False,
				error = e, form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('autoKeyVigenere'))


"""
--------------------------------------------------------------
# Route for Full Vigenere Cipher
--------------------------------------------------------------
"""
# Index route.
@app.route('/full-vigenere-cipher')
def fullKeyVigenere():
	return render_template('pages/full-vigenere-cipher.html', encrypt=True,
		encryptTable=randomEncipherTable, alphabets= alphabets)

# Encrypt route.
@app.route('/full-vigenere-cipher/encrypt', methods=['POST', 'GET'])
def fullKeyVigenereEncrypt():
	if request.method == 'POST':
		# Get the request payload.
		key = request.form['key']
		plaintext = request.form['plaintext']
		# Catch exception when processing Full-key Vigenere Cipher.
		try:
			# Process Encrypt Full-key Vigenere Cipher.
			fullVigenere = FullVigenereCipher(key=key, plaintext=plaintext,
				encryptTable=randomEncipherTable)
			fullVigenere.encrypt()
			# Render successfull webpage with data.
			return render_template('pages/full-vigenere-cipher.html', encrypt=True,
				result_ciphertext = fullVigenere, form = request.form, encryptTable=randomEncipherTable
				, alphabets= alphabets)
		except (Exception) as e:
			# Render error webpage.
			return render_template('pages/full-vigenere-cipher.html', encrypt=True,
				error = e, form = request.form, encryptTable=randomEncipherTable, alphabets= alphabets)
	else:
		# Render default webpage. 
		return redirect(url_for('fullKeyVigenere'))

# Decrypt route.
@app.route('/full-vigenere-cipher/decrypt', methods=['POST', 'GET'])
def fullKeyVigenereDecrypt():
	if request.method == 'POST':
		# Get the request payload.
		key = request.form['key']
		ciphertext = request.form['ciphertext']
		# Catch exception when processing Full-key Vigenere Cipher.
		try:
				# Process Decrypt Full-key Vigenere Cipher.
			fullVigenere = FullVigenereCipher(key=key, ciphertext=ciphertext,
					encryptTable=randomEncipherTable)
			fullVigenere.decrypt()
			# Render successfull webpage with data.
			return render_template('pages/full-vigenere-cipher.html', encrypt=False,
					result_plaintext = fullVigenere, form = request.form, encryptTable=randomEncipherTable
					, alphabets= alphabets)
		except (Exception) as e:
			# Render error webpage.
			return render_template('pages/full-vigenere-cipher.html', encrypt=False,
				error = e, form = request.form, encryptTable=randomEncipherTable, alphabets= alphabets)
	else:
		# Render default webpage. 
			return redirect(url_for('fullKeyVigenere'))

"""
--------------------------------------------------------------
# Route for Extended Vigenere Table
--------------------------------------------------------------
"""
# Index route.
@app.route('/extended-vigenere-cipher')
def extendedVigenere():
	return render_template('pages/extended-vigenere-cipher.html', encrypt=True,
		encryptTable=randomEncipherTable, alphabets= alphabets)

# Encrypt route.
@app.route('/extended-vigenere-cipher/encrypt', methods=['POST', 'GET'])
def extendedVigenereEncrypt():
	if request.method == 'POST':
		# Get the request payload.
		try:
			# Catch exception when processing Extended Vigenere Cipher.
			choice = request.form["encrypt"]
			key = request.form['key']
			# Process Encrypt Extended Vigenere Cipher.
			if (choice == "file"):
				# Encrypt file value.
				plaintext = request.form['plaintext']
				extendedVigenere = ExtendedVigenereCipher(key=key, plaintext=plaintext)
				extendedVigenere.encrypt()
				# Render successfull webpage with data.
				return render_template('pages/extended-vigenere-cipher.html', encrypt=True,
					result_ciphertext = extendedVigenere, form = request.form)
			else:
				# Encrypt file byte.
				file = request.files['file-plaintext']
				# Save the file to local and then open it.
				file.stream.seek(0)
				file.save(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], file.filename))
				with open(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], file.filename), "rb") as f:
					# Encrypt isi filenya dan simpen ke dalam file di tempat yg sama kek upload.
					extendedVigenere = ExtendedVigenereCipher(key=key, plaintext=f.read().decode('utf-8'))
					print(f.read())

				with open(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], file.filename), "wb") as f:
					f.write(bytearray(extendedVigenere.encrypt(), 'utf-8'))
					file.save(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], file.filename))
					# Ntar file hasil encrypt yang di save namanya harus berbeda terus di download.
					# Kalo misal bisa langsung rewrite file nya tanpa harus save file baru lebih bagus si. Ntar kalo gini nama filenya sama gpp.
					

				# Download The file.
				return send_from_directory(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER']), file.filename, as_attachment=True)
		except (Exception) as e:
			# Render error webpage.
			return render_template('pages/extended-vigenere-cipher.html', encrypt=True,
				error = e, form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('extendedVigenere'))

# Decrypt route.
@app.route('/extended-vigenere-cipher/decrypt', methods=['POST', 'GET'])
def extendedVigenereDecrypt():
	if request.method == 'POST':
		# Get the request payload.
		try:
			# Catch exception when processing Extended Vigenere Cipher.
			choice = request.form["decrypt"]
			key = request.form['key']
			# Process Decrypt Extended Vigenere Cipher.
			if (choice == "file"):
				# Encrypt file value.
				ciphertext = request.form['ciphertext']
				extendedVigenere = ExtendedVigenereCipher(key=key, ciphertext=ciphertext)
				extendedVigenere.decrypt()
				# Render successfull webpage with data.
				return render_template('pages/extended-vigenere-cipher.html', encrypt=False,
					result_plaintext = extendedVigenere, form = request.form)
			else:
				# Decrypt file byte.
				file = request.files['file-ciphertext']
				# Save the file to local and then open it.
				file.stream.seek(0)
				file.save(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], file.filename))
				with open(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], file.filename), "rb") as f:
					extendedVigenere = ExtendedVigenereCipher(key=key, ciphertext=str(f.read().decode('utf-8')))
					print(f.read())

				with open(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], file.filename), "wb") as f:
					f.write(bytearray(extendedVigenere.decrypt(), 'utf-8'))
					file.save(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], file.filename))
					# Decrypt isi filenya dan simpen ke dalam file di tempat yg sama kek upload.
					# Ntar file hasil decrypt yang di save namanya harus berbeda terus di download.
					# Kalo misal bisa langsung rewrite file nya tanpa harus save file baru lebih bagus si. Ntar kalo gini nama filenya sama gpp.
				
				# Download The file.
				return send_from_directory(os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER']), file.filename, as_attachment=True)

		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/extended-vigenere-cipher.html', encrypt=False,
				error = e, form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('extendedVigenere'))

"""
--------------------------------------------------------------
# Route for Playfair Cipher
--------------------------------------------------------------
"""
# Index route.
@app.route('/playfair-cipher')
def playfair():
	return render_template('pages/playfair-cipher.html', encrypt=True)

# Encrypt route.
@app.route('/playfair-cipher/encrypt', methods=['POST', 'GET'])
def playfairEncrypt():
	if request.method == 'POST':
		# Get the request payload.
		key = request.form['key']
		plaintext = request.form['plaintext']
		# Catch exception when processing Playfair Cipher.
		try:
			# Process Encrypt Playfair Cipher.
			playfair = PlayfairCipher(key=key, plaintext=plaintext)
			playfair.encrypt()
			return render_template('pages/playfair-cipher.html', encrypt=True,
				result_ciphertext = playfair, form = request.form, matrix = playfair.keyToMatrix())
				# Render successfull webpage with data.
		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/playfair-cipher.html', encrypt=True,
				error = e, form = request.form)
	else:
		# Render default webpage. 
		return redirect('pages/playfair-cipher.html', encrypt=True)

# Decrypt route.
@app.route('/playfair-cipher/decrypt', methods=['POST', 'GET'])
def playfairDecrypt():
	if request.method == 'POST':
		# Get the request payload.
		key = request.form['key']
		ciphertext = request.form['ciphertext']
		# Catch exception when processing Playfair Cipher.
		try:
			# Process Decrypt Playfair Cipher.
			playfair = PlayfairCipher(key=key, ciphertext=ciphertext)
			playfair.decrypt()
			return render_template('pages/playfair-cipher.html', encrypt=False,
				result_plaintext = playfair, form = request.form, matrix = playfair.keyToMatrix())
		except (Exception) as e:
			return render_template('pages/playfair-cipher.html', encrypt=False,
				error = e, form = request.form)
	else:
			return redirect(url_for('playfair'))

"""
--------------------------------------------------------------
# Route for Affine Cipher
--------------------------------------------------------------
"""
# Index route.
@app.route('/affine-cipher')
def affine():
	return render_template('pages/affine-cipher.html', encrypt=True)

# Encrypt route.
@app.route('/affine-cipher/encrypt', methods=['POST', 'GET'])
def affineEncrypt():
	if request.method == 'POST':
		# Get the request payload.
		keyM = int(request.form['keyM'])
		keyB = int(request.form['keyB'])
		plaintext = request.form['plaintext']
		# Catch exception when processing Affine Cipher.
		try:
			# Process Encrypt Affine Cipher.
			affine = AffineCipher(b=keyB, m=keyM, plaintext=plaintext)
			affine.encrypt()
			# Render successfull webpage with data.
			return render_template('pages/affine-cipher.html', encrypt=True,
				result_ciphertext = affine, form = request.form)
		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/affine-cipher.html', encrypt=True,
				error = e, form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('affine'))

# Decrypt route.
@app.route('/affine-cipher/decrypt', methods=['POST', 'GET'])
def affineDecrypt():
	if request.method == 'POST':
		# Get the request payload.
		keyM = int(request.form['keyM'])
		keyB = int(request.form['keyB'])
		ciphertext = request.form['ciphertext']
		# Catch exception when processing Affine Cipher.
		try:
				# Process Decrypt Affine Cipher.
			affine = AffineCipher(b=keyB, m=keyM, ciphertext=ciphertext)
			affine.decrypt()
			# Render successfull webpage with data.
			return render_template('pages/affine-cipher.html', encrypt=False,
				result_plaintext = affine, form = request.form)
		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/affine-cipher.html', encrypt=False,
				error = e, form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('affine'))

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
		# Catch exception when processing payload or encrypting Hill Cipher.
		try:
			# Get request payload.
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
			# Process encrypting Hill Cipher.
			hill = HillCipher(m=matrixKey ,plaintext=plaintext)
			hill.encrypt()
			# Render successfull webpage with data.
			return render_template('pages/hill-cipher.html', encrypt=True, result_ciphertext = hill, 
				form = request.form)
		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/hill-cipher.html', encrypt=True, error = e, 
				form = request.form)
	else:
		# Render default webpage. 
		return redirect(url_for('hill'))

@app.route('/hill-cipher/decrypt', methods=['POST', 'GET'])
def hillDecrypt():
	if request.method == 'POST':
		# Catch error when processing payload or decrypting Hill Cipher.
		try:
			# Get the request payload.
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
			# Process Decrypt Hill Cipher.
			hill = HillCipher(m=matrixKey, ciphertext=ciphertext)
			print(hill.decrypt())
			# Render successfull webpage with data.
			return render_template('pages/hill-cipher.html', encrypt=False, result_plaintext = hill, 
				form = request.form)
		except (Exception) as e:
			# Rende error webpage.
			return render_template('pages/hill-cipher.html', encrypt=False, error = e, 
				form = request.form)
	else:
		# Render default webpage. 
			return redirect(url_for('hill'))

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
