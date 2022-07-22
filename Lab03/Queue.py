#NAME BLOCK:
#Lab: 3
#Name: Nivedita Attada & Justin Lau
'''
Purpose:
The purpose of this lab is to implement link-based List and derivative ADTs using components
from Lab 2 and complex ADT-related methods
'''
from LinkNode import LinkNode
class Queue:

    def __init__(self):
        self.start = self.end = None

    def __del__(self):
        print('Queue Deleted')
        
    '''
    This function takes a Currency object as parameter and adds it to the end of the queue.
    Pre: value - float num
    Post: 
    Return: 
    PSUEDOCODE: create temp node and adds value with existing nodes
    '''

    def enqueue(self, value):
        temp = LinkNode(value)
        if self.end == None:
            self.start = self.end = temp
            return
        self.end.next = temp
        self.end = temp
    
    '''
    This function takes no parameter and removes and returns the Currency object from the front of the queue.
    Pre: 
    Post: 
    Return: 
    PSUEDOCODE: create temp node and deletes value with existing nodes
    '''

    def dequeue(self):
        temp = self.start
        self.start = temp.next

        if(self.start == None):
            self.end = None

    '''
    This function takes no parameter and returns a copy of the Currency object at the front of the queue.
    Pre: 
    Post: 
    Return: self.end.data
    PSUEDOCODE: create temp node and and grab the "front" data
    '''

    def peekFront(self):
            print(self.end.data)
            return self.end.data

    '''
    This function takes no parameter and returns a copy of the Currency object at the end of the queue.
    Pre: 
    Post: 
    Return: self.start.data
    PSUEDOCODE: create temp node and and grab the "end" data
    '''

    def peekRear(self):
            print(self.start.data)
            return self.start.data

    '''
    This function returns a string signifying the contents of the queue from front to end, tab spaced.
    Pre: 
    Post: 
    Return: dataStr
    PSUEDOCODE: Stringify use \t delimiter and putting within temp string to print
    '''

    def printQueue(self):
        x = self.start
        dataStr = ''
        while x:
            dataStr += (str(x.data) + '\t')
            x = x.next
        print(dataStr)
        return dataStr
