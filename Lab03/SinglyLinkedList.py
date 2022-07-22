#NAME BLOCK:
#Lab: 3
#Name: Nivedita Attada & Justin Lau
'''
Purpose:
The purpose of this lab is to implement link-based List and derivative ADTs using components
from Lab 2 and complex ADT-related methods
'''
from LinkNode import LinkNode
class SinglyLinkedList():
    def __init__(self, count = 0, start = None, end = None):
        self.count = count
        self.start = start
        self.end = end
        self.length = 0
    
    #  getters and setters
        
    def getCount(self):
        return self.count
    
    def setCount(self, count):
        self.count = count
    
    def setStart(self):
        return self.start
    
    def setStart(self, start):
        self.start = start
    
    def getEnd(self):
        return self.end
    
    def getEnd(self, end):
        self.end = end
    
    # addCurrency at Index Method 1 (At an Index)
    '''
    This function adds an item at a specific index
    Pre: index - int num, item - float num 
    Post: IndexError, 
    Return: 
    PSUEDOCODE: Iterate through nodes and check certain properties to find proper position to insert
    '''
    
    def addCurrencyatIndex(self, index, item):
        temp = LinkNode(item)
        current = self.start
        previous = None
        count = 0
        found = False
        if index > self.length-1:
            raise IndexError('List Index Out Of Range')
        while current is not None and not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.getNext()
                count += 1
        if previous is None:
            temp.setNext(self.start)
            self.start = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        self.length += 1
    
    # addCurrency Method 2 (Just adding)
    '''
    This function adds an item to the start of a linked list
    Pre: item - float num 
    Post: 
    Return: 
    PSUEDOCODE: assign temp variable and create new link node while inserting existing nodes
    '''
    def addCurrency(self, item):
        temp = LinkNode(item)
        temp.setNext(self.start)
        self.start = temp
        if self.end is None:
            self.end = temp
        self.length += 1

    '''
    This function removes a given element from a linked list
    Pre: item - float num 
    Post: 
    Return: 
    PSUEDOCODE: Iterate through list to find item and remove it
    '''
    def removeCurrencyFromElement(self,item):
        current = self.start
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            # The item is the 1st item
            self.start = current.getNext()
        else:
            if current.getNext() is None:
                self.tail = previous  # in case the current tail is removed
            previous.setNext(current.getNext())
        self.length -= 1

    '''
    This function finds an item's index
    Pre: item - float num 
    Post: 
    Return: 
    PSUEDOCODE: Iterate through list to find item and identify its position through increment
    '''
    def findCurrencyIndex(self, item):
        pos = 0
        current = self.start
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if not found:
            print('Value not present in the List')
            return
        print()
        print(pos)
        return
    
    '''
    This function takes an index values as a parameter and returns the Currency object.
    Pre: item - float num 
    Post: 
    Return: 
    PSUEDOCODE: Use current to iterate through and get the index if it exists
    '''
    def getCurrency(self, index):
        current = self.start  
        count = 0  
        while (current):
            if (count == index):
                print(current.data) 
                return
            count += 1
            current = current.next
        print("Missing") 
        return 0

    '''
    This function returns if a list is empty or not.
    Pre: 
    Post: 
    Return: boolean
    PSUEDOCODE: if self.start is None then empty
    '''
    def isListEmpty(self):
        return self.start is None
    
    '''
    This function returns a count of Currency nodes in the list.
    Pre: 
    Post: 
    Return: length
    PSUEDOCODE: increment length while current is True
    '''
    def countCurrency(self):
        current = self.start
        length = 0
        while current:
            length = length + 1
            current = current.next
        return length

    '''
    This function returns a string of all the Currency objects in the list in the order of index, tab spaced.
    Pre: 
    Post: 
    Return: string
    PSUEDOCODE: Assign Current and check if then next node is not None and return
    '''
    def printList(self):
            current = self.start
            string = '['
            while current is not None:
                string += str(current.getData())
                if current.getNext() is not None:
                    string += ', '
                current = current.getNext()
            string += ']'
            return string
    
    '''
    This function takes a node index as parameter and removes the Currency object at that index and may return a copy of the Currency.
    Pre: index - int num from user
    Post: 
    Return: 
    PSUEDOCODE: 
    '''
    def removeCurrencyAtIndex(self, index=None):
        if index is None:
            index = self.length-1
        if index > self.length-1:
            raise IndexError('List Index Out Of Range')
        current = self.start
        previous = None
        found = False
        if current:
            count = 0
            while current.getNext() is not None and not found:
                if count == index:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                    count += 1
            if previous is None:
                self.start = current.getNext()
                if current.getNext() is None:
                    self.tail = current.getNext()
            else:
                self.tail = previous
                previous.setNext(current.getNext())
        self.length -= 1
        return current.getData()

    
    
        
    
        
        
        
        