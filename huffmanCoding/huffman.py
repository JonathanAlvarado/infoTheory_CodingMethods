def lettersFrequency(text):
    freq = {}
    for c in text:
        if c not in freq.keys():
            f = text.count(c)
            freq[c] = f
    return freq.items()

def orderFrequencies(freq):
    return sorted(freq, key=lambda f:f[1])

def huffmanTree(freq):
    tree = {}
    while len(freq) > 1:
        left = freq.pop(0)
        right = freq.pop(0)
        value = left[1] + right[1]
        tree[left[0], value] = 0
        tree[right[0], value] = 1
        freq.append((value,value))
        freq = orderFrequencies(freq)
    return tree.items(), freq[0]

if __name__ == '__main__':
    text = 'This is a test'
    text = text.replace('\t',' ').replace('\n',' ')
    freq = orderFrequencies( lettersFrequency(text.lower()) )
    tree, root = huffmanTree(freq)
    tree = sorted(tree, key=lambda node:node[0][1])
    
    
