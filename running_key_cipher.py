'''
Python code for running key cipher
'''

from pandas import DataFrame

# function for running key cipher


class RunningKeyCipher:

    def __init__(self, plainText, key):
    # converting the plain text and key to upper case
        self.pt = list(plainText.upper())
        self.ky = list(key.upper())

        # removing spaces in key and plain text
        for char in self.ky:
            if char == ' ':
                self.ky.remove(char)
        for char in self.pt:
            if char == ' ':
                self.pt.remove(char)

        # creating a DataFrame of size 26x26
        tab, tableau = [chr(a) for a in range(65, 91)], []
        for i in range(26):
            a = tab[i:]+tab[:i]
            tableau.append(a)
        self.tabulaRecta = DataFrame(tableau, index=tab, columns=tab)

    def encrypt(self):
        encryptedText = ''
        for i in range(len(self.pt)):
            encryptedText += self.tabulaRecta.values[ord(self.pt[i])-65][ord(self.ky[i])-65]
        return encryptedText
    
    def decrypt(self):
        decryptedText = ''
        for i in range(len(self.pt)):
            decryptedText += ''.join(
                self.tabulaRecta[self.tabulaRecta[self.ky[i]] == self.pt[i]].index.values)
        return decryptedText


if __name__ == '__main__':
    text = input('Text : ')
    key = input('Key : ')
    if len(text) > len(key):
        print('Length of key should be >= text!')
    else:
        code = int(input('Enter 1 to encrypt or 0 to decrypt : ') )
        if  code == 1:
            print(RunningKeyCipher(text, key).encrypt())
        elif code == 0:
            print(RunningKeyCipher(text, key).decrypt())
        else:
            print('WRONG OPTION!')
