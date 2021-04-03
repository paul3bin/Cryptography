'''
Python code for Vigenere Cipher
'''


class VigenereCipher:

    # Initialization funtion
    def __init__(self, text, key):
        # converting key and text to uppercase and removing spaces from them.
        self.text = "".join(text.upper().split(' '))
        self.key = "".join(key.upper().split(' '))

    # Function that encrypts the given plain text using given key.
    def encrypt(self):
        cipher_text, j = [], 0
        for i in range(len(self.text)):
            if j > len(self.key)-1:
                j = 0
            character = (
                (ord(self.text[i])+ord(self.key[j])) % 26)+ord('A')
            j += 1

            cipher_text.append(chr(character))
        return ''.join(cipher_text)

    # Function that decrypts the given plain text using given key.
    def decrypt(self):
        plain_text, j = [], 0
        for i in range(len(self.text)):
            if j > len(self.key)-1:
                j = 0
            character = (
                (ord(self.text[i])-ord(self.key[j])+26) % 26)+ord('A')
            plain_text.append(chr(character))
            j += 1

        return ''.join(plain_text)


if __name__ == '__main__':
    print('\n----------------------Vigenere Cipher----------------------')
    text = input('Enter text or phrase: ')
    key = input(
        'Enter key(Note: The key should be less than the text you entered above and the key should be a text or phrase): ')
    print('\n1. Encrypt a text.\n2. Decrypt a text.\n')
    option = int(input('Option...(1/2): '))
    cipherObj = VigenereCipher(text, key)

    if option == 1:
        print(f'Enrypted text: {cipherObj.encrypt()}')
    elif option == 2:
        print(f'Decrypted text: {cipherObj.decrypt()}')
    else:
        print('Wrong option. Try again.')
