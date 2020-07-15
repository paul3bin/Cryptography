'''
Python code for running key cipher
'''

from pandas import DataFrame

#function for running key cipher        
def Running_Key_Cipher(plainText,key,code):
    #converting the plain text and key to upper case
    pt = list(plainText.upper())
    ky = list(key.upper())

    #removing spaces in key and plain text
    for char in ky:
        if char==' ':
            ky.remove(char)
    for char in pt:
        if char==' ':
            pt.remove(char)
    
    #creating a DataFrame of size 26x26
    tab,tableau = [chr(a) for a in range(65,91)],[]
    for i in range(26):
        a = tab[i:]+tab[:i]
        tableau.append(a) 
    tabulaRecta = DataFrame(tableau,index = [chr(a) for a in range(65,91)],columns=[chr(a) for a in range(65,91)])

    #code encryption
    if code:
        encryptedText = ''
        for i in range(len(pt)):
            encryptedText+=tabulaRecta.values[ord(pt[i])-65][ord(ky[i])-65]
        return encryptedText
    
    #code decryption
    else:
        decryptedText=''
        for i in range(len(pt)):
            decryptedText+=''.join(tabulaRecta[tabulaRecta[ky[i]]==pt[i]].index.values)
        return decryptedText

code = input('Enter 1 to encrypt or 0 to decrypt : ')
if int(code)==0 or int(code)==1:
    plainText = input('Enter plain text : ')
    key = input('Enter key : ')
    if len(plainText)>len(key):
            print('The length of the key should be greater than or equal to length of plain text.')
    else:
        print(Running_Key_Cipher(plainText,key,int(code)))
else:
    print('WRONG OPTION!')