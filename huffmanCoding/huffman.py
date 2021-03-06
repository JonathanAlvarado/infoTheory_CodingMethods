class Node:
    def __init__(self,letter, frequency, left, right):
        self.letter = letter
        self.frequency = frequency
        self.left = left
        self.right = right
        self.code = ''
    
    def __str__(delf):
        return self.letter

def lettersFrequency(text):
    freq = {}
    for c in text:
        if c not in freq.keys():
            f = text.count(c)
            freq[c] = f
    return freq.items()

def orderFrequencies(freq):
    nodes = []
    freq = sorted(freq, key=lambda f:f[1])
    
    for f in freq:
        node = Node(f[0], f[1], None, None)
        #print node.letter, ' ', node.frequency
        nodes.append(node)
    return nodes

def getInfo(node):
    if len(node.letter) == 1:
        print 'letter:',node.letter
        print 'frequency', node.frequency
        print 'code:', node.code, '\n'
    if node.left != None:
        getInfo(node.left)
    if node.right != None:
        getInfo(node.right)

def getNodes(tree):
    while len(tree) > 1:
        left = tree.pop(0)
        right = tree.pop(0)
        letter = left.letter + right.letter
        value = left.frequency + right.frequency
        left.code = '0'
        right.code = '1'
        node = Node(letter, value, left, right)
        #print node.letter, ' ', node.frequency
        tree.append(node)
        tree.sort()
    return tree
        
#the first node that receives is the root of the tree
def getCodes(node):
    if node.left != None:
        node.left.code = node.code + node.left.code
        getCodes(node.left)
    if node.right != None:
        node.right.code = node.code + node.right.code
        getCodes(node.right)
        
def huffmanTree(node, data):
    if not data.has_key(node.letter):
        data[node.letter] = node

    if node.left != None:
        data = huffmanTree(node.left, data)

    if node.right != None:
        data = huffmanTree(node.right, data)

    return data

def compress(data, text):
    codesTable = {}
    compressed = ''
    nodes = data.keys()
    for n in nodes:
        node = data[n]
        codesTable[node.letter] = node.code

    for c in text:
        compressed += codesTable[c]
    return codesTable, compressed

def decompress(node, compressed):
    root = node
    ctext = []
    for c in compressed:
        ctext.append(c)
    msg = ''
    while len(ctext) > 0:
        n = int(ctext.pop(0))
        if(n==0):
            if (node.left != None and len(node.left.letter) == 1):
                msg += node.left.letter
                node = root
            else:
                node = node.left
        else:
            if (node.right != None and len(node.right.letter) == 1):
                msg += node.right.letter
                node = root
            else:
                node = node.right
    return msg
            
    

if __name__ == '__main__':
    #text = 'test this'
    text = raw_input('Text to compress: ')
    text = text.replace('\t',' ').replace('\n',' ')
    freq = lettersFrequency(text)
    freq = orderFrequencies(freq)
    tree = getNodes(freq)
    getCodes(tree[0])
    data = huffmanTree(tree[0], data = {})
    #getInfo(tree[0])
    codesTable, compressed = compress(data, text)
    print 'Original Text: ', text,'\n'
    print 'Compressed text: ',compressed,'\n'
    #print 'Codes table:\n',codesTable,'\n'
    getInfo(tree[0])
    msg = decompress(tree[0], compressed)
    print 'Decompressed text: ', msg
