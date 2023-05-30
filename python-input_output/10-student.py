#!/usr/bin/python3
''' class that defines a student '''


class Student:
    ''' class that defines a student '''
    def __init__(self, first_name, last_name, age):
        ''' constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves a dictionary representation of a Student instance '''
        ''' If attrs is a list of strings, only attribute names contained in this list must be retrieved. '''
    
        if not attrs:
            return vars(self)
        
        return ({key: value for key, value in self.__dict__.items() \
                 if key in attrs})