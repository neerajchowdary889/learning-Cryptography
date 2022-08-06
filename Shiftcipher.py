import time
message = input("Enter the message to encrypt: ")
shift = int(input("Enter int to shift: "))
class encrypt():
    message = list(message)
    def __init__(self):
        self.temp = []
    def encryption(self):
        for i in range(len(message)):
            self.temp.append(ord(message[i]) + shift)
        Ciphertext = ''.join(map(str, self.temp))
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