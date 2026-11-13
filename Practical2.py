import heapq

class Node:
    def __init__(self, char = None, left = None, right = None):
        self.char = char
        self.left = left
        self.right = right

def frequency(text):
    frequency = dict()
    for char in text:
        frequency[char] = frequency.get(char,0) + 1
    return frequency

def buildCode(node,code,mpp):
    if node.char is not None:
        mpp[node.char] = code
        return

    buildCode(node.left, code+"0", mpp)
    buildCode(node.right, code+"1", mpp)

def huffmanCode(text):
    heap = []

    freq = frequency(text)
    print("Frequency count of each character: ",freq)

    counter = 0
    for key, value in freq.items():
        heapq.heappush(heap,(value, counter, Node(char = key)))
        counter += 1

    while len(heap) > 1:
        val1,_,node1 = heapq.heappop(heap)
        val2,_,node2 = heapq.heappop(heap)

        newVal = val1 + val2

        node = Node(left = node1, right = node2)
        heapq.heappush(heap,(newVal, counter, node))
        counter += 1

    root = heap[0][2]

    codeMpp = {}
    buildCode(root, "", codeMpp)

    print("Encoding for each character: ", codeMpp)


    encoding = ""

    for char in text:
        encoding = encoding + codeMpp[char]

    print("Encoded message: ", encoding)

text = input("Enter the text to encode: ")
huffmanCode(text)

