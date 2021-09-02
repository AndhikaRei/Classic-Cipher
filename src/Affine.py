from re import X
from typing import List

from Utility import alphabets, relativePrime, modularInverse

class AffineCipher:
    """
    A class used for representing Affine Cipher and it's component.

    Attributes.
    ----------
    plaintext : str
        Text you want to encrypt or ciphertext after decrypted. In lowercase format.
    ciphertext : str
        Text you want to decrypt or plaintext after encrypted. In lowercase format.
    b : int
        Number of shifting for encrypting or decrypting a text. 
    m : int
        Key for encrypting or decrypting a text.
    """

    def __init__(self, b:int, m:int, plaintext: str ="", ciphertext:str="") -> None:
        """
        Constructor for AffineCipher class. Either plaintext or ciphertext must be empty at 
        creation.

        Parameters
        ----------
        plaintext : str, optional
            Text you want to decrypt or plaintext after encrypted.
        cipherthex : int, optional
            Key for encrypting or decrypting a text.
        b : int
            Number of shifting for encrypting or decrypting a text. 
        m : int
            Key for encrypting or decrypting a text.
        """

        # Input validation.
        if (plaintext != "" and ciphertext != ""):
            raise Exception("Either plaintext or ciphertext must be empty")
        if (plaintext == "" and ciphertext == ""):
            raise Exception("Either plaintext or ciphertext must be filled")
        if (b == None or m == None):
            raise Exception("Key must be filled!")

        self.plaintext = plaintext
        if (plaintext != ""):
            self.plaintext = self.normalizeText(plaintext)

        ciphertext = ciphertext.lower()
        self.ciphertext = ciphertext
        if (ciphertext != ""):
            self.ciphertext = self.normalizeText(ciphertext)
        
        
        b = b % 26
        self.b = b
        
        m = m % 26
        if (not relativePrime(m,26)):
            raise Exception("m must be relative prime with 26")
        self.m = m

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
        for p in self.plaintext:
            ciphertext = ciphertext + alphabets[(alphabets.find(p)*self.m + self.b)%26]
        
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
        modInverse = modularInverse(self.m, 26)
        for c in self.ciphertext:
            plaintext = plaintext + alphabets[(modInverse*(alphabets.find(c)-self.b))%26]
        
        self.plaintext = plaintext
        return plaintext


# # Test for Affine.
# a = "kripto"
# b = 10
# m = 7
# x = "CZOLNE"
# d = AffineCipher(b=b, m=m, plaintext=a, ciphertext="")
# print(d.encrypt())