def vigenere_encrypt(text, key):
    text = "".join(filter(str.isalpha, text)).lower()
    key = "".join(filter(str.isalpha, key)).lower()
    result = ""
    for i in range(len(text)):

        # ord('a') = 97, jadi dikurang 2*97 = 194
        result += chr(97 + ((ord(text[i]) + ord(key[i%len(key)]) - 194) % 26))

    return result


def vigenere_decrypt(text, key):
    result = ""
    for i in range(len(text)):

        result += chr(97 + ((ord(text[i]) - ord(key[i%len(key)])) % 26))

    return result


def fullVigenere_encrypt(text, key):
    alph = "tbgukfcrwjelpnzmqhsadvixyo"
    text = "".join(filter(str.isalpha, text)).lower()
    key = "".join(filter(str.isalpha, key)).lower()
    result = ""
    for i in range(len(text)):

        # ord('a') = 97, jadi dikurang 2*97 = 194
        result += alph[((ord(text[i]) + ord(key[i%len(key)]) - 194) % 26)]

    return result


def fullVigenere_decrypt(text, key):
    alph = "tbgukfcrwjelpnzmqhsadvixyo"
    result = ""
    for i in range(len(text)):

        result += chr(97 + ((alph.find(text[i])- ord(key[i%len(key)]) + 97) % 26))

    return result


def autoVigenere_encrypt(text, key):
    text = "".join(filter(str.isalpha, text)).lower()
    key = "".join(filter(str.isalpha, key)).lower()
    result = ""
    for i in range(len(text)):
        
        if (i < len(key)):
            result += chr(97 + ((ord(text[i]) + ord(key[i]) - 194) % 26))
        else:
            result += chr(97 + ((ord(text[i]) + ord(text[i-len(key)]) - 194) % 26))

    return result


def autoVigenere_decrypt(text, key):
    result = ""
    for i in range(len(text)):
        
        if (i < len(key)):
            result += chr(97 + ((ord(text[i]) - ord(key[i])) % 26))
        else:
            result += chr(97 + ((ord(text[i]) - ord(result[i-len(key)])) % 26))

    return result


def extendedVigenere_encrypt(text, key):
    result = ""
    for i in range(len(text)):

        result += chr((ord(text[i]) + ord(key[i%len(key)])) % 256)

    return result


def extendedVigenere_decrypt(text, key):
    result = ""
    for i in range(len(text)):

        result += chr((ord(text[i]) - ord(key[i%len(key)])) % 256)

    return result



text = str(input("Masukkan text: "))
key = str(input("Masukkan kunci: "))

print(vigenere_decrypt(text, key))