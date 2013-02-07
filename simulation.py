import random
from sys import argv

def readFile(f):
    file = open(f, 'r')
    data = []
    for line in file.readlines():
        if '//' not in line:
            p,q01,q10 = line.split(" ")
            data.append((float(p), float(q01), float(q10)))
    #print data
    file.close()
    return data

def binary():
    word=""
    
if __name__ == "__main__":
    readFile(argv[1])
