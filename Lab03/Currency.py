#NAME BLOCK:
#Lab: 3
#Name: Nivedita Attada & Justin Lau
'''
Purpose:
The purpose of this lab is to implement link-based List and derivative ADTs using components
from Lab 2 and complex ADT-related methods
'''
from abc import ABC, abstractmethod

class Currency(ABC):
    coinvalue = 1
    notevalue = 100 * coinvalue
    def __init__(self):
        self.total = 0.00

    def __init__(self, amount):
        if amount < 0: raise Exception ('Enter Valid Positive Value')
        self.total = amount

    def __init__(self, Currency):
        self.total = Currency()

    def __del__(self):
        pass


    def get_currency(self):
        return self.total

    def set_currency(self, amt):
        self.total = amt

    def add(self, amt):
        self.total += amt

    def subtract(self, amt):
        try:
            if self.total - amt < 0: raise Exception ('Invalid Subtraction')
            self.total -= amt
        except Exception:
            print('Invalid Subtraction')

    def isEqual(self, input):
        if self.total == input: return True

    def isGreater(self, input):
        if self.total < input: return True

    @abstractmethod
    def toString(self):
        pass
