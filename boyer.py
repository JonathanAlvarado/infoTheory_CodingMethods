import random
import sys

def createWord(size):
    word = ''
    for i in range(size):
        letter = chr(random.randint(97,101))
        word+=str(letter)
    return word

def createPattern(size):
    pattern =''
    for i in range(size):
        letter = chr(random.randint(97,101))
        pattern += str(letter)
    return pattern

def boyerMoore(text, pattern):
    '''lenTxt = length of the text
    lenPat = length of the pattern'''
    lenTxt = len(text)
    lenPat = len(pattern)

    #precompute
    bch = badCharacter(text,pattern,lenTxt,lenPat)
    gsuff = goodSuff(pattern,lenPat)
    
    matchesPos = []
    
    j = 0
    comp = 0#comparisons
    while (j <= lenTxt - lenPat):
        i = lenPat-1
        #for i in range(lenTxt-1,-1,-1):
        while True:
            comp +=1
            if i>=0 and pattern[i] == text[i+j]:
                i -= 1
            else:
                break
        if i<0:
            matchesPos.append(j)
            j+= gsuff[0]
        else:
            j += max(gsuff[i], bch[text[i+j]]-lenPat+1+i)
    
    print matchesPos, ' ', comp
    return comp


def badCharacter(text,pattern,t,p):
    '''Dictionary that tells us 
    '''
    badChar = {}
    
    for i in range(t-1):
        if text[i] not in pattern:
            badChar[text[i]] = p

    for j in range(p-1):
        badChar[pattern[j]] = p-j-1
        #badChar.append(p-j-1)
    return badChar

def suffixes(pattern, x):
    a = x - 1
    b = a
    suff = []
    for i in range(x):
        suff.append(0)
    
    suff[x-1] = x
    for i in range(x-2,-1,-1):
        if i > a and suff[i+x-1-b] < i-a:
            suff[i]= suff[i+x-1-b]
        else:
            if i < a:
                a = i
            b = i
            while (a>=0 and pattern[a] == pattern[a+x-1-b]):
                a-=1
            suff[i] = b - a
    return suff
            

def goodSuff(pattern,x):
    gSuff = [] 
    s = suffixes(pattern,x)

    for i in range(x):
        gSuff.append(x)

    for i in range(x-2,-1,-1):
        if (s[i] == i+1):
            for j in range(x-2):#x-1-i):
                if gSuff[j] == x:
                    gSuff[j] = x-1-i

    for i in range(x-1):
        gSuff[x-1-s[i]] = x-1-i

    return gSuff


def main():
    #textSize = int(sys.argv[1])
    #patSize = int(sys.argv[2])
    #text = createWord(textSize)
    #pattern = createPattern(patSize)
    text = sys.argv[1]
    pattern = sys.argv[2]
    boyerMoore(text,pattern)
    #print text.find(pattern)

if __name__ == "__main__":
    main()
