#NAME BLOCK:
#Lab: 3
#Name: Nivedita Attada & Justin Lau
'''
Purpose:
The purpose of this lab is to implement link-based List and derivative ADTs using components
from Lab 2 and complex ADT-related methods
'''
from LinkNode import LinkNode

#implementation of stack data structure
class Stack:
    # creates a stack object
    def __init__(self):
        self.start = LinkNode('') #initializes a head node and creates a stack

    #deletes stack object
    def __del__(self):
        print('Stack Deleted') #prints out statement informing user of deletion


    '''This function adds a new object to the top of the Stack
    Pre: object - contains data at the top of node
    Post:
    Return:
    PSUEDOCODE: This code assigns a new object at the top of the stack and moves everything else down'''
    #adds new object to the stack
    def push(self, value):
        node = LinkNode(value)
        node.next = self.start.next
        self.start.next = node


    '''Removes top object
    Pre:
    Post:
    Return:
    PSUEDOCODE: This function removes the last node to be added to the stack '''
    def pop(self):
        popNode = self.start.next
        self.start.next = self.start.next.next
        return popNode.data


    '''prints last value on stack
    Pre:
    Post:
    Return:
    PSUEDOCODE: This function does not alter the stack and prints the last object added'''
    def peek(self):
        print(self.start.next.data)
        return self.start.next.data


    '''prints whole Stack
    Pre:
    Post:
    Return:
    PSUEDOCODE: This function prints each node in the stack separated by a tab'''
    def printStack(self):
        x = self.start
        dataStr = ''
        while x:
            dataStr += (str(x.data) + '\t')
            x = x.next
        print(dataStr)
        return dataStr
