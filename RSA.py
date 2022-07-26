import sympy
import math
import random
Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349,
353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E'
    ,'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

def primenumber():
    p = sympy.randprime(2, 1000)
    q = sympy.randprime(2, 1000)
    N = p * q
    return p, q, N
p,q,N = primenumber()
# print(f"p,q is  {p},{q}")
# print(f"N is  {N}")
list = []
phiN = (p-1)*(q-1)
def coprime():
    b = N
    a = Primes[random.randint(0, 167)]
    coprimes = math.gcd(b, a)
    coprimes2 = math.gcd(a,phiN)
    if coprimes == 1 and a < phiN and coprimes2 == 1:
        list.append(a)
        list.append(b)
    else:
        coprime()
coprime()
e = list[0]
N = list[1]
#print(f"Encryption key is ({e},{N})")
# ---------------------------------------------------------------------
message = input("Type out Message to Encrypt: ")
indexMessage = []
for i in range(len(message)):
    indexMessage.append(alphabets.index(message[i]))
# print(indexMessage)
class Encryption():
    def __init__(self):
        self.Encrypt = []
    def Encrypty(self):
        for i in range(len(indexMessage)):
            self.Encrypt.append(((indexMessage[i])**(e))%N)
        # print(f"self.Encrypt: {self.Encrypt}")
# ---------------------------------------------------------------------
def decrypt(D):
    decryptemp = (D * e) % phiN
    while (decryptemp != 1):
        D = D + 1
        decryptemp = (D * e) % phiN
    list.append(D)
decrypt(1)
D = list[2]
# print(f"D is {D}")
# ---------------------------------------------------------------------
class Decryption(Encryption):
    def Decrypt(self):
        self.Decryptt = []
        self.DecryptTemp = []
        for z in range(len(self.Encrypt)):
            self.DecryptTemp.append(((self.Encrypt[z])**(D))%N)
        # print(f"self.DecryptTemp: {self.DecryptTemp}")
        for j in range(len(self.DecryptTemp)):
            self.Decryptt.append(alphabets[self.DecryptTemp[j]])
        self.Decryptt = ''.join(map(str,self.Decryptt))
        print(self.Decryptt)
Decrypty = Decryption()
Decrypty.Encrypty()
dec = int(input("Press '0' to decrypt: "))
if dec == 0:
    Decrypty.Decrypt()
else:
    raise Exception("Use right key to decrypt...")


"""This is RSA Cipher implementation, remove comments to see the clear view of the implementation i did.
if you want to encrypt only lower and upper letters and this algo is much faster because no need of bigger calculations."""