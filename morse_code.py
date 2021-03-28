'''
Python code for encryption and decryption of a message using morse code
'''


class MorseCode:

    def __init__(self, message) -> None:
        self.message = message.upper()

    # Function that returns value or key from morse_dict dictionary
    def getDictItems(self, val, option):
        morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..',
                      '0': '-----', '1': '.----', '2': '..--', '3': '...--', '4': '....-',
                      '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                      '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.',
                      '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
                      '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '$': '...-..-', '@': '.--.-.'}
        if option == 1:
            return morse_dict[val]

        elif option == 2:
            for key, value in morse_dict.items():
                if val == value:
                    return key

    # Function to encrypt given message
    def encrypt(self):
        cipherText = ''
        for character in self.message:
            if character == ' ':
                cipherText += '/ '
            else:
                cipherText += self.getDictItems(character, 1)
                cipherText += ' '
        return cipherText[:-1]

    # Function to decrypt given cipher text
    def decrypt(self):
        plainText = ''
        characterList = self.message.split(' ')
        for character in characterList:
            if character == '/':
                plainText += ' '
            else:
                plainText += self.getDictItems(character, 2)
        return plainText


if __name__ == '__main__':
    print('\n--------------------Morse Code--------------------')
    text = str(input('Enter message: '))
    morseObj = MorseCode(text)
    print('\n1. Encrypt.\n2. Decrypt.')
    option = int(input('Option: '))
    if option == 1:
        print(morseObj.encrypt())
    elif option == 2:
        print(morseObj.decrypt())
    else:
        print('Wrong option. Try again.')
