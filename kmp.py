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

def kmp(text,pattern):
    m = len(text)
    n = len(pattern)

    matchesPos = []
    match = 0
    pos = 0#current position in text
    comp = 0 #comparisons

    while pos < m:
        skips = 0
        #if length of pattern is greater than the rest of the text the function finishes
        if n > len( text[pos:m] ):
            return len(matchesPos)

        for i in range(n):
            if i+pos < m:
                comp += 1
                if text[i+pos] == pattern[i]:
                    match+=1
                    skips +=1
                else:
                    break
        
        if skips > 0:
            pos += skips
        else:
            pos += 1

        if skips == n:
            matchesPos.append(match)
            
    return comp#len(matchesPos)
    


def main():
    #textSize = int(sys.argv[1])                                              
    #patSize = int(sys.argv[2])                                                
    #text = createWord(textSize)
 #pattern = createPattern(patSize)                                           
    text = sys.argv[1]
    pattern = sys.argv[2]
    kmp(text,pattern)
    #print text.find(pattern)                                             

if __name__ == "__main__":
    main()
        
