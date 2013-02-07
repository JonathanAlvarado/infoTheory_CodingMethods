import random
from sys import argv

def readFile(f):
    '''lee archivo con probabilidades '''
    file = open(f, 'r')
    data = []
    for line in file.readlines():
        if '//' not in line:
            p,q01,q10 = line.split(",")
            data.append((float(p), float(q01), float(q10)))
    #print data
    file.close()
    return data

def binary(p,n):
    ''''crea palabras binarias aleatoriamente '''
    word=""
    for i in range(n):
        rand = random.uniform(-1.0,1.0)
        if rand >= 0 and rand < p:
            word += "0"
        else:
            word += "1"
    print word
    return word
    
def simulation(f):
    probs = readFile(f)
    
    for x in range(len(probs)):
        p, q11, q21 = probs[x]
        for y in range(30):
            word = binary(p,y)

if __name__ == "__main__":
    simulation(argv[1])
