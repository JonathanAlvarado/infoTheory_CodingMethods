import random,sys,math

class Simulation:

    def __init__(self,frequency,length,nTimes,prob0, prob1, fileName):
        self.freq = frequency
        self.probs = ([prob0, 1-prob0],[1-prob1, prob1])
        
        self.doc = open(fileName,'w')
        
        for i in range(1, (length+1)):
            self.avrg = (self.simulator(i,nTimes))
            self.doc.write( str(i) + ' ' + str(self.avrg)+ '\n')
            

    def wordGenerator(self, length):
        word = []
        for i in range(length):
            rand = random.uniform(0,1)
            if rand > self.freq:
                word.append(0)
            else:
                word.append(1)
        #print word
        return word
    
    def simulator(self,length, nTimes):
        success = 0
        for i in range(nTimes):
            word = self.wordGenerator(length)
            received = self.transmission(word)
            
            equal = self.comparison(word,received)
            if equal : success +=1
        print success
        average = float(success)/nTimes
        return average

    def transmission(self,word):
        received = []
        for i in word:
            rand = random.uniform(0,1)
            
            if i is 0:
                if rand > 0 and rand < self.probs[0][0]:
                    received.append(0)
                else:
                    received.append(1)
            elif i is 1:
                if rand > 0 and rand <= self.probs[1][1] :
                    received.append(1)
                else:
                    received.append(0)
        #print received
        return received

    def comparison(self,word,received):
        wrd = ''
        rcv = ''
        for i in range(len(word)):
            wrd += str(word[i])
            rcv += str(received[i])
        #print wrd, "   ", rcv
        if wrd == rcv : return True
        else : return False
'''
    def average(self,nTimes):
        average = 0.0
        for i in successes:
            average +=i
        self.successes = self./nTimes
        return average

    def standardDesviation(self):
        variance = 0.0
        for i in successes:
            variance = pow( (i - self.avrg), 2)
        variance = variance / len(successes)
        stdDes = pow(variance,0.5)
        return stdDes'''

def main():
    fileName = sys.argv[1]
    nTimes = int(sys.argv[2])
    frequency = float(sys.argv[3])
    length = int(sys.argv[4])
    prob0 = float(sys.argv[5])
    prob1 = float(sys.argv[6])
    
    sim = Simulation(frequency, length, nTimes,prob0,prob1, fileName)

if __name__ == "__main__":
    main()
