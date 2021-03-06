import random
from Utility import alphabets, modularInverse, relativePrime

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
        if (not relativePrime(self.determinantMatrix(m), 26)):
            raise Exception("matrix determinant must be relative prime with 26, eg (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25).)")

        self.plaintext = plaintext
        if (plaintext != ""):
            self.plaintext = self.normalizeText(plaintext)

        self.ciphertext = ciphertext
        if (ciphertext != ""):
            self.ciphertext = self.normalizeText(ciphertext)
        
        self.m = m

    @staticmethod
    def generateBasicHillTable()->str:
        """
        Method to generate normal Hill Cipher encrypt table.
        
        Return the List of string representing normal ill Cipher encrypt table. 
        """

        # Variable declaration.
        basicHillTable:list = []
        templist:list = []
        num:int

        # Loop to create Playfair Cipher table.
        for i in range(9):

            # Generate random int
            num = random.randint(0, 25)
            templist.append(num)

            # Add new int to table
            if (i % 3 == 2):
                basicHillTable.append(templist)
                templist = []
        
        return basicHillTable

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
        tail:int
        
        # Remove number, punctuation, and space.
        normalizedText = "".join(filter(str.isalpha, text)).lower()

        # Add dummy "x" char
        tail = len(normalizedText) % 3
        if (tail != 0):
            normalizedText += "x" * (3-tail)
            
        return normalizedText  
    
    @staticmethod
    def determinantMatrix(m)->int:
        """
        Method to find matrix determinant.
        
        Return the determinant (mod 26). 
        """

        # Variable declaration.
        det:int = 0
        minor = [[0 for i in range (3)] for j in range (3)]

        # Find minor entry matrix.
        for i in range (3):
            for j in range(3):
                minor[i][j] = (m[(i+1)%3][(j+1)%3] * m[(i+2)%3][(j+2)%3] - m[(i+1)%3][(j+2)%3] * m[(i+2)%3][(j+1)%3])
        
        # Find determinant.
        for i in range (3):
            det += m[0][i]*minor[0][i]
        
        # Find modular inverse determinant.
        det %= 26

        return det

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
        for i in range (0, len(self.plaintext), 3):

            # Find value of p1 p2 p3
            p1 = alphabets.find(self.plaintext[i])
            p2 = alphabets.find(self.plaintext[i+1])
            p3 = alphabets.find(self.plaintext[i+2])

            # Find it's corresponding cipher value
            ciphertext += alphabets[((self.m[0][0]*p1 + self.m[0][1]*p2 + self.m[0][2]*p3)%26)]
            ciphertext += alphabets[((self.m[1][0]*p1 + self.m[1][1]*p2 + self.m[1][2]*p3)%26)]
            ciphertext += alphabets[((self.m[2][0]*p1 + self.m[2][1]*p2 + self.m[2][2]*p3)%26)]
        
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
        minor = [[0 for i in range (3)] for j in range (3)]
        mInverse = [[0 for i in range (3)] for j in range (3)]
        det:int = 0

        # Find minor entry matrix.
        for i in range (3):
            for j in range(3):
                minor[i][j] = (self.m[(i+1)%3][(j+1)%3] * self.m[(i+2)%3][(j+2)%3] - self.m[(i+1)%3][(j+2)%3] * self.m[(i+2)%3][(j+1)%3])
        
        # Find determinant.
        for i in range (3):
            det += self.m[0][i]*minor[0][i]
        
        # Find modular inverse determinant.
        det %= 26
        detInverse = modularInverse(det, 26)
        print(detInverse)

        # Find modular inverse matrix
        for i in range (3):
            for j in range(3):
                mInverse[j][i] = ((minor[i][j]%26) * detInverse) % 26

        # Decrypt the ciphertext.
        for i in range (0, len(self.ciphertext), 3):

            # Find value of c1 c2 c3
            c1 = alphabets.find(self.ciphertext[i])
            c2 = alphabets.find(self.ciphertext[i+1])
            c3 = alphabets.find(self.ciphertext[i+2])

            # Find it's corresponding plain value
            plaintext += alphabets[((mInverse[0][0]*c1 + mInverse[0][1]*c2 + mInverse[0][2]*c3)%26)]
            plaintext += alphabets[((mInverse[1][0]*c1 + mInverse[1][1]*c2 + mInverse[1][2]*c3)%26)]
            plaintext += alphabets[((mInverse[2][0]*c1 + mInverse[2][1]*c2 + mInverse[2][2]*c3)%26)]
        
        self.plaintext = plaintext
        return plaintext


# Test for Hill.
# a = "paymoremoney"
# b = "JWJNMLSEQPIB"
# m = [[1,2,8],[6,4,4],[2,8,9]]
# d = HillCipher(m=m, plaintext="", ciphertext=b)
# print(d.decrypt())