import random,sys

class Simulation:

    def __init__(self,frequency,length,nTimes,prob0, prob1):
        self.freq = frequency
        self.length = length
        self.probs = [[prob0, 1-prob0],[1-prob1, prob1]]
        self.simulator(nTimes)

    def wordGenerator(self):
        word = []
        for i in range(self.length):
            rand = random.uniform(0,1)
            if rand > self.freq:
                word.append(0)
            else:
                word.append(1)
        #print word
        return word
    
    def transmission(self,word):
        received = []
        for i in range(len(word)):
            rand = random.uniform(0,1)
            
            if word[i] is 0:
                if rand >= self.probs[0][0]:
                    received.append(0)
                else:
                    received.append(1)
            elif word[i] is 1:
                if rand >= self.probs[1][1] :
                    received.append(0)
                else:
                    received.append(1)
        #print received
        return received
        
    def simulator(self, nTimes):
        for i in range(nTimes):
            word = self.wordGenerator()
            received = self.transmission(word)


def main():
    nTimes = int(sys.argv[1])
    frequency = float(sys.argv[2])
    length = int(sys.argv[3])
    prob0 = float(sys.argv[4])
    prob1 = float(sys.argv[5])
    
    sim = Simulation(frequency, length, nTimes,prob0,prob1)

if __name__ == "__main__":
    main()
