import string
import random
ran = input("Enter Plaintext to Encrypt: ")
str1 = list(ran)
i = 0
ranKey = ''.join([random.choice(string.ascii_letters) for i in range(len(str1))])
key = list(ranKey)
Liststr = []
ListKey = []
ListAll = []
ListCiphertext = []
n = 0
j = 0
while n < len(str1):
    Liststr.append(ord(str1[n]))
    n = n+1
while j < len(key):
    ListKey.append(ord(key[j]))
    j = j+1
# print(Liststr)
# print(ListKey)
def ciphertext():
    for k in range(len(Liststr)):
        XOR = Liststr[k]+ListKey[k]
        ListAll.append(XOR)
        ListCiphertext.append(chr(ListAll[k]))
    # print(ListAll)
    # print(ListCiphertext)

ciphertext()
Ciphertext = ''.join(map(str, ListCiphertext))
print("Ciphertext is : \n"+Ciphertext)
print("-----------------------------------> Encryption done")
# -----------------------------------> Encryption done
def Decryption():
    temp = []
    temp2 = []
    for z in range(len(ListCiphertext)):
        deXOR = ListAll[z]-ListKey[z]
        temp.append(deXOR)
        temp2.append(chr(temp[z]))
    # print(temp2)
    Plaintext = ''.join(map(str, temp2))
    print("Plaintext is : \n"+Plaintext)

dec = int(input("Press '0' to decrypt: "))
if dec == 0:
    Decryption()
    print("-----------------------------------> Decryption done")
else:
    raise Exception("Use right key to decrypt...")
# -----------------------------------> Decryption done
#Remove comments to see the proper implementation,,, We can make changes even on this code

