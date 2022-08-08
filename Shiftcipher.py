import time
message = input("Enter the message to encrypt: ")
shift = int(input("Enter int to shift: "))
start = time.time()
class encrypt():
    message = list(message)
    def __init__(self):
        self.temp = []
        self.temp2=[]
    def encryption(self):
        for i in range(len(message)):
            temparary = ord(message[i]) + shift
            self.temp.append(ord(message[i]) + shift)
            self.temp2.append(chr(temparary))
        Ciphertext = ''.join(map(str, self.temp2))
        print("Ciphertext : \n",Ciphertext)
class decrypt(encrypt):
    def decryption(self):
        temp2 = []
        for j in range(len(self.temp)):
            temp2.append(chr(self.temp[j]-shift))
        Plaintext = ''.join(map(str, temp2))
        print("Plaintext : \n",Plaintext)
Decrypt = decrypt()
Decrypt.encryption()
Decrypt.decryption()
end = time.time()
print(end - start)