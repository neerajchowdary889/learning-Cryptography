import base64

Message = input("Enter Message to Encrypt: ")

class Encryption():
    def Encrypt(self):
        self.Encrypt = base64.b64encode(bytes(Message, encoding = "utf8"))
        print(self.Encrypt)
class Decryption(Encryption):
    def Decrypt(self):
        self.Decrypt = base64.b64decode(self.Encrypt)
        print(self.Decrypt)

encrypt = Decryption()
encrypt.Encrypt()
encrypt.Decrypt()
