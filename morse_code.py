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

        operation = {1: morse_dict, 2: list(morse_dict.keys())}
        if option == 1:
            return operation[option][val]
        else:
            return operation[option][list(morse_dict.values()).index(val)]

    # Function to encrypt given message
    def encrypt(self):

        return "".join(['/ ' if character == ' '
                        else f'{self.getDictItems(character, 1)} '
                        for character in self.message])

    # Function to decrypt given cipher text
    def decrypt(self):

        return "".join([' ' if character == '/'
                        else f'{self.getDictItems(character, 2)}'
                        for character in self.message.split(' ')])


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
