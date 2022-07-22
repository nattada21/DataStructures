#NAME BLOCK:
#Lab: 3
#Name: Nivedita Attada & Justin Lau
'''
Purpose:
The purpose of this lab is to implement link-based List and derivative ADTs using components
from Lab 2 and complex ADT-related methods
'''
from SinglyLinkedList import SinglyLinkedList
from Stack import Stack
from Queue import Queue
from Dollar import Dollar
from Currency import Currency

def main():
    dollar_arr = [  # indexes
        Dollar(57.12), #0
        Dollar(23.44), #1
        Dollar(87.43), #2
        Dollar(68.99), #3
        Dollar(111.22), #4
        Dollar(44.55), #5
        Dollar(77.77), #6
        Dollar(18.36), #7
        Dollar(543.21), #8
        Dollar(20.21), #9
        Dollar(345.67), #10
        Dollar(36.18), #11
        Dollar(48.48), #12
        Dollar(101.00), #13
        Dollar(11.00), #14
        Dollar(21.00), #15
        Dollar(51.00), #16
        Dollar(1.00), #17
        Dollar(251.00), #18
        Dollar(151.00), #19
    ]
    
    print('Lab #3 Welcome Message: ')
    print('Implementing Lab2 using Linked Lists, Stacks, and Queues')
    print('- Nivedita Attada & Justin Lau')

    # making objects

    singlylinkedlstObj = SinglyLinkedList()
    print("Start Linked List")
    # linked list objectives
    for i in range(0,7):
        singlylinkedlstObj.addCurrency(dollar_arr[i].total)
    print(singlylinkedlstObj.printList())
    singlylinkedlstObj.findCurrencyIndex(87.43)
    singlylinkedlstObj.findCurrencyIndex(44.56)
    singlylinkedlstObj.removeCurrencyFromElement(111.22)
    singlylinkedlstObj.removeCurrencyAtIndex(2) # the node at index 2
    print(singlylinkedlstObj.printList())
    for i in range(9,12):
        singlylinkedlstObj.addCurrencyatIndex(i % 5, dollar_arr[i].total)
    singlylinkedlstObj.removeCurrencyAtIndex(singlylinkedlstObj.countCurrency()%6)
    singlylinkedlstObj.removeCurrencyAtIndex(singlylinkedlstObj.countCurrency()/7)
    print(singlylinkedlstObj.printList())

    print("\nStart Stack\n")
    s = Stack()
    for i in range(7):
        s.push(dollar_arr[i+13].total)
    s.peek()
    s.pop()
    s.pop()
    s.pop()
    s.printStack()
    for i in range(5):
        s.push(dollar_arr[i].total)
    s.pop()
    s.pop()
    s.printStack()

    print("\nStart Queue\n")
    q = Queue()
    for i in range(5,19,2):
        q.enqueue(dollar_arr[i].total)
    q.peekFront()
    q.peekRear()
    q.dequeue()
    q.dequeue()
    q.printQueue()
    for i in range(5):
        q.enqueue(dollar_arr[i+10].total)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.printQueue()

    print('Ending Message: Thank you for using our program')
    print('Have a wonderful day :)')

if __name__ == "__main__":
    main()
