alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
message = input("Enter the message to Encrypt: ")
message = message.lower()
message = list(message)
key = []
a = 3
b = 20
print(a,b)
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
        encrypttemp = 0
        for i in range(len(message)):
            encrypttemp = (((a)*(temp[i])+(b))%26)
            self.temp.append(encrypttemp)
            self.Encrypt.append(alphabets[self.temp[i]])
        self.Encrypt = ''.join(map(str,self.Encrypt))
        print(f"Ciphertext : {self.Encrypt}")
# def gcd(x, y):
#     if (x == 0):
#         return y
#     return gcd(y % x, x)
# def gcd(x, y):
#     for x in range(1, y):
#         if (((x % y) * (x % y)) % y == 1):
#             return x
#     return -1
# def phi(n):
#     result = 1
#     for i in range(2, n):
#         if (gcd(i, n) == 1):
#             result+=1
#     return result
# n = a
def modInverse(a, m):

    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
n = modInverse(a,26)

class decrypt(encrypt):
    def Decryption(self):
        self.temp2 = []
        self.decrypt = []
        self.decrypt1 = []
        self.Encrypt = list(self.Encrypt)
        j = 0
        for j in range(len(self.Encrypt)):
            self.temp2.append(alphabets.index(self.Encrypt[j]))
        for v in range(len(self.temp2)):
            decryption = (((self.temp2[v]-b)*(n))%26)
            self.decrypt.append(decryption)
        for k in range(len(self.decrypt)):
            self.decrypt1.append(alphabets[self.decrypt[k]])
        self.decrypt1 = ''.join(map(str,self.decrypt1))
        print(self.decrypt1)
Encrypt = decrypt()
Encrypt.Encryption()
Encrypt.Decryption()

""" 'a' value should be in certain range, in only that range this code works, dont know the issue. some calculation mistakes..."""
""" NOT PERFECT.... """