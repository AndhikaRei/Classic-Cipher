from typing import List

from Utility import alphabets

class VigenereCipher:
    """
    A class used for representing VigenereCipher and it's component.

    Attributes.
    ----------
    plaintext : str
        Text you want to encrypt or ciphertext after decrypted. In lowercase format.
    ciphertext : str
        Text you want to decrypt or plaintext after encrypted. In lowercase format.
    key : str
        Key for encrypting or decrypting a text. 
    """

    def __init__(self, key:str, plaintext: str ="", ciphertext:str="") -> None:
        """
        Constructor for VigenereCipher class. Either plaintext or ciphertext must be empty at 
        creation.

        Parameters
        ----------
        key : str
            Text you want to encrypt or ciphertext after decrypted.
        plaintext : str, optional
            Text you want to decrypt or plaintext after encrypted.
        cipherthex : int, optional
            Key for encrypting or decrypting a text.
        """

        # Input validation.
        if (plaintext != "" and ciphertext != ""):
            raise Exception("Either plaintext or ciphertext must be empty")
        if (plaintext == "" and ciphertext == ""):
            raise Exception("Either plaintext or ciphertext must be filled")
        if (key ==""):
            raise Exception("Key must be filled!")

        self.plaintext = plaintext
        if (plaintext != ""):
            self.plaintext = self.normalizeText(plaintext)

        ciphertext = ciphertext.lower()
        self.ciphertext = ciphertext
        if (ciphertext != ""):
            self.ciphertext = self.normalizeText(ciphertext)
        
        key = key.lower()
        self.key = key
        if (key != ""):
            if (self.plaintext != ""):
                self.key = self.normalizeKey(self.plaintext, key)
            else:
                self.key = self.normalizeKey(self.ciphertext, key)

    def encrypt(self)->str:
        """
        Method to encrypt current plaintext with current key. Modify ciphertext attribute also
        
        Return the capitalized ciphertext. 
        """

        # Class validation. 
        if (self.plaintext == "" or self.ciphertext != ""):
            raise Exception("Plaintext must be filled and ciphertext must be empty")

        # Variable declaration.
        ciphertext:str = ""

        # Encrypt the plaintext. 
        for (p,k) in zip(self.plaintext, self.key):
            ciphertext = ciphertext + alphabets[(alphabets.find(p)+alphabets.find(k))%26]
        
        self.ciphertext = ciphertext
        return ciphertext.upper()

    
    def decrypt(self)->str:
        """
        Method to decrypt current ciphertext with current key. Modify plaintext attribute also
        
        Return the plaintext. 
        """

        # Class validation.
        if (self.plaintext != "" and self.ciphertext == ""):
            raise Exception("Plaintext must be empty and ciphertext must be filled")

        # Variable declaration.
        plaintext:str = ""

        # Encrypt the plaintext. 
        for (c,k) in zip(self.ciphertext, self.key):
            plaintext = plaintext + alphabets[(alphabets.find(c)-alphabets.find(k))%26]
        
        self.plaintext = plaintext
        return plaintext


    @staticmethod
    def generateBasicVigenereTable()->List[str]:
        """
        Method to generate normal Vigenere Cipher encrypt table.
        
        Return the List of string representing normal Vigenere Cipher encrypt table. 
        """

        # Variable declaration.
        basicVigenereTable:List[str] = []

        # Loop to create Vigenere Cipher table.
        for i in range(26):
            if (i==0):
                basicVigenereTable.append(alphabets)
            else:
                basicVigenereTable.append(basicVigenereTable[i-1][1:]+basicVigenereTable[i-1][0])
        
        return basicVigenereTable


    @staticmethod
    def normalizeText(text:str)-> str:
        """
        Method to normalize text by removing space and punctuation.
        
        Return the normalized text. 
        
        Parameters
        ----------
        text : str
            Text you want to normalize.
        """

        # Variable declaration.
        normalizedText:str
        
        # Remove number, punctuation, and space.
        normalizedText = "".join(filter(str.isalpha, text)).lower()
        return normalizedText        
    
    @staticmethod
    def normalizeKey(text:str, key:str)-> str:
        """
        Method to normalize key by removing space, punctuation, and repeat the key until it have 
        same lenght with text. Text can be normalized plaintext or normalized ciphertext.
        
        Return the normalized key. 
        
        Parameters
        ----------
        text : str
            Normalized text (can be plaintext or ciphertext).
        key : str 
            Key you want to normalize
        """

        # Variable declaration.
        normalizedKey:str

        # Remove number, punctuation, and space.
        normalizedKey = "".join(filter(str.isalpha, key)).lower()

        # Repeat key until it has same length with plaintext.
        normalizedKey = (normalizedKey*(len(text)//len(normalizedKey)+1))[:len(text)]

        return normalizedKey

class FullVigenereCipher(VigenereCipher):
    """
    A class used for representing Full Vigenere Cipher and it's component. It's basically same 
    with Vigenere Cipher except it's use permutation of encrypt table for encrypt and decrypt. So 
    it will have new attribute in class

    Attributes.
    ----------
    plaintext : str
        Text you want to encrypt or ciphertext after decrypted. In lowercase format.
    ciphertext : str
        Text you want to decrypt or plaintext after encrypted. In lowercase format.
    key : str
        Key for encrypting or decrypting a text.
    encryptTable: List[str]
        Encrypt table for encrypting and decrypting. 
    """

    def __init__(self, key:str, plaintext: str ="", ciphertext:str="", encryptTable:List[str]=[]) -> None:
        """
        Constructor for FullVigenereCipher class. Either plaintext or ciphertext must be empty at 
        creation.

        Parameters
        ----------
        key : str
            Text you want to encrypt or ciphertext after decrypted.
        plaintext : str
            Text you want to decrypt or plaintext after encrypted.
        cipherthex : int, optional
            Key for encrypting or decrypting a text.
        encryptTable : List[str], optional
        """

        super(FullVigenereCipher, self).__init__(key, plaintext, ciphertext)
        
        self.encryptTable = encryptTable
        if (len(encryptTable)==0):
            self.encryptTable = self.generateBasicVigenereTable()
    
    def encrypt(self)->str:
        """
        Method to encrypt current plaintext with current key and current encrypt table. 
        Modify ciphertext attribute also
        
        Return the capitalized ciphertext. 
        """

        # Class validation. 
        if (self.plaintext == "" or self.ciphertext != ""):
            raise Exception("Plaintext must be filled and ciphertext must be empty")


        # Variable declaration.
        ciphertext:str = ""

        # Encrypt the plaintext. 
        for (p,k) in zip(self.plaintext, self.key):
            ciphertext = ciphertext + self.encryptTable[alphabets.find(k)][alphabets.find(p)]
        
        self.ciphertext = ciphertext
        return ciphertext.upper()

    
    def decrypt(self)->str:
        """
        Method to decrypt current ciphertext with current key. Modify plaintext attribute also
        
        Return the plaintext. 
        """

        # Class validation.
        if (self.plaintext != "" and self.ciphertext != ""):
            raise Exception("Either plaintext or ciphertext must be empty")

        # Variable declaration.
        plaintext:str = ""

        # Encrypt the plaintext. 
        for (c,k) in zip(self.ciphertext, self.key):
            plaintext = plaintext + alphabets[self.encryptTable[alphabets.find(k)].find(c)]
        
        self.plaintext = plaintext
        return plaintext

class AutoKeyVigenereCipher(VigenereCipher):
    """
    A class used for representing Auto-Key Vigenere Cipher and it's component. It's basically same 
    with Vigenere Cipher except it's way for normalizing key and decrypt the ciphertext.

    Attributes.
    ----------
    plaintext : str
        Text you want to encrypt or ciphertext after decrypted. In lowercase format.
    ciphertext : str
        Text you want to decrypt or plaintext after encrypted. In lowercase format.
    key : str
        Key for encrypting or decrypting a text. 
    """

    def __init__(self, key:str, plaintext: str ="", ciphertext:str="") -> None:
        """
        Constructor for AutoKeyVigenereCipher class. Either plaintext or ciphertext must be empty at 
        creation. If plaintext are empty then key will not be fully normalized (must decrypt the 
        ciphertext first to know the complete key), else if ciphertext are empty then key will 
        be normalized.

        Parameters
        ----------
        key : str
            Text you want to encrypt or ciphertext after decrypted.
        plaintext : str
            Text you want to decrypt or plaintext after encrypted.
        cipherthex : int, optional
            Key for encrypting or decrypting a text.
        """

        # Input validation.
        if (plaintext != "" and ciphertext != ""):
            raise Exception("Either plaintext or ciphertext must be empty")
        if (plaintext == "" and ciphertext == ""):
            raise Exception("Either plaintext or ciphertext must be filled")
        if (key ==""):
            raise Exception("Key must be filled!")

        self.plaintext = plaintext
        if (plaintext != ""):
            self.plaintext = self.normalizeText(plaintext)

        ciphertext = ciphertext.lower()
        self.ciphertext = ciphertext
        if (ciphertext != ""):
            self.ciphertext = self.normalizeText(ciphertext)
        
        key = key.lower()
        self.key = key
        if (key != ""):
            if (self.plaintext != ""):
                self.key = self.normalizeKey(self.plaintext, key)
            else:
                self.key = self.normalizeText(key)

    def decrypt(self)->str:
        """
        Method to decrypt current ciphertext with current key. While decrypting it will also 
        complete the key. Modify plaintext attribute.
        
        Return the plaintext. 
        """

        # Class validation.
        if (self.plaintext != "" and self.ciphertext != ""):
            raise Exception("Either plaintext or ciphertext must be empty")

        # Variable declaration.
        plaintext:str = ""
        currPlainText:chr = ""

        # Encrypt the plaintext. 
        # Notify that it will dinamically update the key.
        for (index, c) in enumerate(self.ciphertext):
            currPlainText = alphabets[(alphabets.find(c)-alphabets.find(self.key[index]))%26]
            plaintext = plaintext + currPlainText
            if (len(self.key) < len(self.ciphertext)):
                self.key = self.key + currPlainText
        
        self.plaintext = plaintext
        return plaintext

    @staticmethod
    def normalizeKey(plaintext:str, key:str)-> str:
        """
        Method to normalize key by removing space, punctuation, and fill the key with repeated text 
        until it have same lenght with text. "text" must be normalized plaintext. Otherwise you can
        complete the key while decrypting ciphertext.
        
        Return the normalized key. 
        
        Parameters
        ----------
        plaintext : str
            Normalized plaintext.
        key : str 
            Key you want to normalize
        """

        # Variable declaration.
        normalizedKey:str
        
        # Remove number, punctuation, and space.
        normalizedKey = "".join(filter(str.isalpha, key)).lower()

        # Repeat key until it has same length with plaintext.
        normalizedKey = (normalizedKey + plaintext*(len(plaintext)//len(normalizedKey)+1))[:len(plaintext)]
        return normalizedKey

class ExtendedVigenereCipher:
    """
    A class used for representing Extended Vigenere Cipher and it's component. It's basically 
    Vigenere Cipher with 256 ASCII character.

    Attributes.
    ----------
    plaintext : str
        Text you want to encrypt or ciphertext after decrypted. In lowercase format.
    ciphertext : str
        Text you want to decrypt or plaintext after encrypted. In lowercase format.
    key : str
        Key for encrypting or decrypting a text. 
    """

    def __init__(self, key:str, plaintext: str ="", ciphertext:str="") -> None:
        """
        Constructor for VigenereCipher class. Either plaintext or ciphertext must be empty at 
        creation.

        Parameters
        ----------
        key : str
            Text you want to encrypt or ciphertext after decrypted.
        plaintext : str, optional
            Text you want to decrypt or plaintext after encrypted.
        cipherthex : int, optional
            Key for encrypting or decrypting a text.
        """

        # Input validation.
        if (plaintext != "" and ciphertext != ""):
            raise Exception("Either plaintext or ciphertext must be empty")
        if (plaintext == "" and ciphertext == ""):
            raise Exception("Either plaintext or ciphertext must be filled")
        if (key ==""):
            raise Exception("Key must be filled!")

        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.key = key
        if (key != ""):
            if (self.plaintext != ""):
                self.key = self.normalizeKey(self.plaintext, key)
            else:
                self.key = self.normalizeKey(self.ciphertext, key)
    
    @staticmethod
    def normalizeKey(text:str, key:str)-> str:
        """
        Method to normalize key by repeat the key until it have same length with text. 
        Text can be plaintext or ciphertext.

        Return the normalized key. 
        
        Parameters
        ----------
        text : str
            Normalized text (can be plaintext or ciphertext).
        key : str 
            Key you want to normalize
        """

        # Variable declaration.
        normalizedKey:str

        # Repeat key until it has same length with plaintext.
        normalizedKey = (key*(len(text)//len(key)+1))[:len(text)]
        return normalizedKey
    
    def encrypt(self)->str:
        """
        Method to encrypt current plaintext with current key. Modify ciphertext attribute also
        
        Return the ciphertext. 
        """

        # Class validation. 
        if (self.plaintext == "" or self.ciphertext != ""):
            raise Exception("Plaintext must be filled and ciphertext must be empty")


        # Variable declaration.
        ciphertext:str = ""

        # Encrypt the plaintext. 
        for (p,k) in zip(self.plaintext, self.key):
            ciphertext = ciphertext + chr((ord(p) + ord(k)) % 256)
        
        self.ciphertext = ciphertext
        return ciphertext

    
    def decrypt(self)->str:
        """
        Method to decrypt current ciphertext with current key. Modify plaintext attribute also
        
        Return the plaintext. 
        """

        # Class validation.
        if (self.plaintext != "" and self.ciphertext != ""):
            raise Exception("Either plaintext or ciphertext must be empty")

        # Variable declaration.
        plaintext:str = ""

        # Encrypt the plaintext. 
        for (c,k) in zip(self.ciphertext, self.key):
            plaintext = plaintext + chr((ord(c) - ord(k)) % 256)
        
        self.plaintext = plaintext
        return plaintext

# # Test for normal.
# a = "thisplaintext"
# b = "sony"
# c = "LVVQHZNGFHRVL"
# d = VigenereCipher(key=b, ciphertext=c)
# print(d.decrypt())
# print(d.key)

# Test for full vigenere cipher.
# a = "thisplaintext"
# b = "sony"
# c = "LVVQHZNGFHRVL"
# d = FullVigenereCipher(key=b, ciphertext=c)
# print(d.decrypt())

# # Test for auto key.
# a = "attack the east wall at dawn"
# b = "QUEEN"
# c = "QNXEPKMAEGKLAAELDTPDLHN"
# d = AutoKeyVigenereCipher(key=b, ciphertext=c)
# print(d.decrypt())
# print(d.key)

# Text for extended cipher
# a = "thisplaintext"
# b = chr(1)
# c = "LVVQHZNGFHRVL"
# d = ExtendedVigenereCipher(key=b, ciphertext=c)
# print(d.decrypt())
# print(d.key)