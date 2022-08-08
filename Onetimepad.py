import random
import string
import onetimepad
str = input("Enter Plaintext to Encrypt: ")
i = 0
key = ''.join([random.choice(string.ascii_letters) for i in range(len(str))])
Ciphertext = onetimepad.encrypt(str, key)
print("Ciphertext is: \n"+Ciphertext)
plaintext = onetimepad.decrypt(Ciphertext, key)
print("Plaintext is: \n"+plaintext)


