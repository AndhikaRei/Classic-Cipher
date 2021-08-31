import re
from typing import List

# 
# alphabets is a string that represent all Indonesia alphabet.
alphabets:str = "abcdefghijklmnopqrstuvwxyz"

class PlayfairCipher:
    """
    A class used for representing PlayfairCipher and it's component.

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
        Constructor for PlayfairCipher class. Either plaintext or ciphertext must be empty at 
        creation.

        Parameters
        ----------
        key : str
            Key for encrypting or decrypting a text.
        plaintext : str, optional
            Text you want to encrypt or ciphertext after decrypted.
        cipherthex : int, optional
            Text you want to decrypt or plaintext after encrypted.
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

        ciphertext = ciphertext.lower() # ini buat apa ya? bknya udh di lower di normalizeText?
        self.ciphertext = ciphertext
        if (ciphertext != ""):
            self.ciphertext = self.normalizeText(ciphertext)
        
        key = key.lower() # ini juga
        self.key = key
        if (key != ""):
            self.key = self.normalizeKey(key)

    def encrypt(self)->str:
        """
        Method to encrypt current plaintext with current key.
        
        Return the capitalized ciphertext. 
        """

        # Class validation. 
        if (self.plaintext == "" or self.ciphertext != ""):
            raise Exception("Plaintext must be filled and ciphertext must be empty")

        # Variable declaration.
        ciphertext:str = ""
        letter1:int
        letter2:int

        # Encrypt the plaintext. 
        for i in range (0, len(self.plaintext), 2):

            # Assign to variable
            letter1 = self.key.find(self.plaintext[i])
            letter2 = self.key.find(self.plaintext[i+1])

            # 2 chars in the same row
            if (letter1//5 == letter2//5):
                ciphertext += self.key[(letter1//5)*5 + ((letter1%5)+1)%5]
                ciphertext += self.key[(letter2//5)*5 + ((letter2%5)+1)%5]

            # 2 chars in the same column
            elif (letter1%5 == letter2%5):
                ciphertext += self.key[(letter1+5)%25]
                ciphertext += self.key[(letter2+5)%25]

            # Other places
            else:
                ciphertext += self.key[(letter1//5)*5 + letter2%5]
                ciphertext += self.key[(letter2//5)*5 + letter1%5]
        
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
    def generateBasicPlayfairTable()->List[str]:
        """
        Method to generate normal Playfair Cipher encrypt table.
        
        Return the List of string representing normal Playfair Cipher encrypt table. 
        """

        # Variable declaration.
        basicPlayfairTable:List[str] = []

        # Loop to create Playfair Cipher table.
        for i in range(26):
            if (i==0):
                basicPlayfairTable.append(alphabets)
            else:
                basicPlayfairTable.append(basicPlayfairTable[i-1][1:]+basicPlayfairTable[i-1][0])
        
        return basicPlayfairTable


    @staticmethod
    def normalizeText(text:str)-> str:
        """
        Method to normalize text by removing space and punctuation, swap char "j" to "i", 
        add aditional char "x" for two consecutives same chars or unpaired chars.
        Assumption: no 3 or more consecutive same char, no "x" at end of text. 
        
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

        # Swap char "j" to "i"
        normalizedText.replace("j", "i")

        # Add aditional char "x"
        normalizedText = re.sub(r'(.)\1', r'\1x\1', normalizedText)

        # Add char "x" at end of text if length is odd
        if (len(normalizedText) % 2 == 1):
            normalizedText += "x"

        return normalizedText        
    
    @staticmethod
    def normalizeKey(key:str)-> str:
        """
        Method to normalize key by removing space, punctuation, duplicates, and char "j",
        also complete key with the rest of alphabet if length < 25.
        
        Return the normalized key. 
        
        Parameters
        ----------
        key : str 
            Key you want to normalize
        """

        # Variable declaration.
        normalizedKey:str

        # Remove number, punctuation, and space.
        normalizedKey = "".join(filter(str.isalpha, key)).lower()

        # Remove char "j"
        normalizedKey.replace("j", "")

        # Complete the key with the rest of alphabet
        for letter in alphabets:
            if letter not in normalizedKey:
                normalizedKey += letter

        return normalizedKey

# Test for normal.
a = "temui ibu nanti malam"
b = "alngeshpubcdfikmoqrtvwxyz"
c = "LVVQHZNGFHRVL"
d = PlayfairCipher(key=b, plaintext=a)
print(d.encrypt())
# print(d.key)