def plaintocipher():
    cipher=''
    plain=input("Enter your plain text:")
    key=int(input("Enter your key:"))
    for i in plain:
        j=ord(i)
        if i.islower():
            k=(j+key-97)%26+97
        else:
            k=(j+key-65)%26+65
        l=chr(k)
        cipher+=l
    print(f"Cipher text is: {cipher}")    
    
def ciphertoplain():
    cipher=''
    plain=input("Enter your cipher text:")
    key=int(input("Enter your key:"))
    for i in plain:
        j=ord(i)
        if i.islower():
            k=(j-key-97)%26+97
        else:
            k=(j-key-65)%26+65
        l=chr(k)
        cipher+=l
    print(f"Plain text is: {cipher}")    
    
def bruteforce():
    cipher=''
    plain=input("Enter your cipher text:")
    l1=[]
    for ii in range(26):
        cipher=''
        for i in plain:
            j=ord(i)
            if i.islower():
                k=(j-ii-97)%26+97
            else:
                k=(j-ii-65)%26+65
            l=chr(k)
            cipher+=l
        l1.append(cipher)
    print(*l1)        

def alphanumerical():
    word={'a':'!', 'b':'@', 'c':'#', 'd':'$', 'e':'%', 'f':'^', 'g':'&', 'h':'*', 'g':'(', 'h':')', 'i':'-', 'j':'_', 'k':'+', 'l':'=', 'm':'|', 'n':'/', 'o':'?', 'p':'>', 'q':'<', 'r':',', 's':'.', 't':'`', 'u':'~', 'v':'♩', 'w':'∫', 'x':'∆', 'y':'⌗', 'z':'▮', ' ':'⅖', 'A':'␁', 'B':'⍅', 'C':'⌾', 'D':'⌿', 'E':'⍃', 'F':'⍉', 'G':'⍊', 'H':'⍋', 'I':'⍎', 'J':'⍟', 'K':'⍳', 'L':'⍴', 'M':'▌', 'N':'▢', 'O':'▭', 'P':'⊞', 'Q':'〓', 'R':'☗', 'S':'◭', 'T':'◮', 'U':'✹', 'V':'⋖', 'W':'◞', 'X':'⊖', 'Y':'Σ', 'Z':'❀'}
    def encryption(): 
        a=input("Enter the Plain Text: ")
        cipher=''
        for i in a:
            ch=word[i]
            cipher+=ch
        print(f'the cipher text is : {cipher}')
        
    def decryption():
        a=input("Enter the cipher Text: ")
        plain=''
        for i in a:
            ch=list(word.keys())[list(word.values()).index(i)]
            plain+=ch
        print(f'the plain text is : {plain}')
        
    print(' press:1 for Encryption \n press:2 for decryption \n press:3 to exit to main menu')
    b=int(input('Enter your choice: '))
    while b!=3:
        if b==1:
            encryption()
        elif b==2:
            decryption()
        else:
            continue
        print(' press:1 for Encryption \n press:2 for decryption \n press:3 to exit to main menu')
        b=int(input('Enter your choice: '))
          



print(" press:1 for encryption \n press:2 for decryption \n press:3 for bruteforce \n press:4 for monoalphabetic \n press:5 to exit ")
a=int(input("Enter your choice: "))
while a!=5:
    if a==1:
        plaintocipher()
    elif a==2:
        ciphertoplain()
    elif a==3:
        bruteforce()
    elif a==4:
        alphanumerical()
    else:
        continue
    print(" press:1 for encryption \n press:2 for decryption \n press:3 for bruteforce \n press:4 for monoalphabetic \n press:5 to exit ")
    a=int(input("Enter your choice: "))
    