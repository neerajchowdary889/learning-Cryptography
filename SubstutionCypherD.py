A = "@"
B = "&"
C = "$"
D = "~"
inp = int(input("Input the Number:\n"
            "1 --> Encrypt\n"
            "2 --> Decrypt\n"))

class Encryption:
    def conversion(self):
        text = input("Input the Text: ")
        text1 = text.upper()
        text2 = list(text1)
        print("Input String is: ", text1)
        i = 0
        i1 = 0
        while i < len(text2):
            j = text2[i]
            if (text2[i] == 'A'):
                text2[i] = j.replace("A", A)
            if (text2[i] == 'B'):
                text2[i] = j.replace("B", B)
            if (text2[i] == 'C'):
                text2[i] = j.replace("C", C)
            if (text2[i] == "D"):
                text2[i] = j.replace("D", D)
            i = i + 1
        print("Cypher text is: ", end="")
        while i1 < len(text2):
            print(text2[i1], end="")
            i1 = i1 + 1

class Decryption(Encryption):
    def decryption(self):
        z = 0
        z1 = 0
        text3 = text2
        while z < len(text2):
            j = text3[z]
            if (text3[z] == '@'):
                text3[z] = j.replace("@", A)
            if (text3[z] == '&'):
                text3[z] = j.replace("&", B)
            if (text3[z] == '$'):
                text3[z] = j.replace("$", C)
            if (text3[z] == "~"):
                text3[z] = j.replace("~", D)
            z = z + 1
        print("Text is: ", end="")
        while z1 < len(text3):
            print(text3[z1], end="")
            z1 = z1 + 1

if (inp == 1):
    encrypt = Encryption()
    encrypt.conversion()

elif (inp == 2):
    decrypt = Decryption()
    decrypt.decryption()
else:
    print("Wrong Input")