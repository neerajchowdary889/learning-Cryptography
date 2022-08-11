import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
message = input("Enter the message to Encrypt: ")
message = message.lower()
message = list(message)
key = []
def Keygeneration():
    x1 = 0
    while x1 < 2:
        key.append(random.randint(1,9))
        x1 = x1+1
Keygeneration()
a = int(key[0])
b = int(key[1])
temp = []
for j in range(len(message)):
    temp.append(alphabets.index(message[j]))
temp = list(map(int, temp))
# E(c) = (a(c)+b)%26  c --> Ciphertext
class encrypt():
    def __init__(self):
        self.temp = []
        self.Encrypt = []
    def Encryption(self):
        for i in range(len(message)):
            self.temp.append((a*(temp[i])+b)%26)
            self.Encrypt.append(alphabets[self.temp[i]])
        self.Encrypt = ''.join(map(str,self.Encrypt))
        print(self.Encrypt)
def gcd(x, y):
    if (x == 0):
        return y
    return gcd(y % x, x)
def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result
n = a
# print(phi(n))
class decrypt(encrypt):
    def Decryption(self):
        self.temp2 = []
        self.decrypt = []
        self.decrypt1 = []
        self.Encrypt = list(self.Encrypt)
        j = 0
        for j in range(len(self.Encrypt)):
            self.temp2.append(alphabets.index(self.Encrypt[j]))
            print(self.temp2)
        print(self.temp2)
        for v in range(len(self.temp2)):
            decryption = (((self.temp2[v]-b)*(phi(n)))%26)
            self.decrypt.append(decryption)
            print(self.decrypt)
        for k in range(len(self.decrypt)):
            self.decrypt1.append(alphabets[self.decrypt[k]])
        self.decrypt1 = ''.join(map(str,self.decrypt1))
        print(self.decrypt1)
Encrypt = decrypt()
Encrypt.Encryption()
Encrypt.Decryption()
