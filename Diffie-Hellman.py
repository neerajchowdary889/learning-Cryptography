import multiprocessing as mp
import random

a = random.randint(1,10000)
b = random.randint(1,10000)
g = random.randint(1,100000)
n = random.randint(1,100000)
# print(f"a = {a}\nb = {b}")
print(f"g = {g}\nn = {n}\ng,n publicly known values")
temp = []

def finding_x():
    x = (((g)**(a))%n)
    temp.append(x)
def finding_y():
    y = (((g)**(b))%n)
    temp.append(y)

class keyFinding:
    def __init__(self):
        self.Sa = 0
        self.Sb = 0
    def finding_Sa(self,y):
        self.Sa = (((y)**(a))%n)
        # print(f"Sa is {self.Sa}")
    def finding_Sb(self,x):
        self.Sb = (((x)**(b))%n)
        # print(f"Sb is {self.Sb}")
    def Key(self):
        if(self.Sa == self.Sb):
            print(True)
            print(f"Both Side users now have the common key which is {self.Sa}")
        else:
            raise Exception("Something went wrong...")

if __name__ == '__main__':
    p1 = mp.Process(target=finding_x())
    p2 = mp.Process(target=finding_y())
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"x = {temp[0]}\ny = {temp[1]}")

    key = keyFinding()
    p3 = mp.Process(target=key.finding_Sa(temp[1]))
    p4 = mp.Process(target=key.finding_Sb(temp[0]))
    p3.start()
    p4.start()
    p3.join()
    p4.join()
    key.Key()

"""This is the Implementation of Diffie-Hellman key exchange at last after computation both send and receiver has 
the same key(for Symmetric Encryption)... Uncomment to see the clear implementation of Diffie-Hellman key exchange..."""