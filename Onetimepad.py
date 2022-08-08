import random
import string
import onetimepad
str = input("Enter Plaintext to Encrypt: ")
i = 0
key = ''.join([random.choice(string.ascii_letters) for i in range(len(str))])
print(str, key)
Ciphertext = onetimepad.encrypt(str, key)
<<<<<<< HEAD
print("Ciphertext is: \n"+Ciphertext)
plaintext = onetimepad.decrypt(Ciphertext, key)
print("Plaintext is: \n"+plaintext)
=======
print("Ciphertext is "+Ciphertext)
plaintext = onetimepad.decrypt(Ciphertext, key)
print("Plaintext is "+plaintext)
>>>>>>> origin/master

