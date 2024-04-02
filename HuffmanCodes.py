#  File: HuffmanCodes.py
#  Student Name:
#  Student UT EID:
# Python Huffman Compression
from PriorityQueue import PriorityQueue
import sys


# Huffman Node Class
class Huffman_Node(object):
    def __init__(self, ch=None, count=0, left=None, right=None):
        self.ch = ch
        self.count = count
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        if self.ch is None:
            ch = "*"
        else:
            ch = self.ch
        return ch + ", " + str(self.count)


# Build Character Frequency Table
# uses dictionary
# characters added in the order they first occur
def build_char_freq_table(inputString):

    table =  dict() 

    for i in range(len(inputString)):

        currentCharacter = inputString[i]

        if currentCharacter in table.keys():
            table[currentCharacter] = table[currentCharacter] + 1

        else:
            table[currentCharacter] = 1

    return table


# Builds the Huffman Tree
# Creates Huffman Nodes, some pointing to others.
# Returns the root node
def build_huffman_tree(inputString):
    # Build the frequency table, a dictionary of character, frequency pairs
    freq_table = build_char_freq_table(inputString)

    # Build a priority queue, a queue of frequency, character pairs
    # Hightest priority is lowest frequency
    # When a tie in frequency, first item added will be removed first
    priorities = PriorityQueue()
    for key in freq_table:
        node = Huffman_Node(ch=key, count=freq_table[key])
        priorities.push(node)

    # Builds internal nodes of huffman tree, connects all nodes
    while (priorities.get_size() > 1):

        # Dequeue 2 lowest priority nodes
        left = priorities.pop()
        right = priorities.pop()

        # Make a parent for the two nodes
        freqSum = right.count + left.count
        parentNode = Huffman_Node(ch=None, count=freqSum, left=left, right=right)

        # Enqueue parent into nodes
        priorities.push(parentNode)

    # At the end, priority queue is empty
    # Return the root node of the Huffman Tree
    return priorities.pop()


# After Huffman Tree is built, create dictionary of
# characters and code pairs
def get_huffman_codes(node, prefix, codes):
    if (node.left is None and node.right is None):
        codes[node.ch] = prefix
    else:
        get_huffman_codes(node.left, prefix + "0", codes)
        get_huffman_codes(node.right, prefix + "1", codes)
    return codes


# For each character in input file, returns the Huffman Code
# Input file uses <space> to indicate a space
# If character not found, display "No code found"
def process_chars(data, huff_codes):

    # ADD CODE HERE

    # var for header
    header = "Character    Code"
 
    # bool var to skip first line
    first = True
    
    # loop over each line in data
    for line in data:
        
        # only character that matters is the first of each line
        inp = line[0]

        # skip the first line
        if first == True:
            print(header)
            first = False
            continue




        # account for "<space>" 
        if (inp == "<"):
            if " " in huff_codes.keys():
                character = "            "
                code = huff_codes[" "]
            else:
                character = "            "
                code = "No code found"
            print(character, code)
            continue

        # check if not in dict
        if (inp not in huff_codes.keys()):
            character = inp + "           "
            code = "No code found"
            print(character, code)
            continue
    
            
        # characters in dict
        else:
            character = inp + "           "
            code = huff_codes[inp]
            print(character, code)
            
        


    
        

''' DRIVER CODE '''

# Open input source
# Change debug to false before submitting
debug = True
if debug:
    in_data = open('message.in')
else:
    in_data = sys.stdin

# read message
data = in_data.readlines()
message = data[0].strip()

# Build Huffman Tree and Codes
root = build_huffman_tree(message)
huff_codes = get_huffman_codes(root, "", {})

# display code for each character in input file
process_chars(data, huff_codes)