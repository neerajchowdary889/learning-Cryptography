import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H'
    ,'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
message = input("Enter the message to Encrypt: ")
message = message.lower()
message = list(message)
n = len(message)
msgtemp = []
for z in range(n):
    msgtemp.append(alphabets.index(message[z]))
key = []
keytemp = []
for i in range(n*n):
    i1 = random.randint(0,9)
    key.append(alphabets[i1])
for j in range(len(key)):
    keytemp.append(alphabets.index(key[j]))
keyMatrix = [[0] * 3 for i in range(n)]
k = 0
for i2 in range(n):
    for j2 in range(n):
        keyMatrix[i2][j2] = keytemp[k]
        k += 1
print("Message matrix :\n",msgtemp)
print("Key matrix :\n", keyMatrix)
selftemp = [[0] * 3 for i in range(n)]
class Encrypt():
    def encrypt(self):
        self.temp = []
        for i in range(n):
            z2 = 0
            for j in range(n):
                selftemp[i][j]=((keyMatrix[i][j]*msgtemp[z2]))
                z2 = z2+1
        self.rows = len(selftemp)
        self.cols = len(selftemp[0])
        self.Matrix = []
        for i in range(0, self.rows):
            sumRow = 0;
            for j in range(0, self.cols):
                sumRow = sumRow + selftemp[i][j];
            self.Matrix.append(sumRow%26)
        print("selftemp matrix: \n",selftemp)
        print("sumrow is:\n",self.Matrix)
Encryption = Encrypt()
Encryption.encrypt()
