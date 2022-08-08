import random
message = input("Enter the message to encrypt: ")
blocksize = 6
i = 0
blocks = []
key = []
while i < len(message):
    blocks.append(message[i:i+blocksize])
    i = i+blocksize
print(blocks)
for j in range(len(blocks)):
    key.append(random.randint(1,30))
print(key)
class encrypt():
    def __init__(self):
        self.temp = []
        self.encryptTemp = []
    def convert(self):
        for j in message:
            self.temp.append(ord(j))
        print(self.temp)
    def Encryption(self):
        k = 0
        k1 = 0
        k2 = 0
        while k < len(self.temp):
            self.temp[k] = ((self.temp[k]+key[k1]) for k2 in range(k + blocksize))
            k = k+blocksize
            k2 = k
            k1 = k1+1
        print(self.temp)


encryption = encrypt()
encryption.convert()
encryption.Encryption()



