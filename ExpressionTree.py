#  File: ExpressionTree.py
#  Student Name: Matias Ramirez de Alva
#  Student UT EID: mr59342

import sys

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']

# this dict sets the precedence of the operators
precedence_dict = {'**': 1, '*': 2, '/': 2, '//': 2, '%': 2, '+': 3, '-': 3}


# Input: Elements of a simple expression
#        operator (String) and two operands (numbers)
# Output: result of evaluation of the expression
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)


# Stack Class - DO NOT CHANGE
# Traditional Stack implementation containing list of data items
# Used to keep track of items in nested expressions.
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
#          in a binary expression. It includes data (a character) and
#          two pointers, to the left and right child nodes.
# You do not need to make changes to this class.
class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

# Tree Class
# Purpose: To represent the string representation of operators and operands
#          of a binary expression so it can be evaluated.
# You need to make a lot f changes to this class!
class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree
    def create_tree(self, expr):

        # initialize the stack
        stacko = Stack()

        # iterating through each character in the given expression
        for char in expr:
            
            # check if char is of token "left parenthesis"
            if char == "(":
                stacko.push(char)

            # check if char is of token "operator"
            elif char in operators:

                # the following checks for operator priority order

                # check if stack is empty (is it ever empty if we are working w an operator ???)
                if stacko.is_empty():

                    op = char

                     # create a new node for the operator
                    op_node = Node(op)

                    # push the op_node onto the stack
                    stacko.push(op_node)

                # check if current operator is of higher priority than operators in stack
                else:
                    # get priority of current char
                    curr_precedence = precedence_dict.get(char)

                    # loop check to find the correct place for char
                    while (precedence_dict.get(stacko.peek()) <= curr_precedence) and not stacko.is_empty():

                        # check if item in operators
                        if stacko.peek() in operators:

                            # pop operator
                            popped_operator = stacko.pop()

                            # pop two following operands assuming they are there, 
                            # and make them part of subtree of operator
                            if not stacko.is_empty():
                                rOperand = stacko.pop()
                        
                            if stacko.is_empty() == False:
                                lOperand = stacko.pop()

                            if rOperand and lOperand:
                                popped_operator.rChild = rOperand
                                popped_operator.lChild = lOperand
                            stacko.push(popped_operator)

                    # push operator into stack as new node
                    curr_operator = Node(char)

                    # push operator into stack
                    stacko.push(curr_operator)


            # check if char is of token "operand"
            elif char.isdigit():

                # convert char into an int if necessary (maybe a float too ???)
                numb = int(char)

                # create a new node for the numb
                numb_node = Node(numb)

                # push the numb onto the stack
                stacko.push(numb_node)

            elif char == ")":
                d = 4


    # Input: A node in an expression tree
    # Output: The result of evaluating the expression
    #         with this node as the root
    def evaluate(self, current):
        pass
        '''##### ADD CODE HERE #####'''

    # Starter Method for pre_order
    # Input: a node in an expression tree
    # Output: (string) the preorder notation of the expression
    #                  with this node a the root
    def pre_order(self, current):
        pass
        '''##### ADD CODE HERE #####'''

    # Starter Method for post_order
    # Input: a node in an expression tree
    # Output: (string) the post order notation of the expression
    #                  with this node a the root
    def post_order(self, current):
        pass
        '''##### ADD CODE HERE #####'''


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin

    # read infix expression
    line = in_data.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()