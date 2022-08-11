
dict ={"a":"1","f":"6","k":"Z","p":"R","u":"C","z":"L","9":"T","0":"J",
       "b":"2","g":"7","l":"A","q":"Y","v":"F","1":"B","8":"U"," ":".",
       "c":"3","h":"8","m":"P","r":"E","w":"X","2":"D","7":"V",
       "d":"4","i":"9","n":"Q","s":"N","x":"G","3":"K","6":"H",
       "e":"5","j":"0","o":"S","t":"O","y":"W","4":"M","5":"I"
}
message = input("Enter String to encrypt: ")
message = list(message)
class Encrypt():
    def __init__(self):
        self.temp = []
        self.Ciphertext = ''
    def Encryption(self):
        for i in range(len(message)):
            word = message[i]
            replace = dict.get(word)
            self.temp.append(replace)
            self.Ciphertext = ''.join(map(str,self.temp))
        print("Ciphertext is : \n",self.Ciphertext)
class Decrypt(Encrypt):
    def Decryption(self):
        self.decrypt = []
        Ciphertext = list(self.Ciphertext)
        for j in range(len(Ciphertext)):
            self.decrypt.append(list(dict.keys())[list(dict.values()).index(Ciphertext[j])])
            decrypt = ''.join(map(str,self.decrypt))
        print("Plaintext is : \n",decrypt)
encrypt = Decrypt()
encrypt.Encryption()
dec = int(input("Press '0' to decrypt: "))
if dec == 0:
    encrypt.Decryption()
else:
    raise Exception("Use right key to decrypt...")