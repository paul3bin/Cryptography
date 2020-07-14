class CaesarCipher:
	def decryption(self,cipherText,key):
		decipheredText = ""
		for ch in cipherText:
			if ch.isalpha():
				newchar = ord(ch)-key
				if newchar<ord('a'):
					newchar+=26
				newShiftedALphabet = chr(newchar)
				decipheredText+=newShiftedALphabet
		print("The plain text is : "+decipheredText)

	def encryption(self,plainText,key):
		cipherText = ""
		for ch in plainText:
			if ch.isalpha():
				alphabetInString = ord(ch) + key
				if alphabetInString > ord('z'):
					alphabetInString-=26
				shiftedAlphabet = chr(alphabetInString)
				cipherText+=shiftedAlphabet
		print("Your encrypted text is :"+cipherText)
	
plainText = input("Enter your plain text : ")
key = int(input("Enter shift value(integer) : "))
print("\n1. Encrypt this text\n2. Decrypt this text")
optionInput = int(input("Option: "))
cipherobj = CaesarCipher()
if optionInput==1:
	cipherobj.encryption(plainText,key)
elif optionInput==2:
	cipherobj.decryption(plainText,key)
else:
	print('Invalid option.')