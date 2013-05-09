import numpy
import random
import sys

def createMessage(length):
    msg = []
    for i in range(length):
        letter = random.choice([0,1])
        msg.append(letter)
    return numpy.array(msg, dtype = int)

def encode(m, g):
    enc = numpy.dot(m, g)%2
    return enc

def decode(m, h):
    dec = numpy.dot(h, m)%2
    return dec

def noise(m, error):
    noisy = numpy.copy(m)
    bit = 0
    for i in range(len(noisy)):
        e = random.random()
        if e <= error:
            if noisy[i] == 0:
                noisy[i] = 1
                bit +=1
            else:
                noisy[i] = 0
                bit +=1
            if bit ==1:
                break
    return noisy

def findError(m, noisy):
    n = ''
    for i in range(len(m)):
        n += str(m[i])
    n = n[::-1]
    n = int(n,2)
    if n > 0:
        if noisy[n] == 0:
            noisy[n] = 1
        else: #noisy[n] == 1:
            noisy[n] = 0
    return noisy

def hamming(length, n, error):
    g =  numpy.array([[1, 0, 0, 0, 0, 1, 1],[0, 1, 0, 0, 1, 0, 1],[0, 0, 1, 0, 1, 1, 0],[0, 0, 0, 1, 1, 1, 1]])
    h = numpy.array([[0, 0, 0, 1, 1, 1, 1],[0, 1, 1, 0, 0, 1, 1],[1, 0, 1, 0, 1, 0, 1],])
    corrected = 0
    uncorrected = 0
    for i in range(n):
        msg = createMessage(length)
        enc = encode(msg, g)
        #print "original message: ", msg
        #print "encoded msg: ", enc
        noisy = noise(enc, error)
        #print 'noisy mesage: ', noisy
        dec = decode(noisy, h)
        #print 'decoded msg: ', dec
        noError = findError(dec, noisy)
        #print 'no error: ', noError
        if (enc==noError).all():
            corrected+=1
        else:
            uncorrected+=1
        
        
if __name__ == '__main__':
    
    length = int(raw_input('bits length: '))#int(sys.argv[1])
    n = int(raw_input('Repetitions: '))#int(sys.argv[2])
    error = float(raw_input('Error percentage: '))
    
    hamming(length,n,error)
