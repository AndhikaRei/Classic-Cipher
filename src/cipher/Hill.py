from Utility import alphabets, modularInverse

class HillCipher:
    """
    A class used for representing Hill Cipher and it's component.

    Attributes.
    ----------
    plaintext : str
        Text you want to encrypt or ciphertext after decrypted. In lowercase format.
    ciphertext : str
        Text you want to decrypt or plaintext after encrypted. In lowercase format.
    m : list of int
        Key for encrypting or decrypting a text.
    """

    def __init__(self, m:list, plaintext: str ="", ciphertext:str="") -> None:
        """
        Constructor for HillCipher class. Either plaintext or ciphertext must be empty at 
        creation.

        Parameters
        ----------
        plaintext : str, optional
            Text you want to decrypt or plaintext after encrypted.
        cipherthex : int, optional
            Key for encrypting or decrypting a text.
        m : list of int
            Key for encrypting or decrypting a text.
        """

        # Input validation.
        if (plaintext != "" and ciphertext != ""):
            raise Exception("Either plaintext or ciphertext must be empty")
        if (plaintext == "" and ciphertext == ""):
            raise Exception("Either plaintext or ciphertext must be filled")
        if (m == None):
            raise Exception("Key must be filled!")

        self.plaintext = plaintext
        if (plaintext != ""):
            self.plaintext = self.normalizeText(plaintext)

        ciphertext = ciphertext.lower()
        self.ciphertext = ciphertext
        if (ciphertext != ""):
            self.ciphertext = self.normalizeText(ciphertext)
        
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
        ordo = (len(self.m))**0.5
        for i in range (0, len(self.plaintext), 3):

            # Find value of p1 p2 p3
            p1 = alphabets.find(self.plaintext[i])
            p2 = alphabets.find(self.plaintext[i+1])
            p3 = alphabets.find(self.plaintext[i+2])

            # Find it's corresponding cipher value
            ciphertext += alphabets[((self.m[0]*p1 + self.m[1]*p2 + self.m[2]*p3)%26)]
            ciphertext += alphabets[((self.m[3]*p1 + self.m[4]*p2 + self.m[5]*p3)%26)]
            ciphertext += alphabets[((self.m[6]*p1 + self.m[7]*p2 + self.m[8]*p3)%26)]
        
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


# Test for Hill.
a = "kripto"
b = 10
m = 7
x = "CZOLNE"
d = HillCipher(m=m, plaintext="", ciphertext=x)
print(d.decrypt())