# Converstion of Human Friendly into cyphertext

A = "@"
B = "&"
C = "$"
D = "~"

if __name__ == "__main__":
    def conversion():
        text = input()
        text1 = text.upper()
        text2 = list(text1)
        print("Input String is: ",text1)
        i = 0
        i1 = 0
        while i < len(text2):
            j = text2[i]
            if( text2[i] == 'A'):
                text2[i] = j.replace("A", A)
            if(text2[i] == 'B'):
                text2[i] = j.replace("B", B)
            if(text2[i] == 'C'):
                text2[i] = j.replace("C", C)
            if(text2[i] == "D"):
                text2[i] = j.replace("D", D)
            i = i + 1
        print("Cypher text is: ",end = "")
        while i1 < len(text2):
            print(text2[i1],end="")
            i1 = i1+1
conversion()


