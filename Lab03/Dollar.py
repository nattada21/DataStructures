#NAME BLOCK:
#Lab: 2
#Name: Nivedita Attada & Justin Lau
'''
Purpose:
The purpose of this lab is to demonstrate polymorphism and object oriented programming
within a scenario through multiple classes, objects, and state management.
'''
from Currency import Currency
from abc import ABC, abstractmethod

class Dollar(Currency):
    def __init__(self, total):
        self.total = total
        self.curr_name = ' Dollar'

    # getters and setters

    def get_total(self):
        return self.total

    def set_total(self,amt):
        self.total = amt

    '''
    This function grabs a num from the user and stringifies the name and value in the form xx.yy
    Pre: float - float num provided by user
    Post:
    Return: str
    PSUEDOCODE: get the "total" portion as a str and add the curr name to it (already a string)
        '''
    def toString(self):
            return "%.2f" % self.total + self.curr_name
