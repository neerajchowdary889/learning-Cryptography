"""We are using SHA256 here for password storing."""
import hashlib
import linecache
print("Welcome...")
print("1. NewUser\n2. Login")
inp = int(input("Type your input here: "))
salt = "Neeraj256"
# """ SHA 256 """
# def SHA256(Message):
#     SHA_256 = hashlib.sha3_256(Message.encode())
#     print(f"SHA256:\n{SHA256_hash.hexdigest()}")
class NewUser():
    def register(self):
        print("__NewUser__")
        Username = input("Type your Username: \n>>>")
        HashUsername = hashlib.sha256(Username.encode())
        HashUsername = HashUsername.hexdigest()
        Password = input("Type your Password: \n>>>")
        Password = Password+salt
        HashPassword = hashlib.sha256(Password.encode())
        HashPassword = HashPassword.hexdigest()
        with open("Text.txt", "a") as f:
            f.write(f"Username : {Username}\n>>>Username : {HashUsername}\n>>>Password : {HashPassword}")
            f.write("\n")
            f.close()
        print("Your Credentials added to the file...")
class Login():
    def login(self):
        print("__Login__")
        Username = input("Type your Username: \n>>>")
        HashUsername = hashlib.sha256(Username.encode())
        HashUsername = HashUsername.hexdigest()
        HashUsername = (f">>>Username : {HashUsername}")
        Password = input("Type your Password: \n>>>")
        Password = Password+salt
        HashPassword = hashlib.sha256(Password.encode())
        HashPassword = HashPassword.hexdigest()
        HashPassword = (f">>>Password : {HashPassword}\n")
        with open("Text.txt", "r") as f:
            temp = False
            for index, line in enumerate(f):
                if HashUsername in line:
                    temp = True
                    temmpy = int(index+2)
                    if (temp):
                        con = linecache.getline('Text.txt', temmpy)
                        if (con == HashPassword):
                            print("You Logged in...")
                        else:
                            temp = False
            if(temp == False):
                print("Incorrect Credentials...")

if (inp == 1):
    Register = NewUser()
    Register.register()
elif(inp == 2):
    L = Login()
    L.login()
else:
    raise("Incorrect Entry...........")

"""-> We can make this little bit short and precise but i made a long code for clean text file purpose
   -> We can add change password and stuff but i'm not adding because i made this just for understanding
salt and Hasing, if you want to add some stuff just fork this and push i will see and pull to my code."""