'''
Python code for ROT13 algorithm.
'''


class ROT13:

    def __init__(self, text: str):
        # removing spaces from the text
        self.text = "".join(text.upper().split(' '))

    def encrypt(self):

        return "".join([chr(ord(alphabet)-13) if ord(alphabet) > ord('A')+12
                        else chr(ord(alphabet)+13) for alphabet in self.text])

    def decrypt(self):

        return "".join([chr(ord(alphabet)-13) if ord(alphabet) > ord('A')+12
                        else chr(ord(alphabet)+13) for alphabet in self.text])


if __name__ == '__main__':
    print(ROT13('SHA').encrypt())
    print(ROT13('FUN').decrypt())
