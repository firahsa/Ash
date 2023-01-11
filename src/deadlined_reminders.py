from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from os import times_result
from dateutil.parser import parse
from datetime import datetime, date


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta): 

    @abstractmethod 
    def is_due(self):
        pass

class DeadlinedReminder(ABC, Iterable): 

     @abstractmethod
     def is_due(self): 
         pass

     @classmethod
     def __subclasshook__(cls, subclass): # subhook checks that the given subclass contains the required methods __iter__() and is_due() anywhere in its hierarchy
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any (attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True


class DateReminder(DeadlinedReminder): 
    def __init__(self, text: str, date: str, time: str, completed=bool):  # method takes 4 arguments 
        self.date = parse(f'{date} {time}', dayfirst=True)  # parse function stores date parameter on to self.
        self.text = text 
        self.time = time 
        self.date = date
        self.completed = completed # adds an new attribute called complete which is set to False as a default to show

   
    def mark_as_completed(self):
        self.completed = True # add a method called mark_as_completed to the class, which sets the completed attribute to True.

        
    def is_due(self):
        return self.date <= datetime.now()
        
 
    def __iter__(self): 
        return iter([self.text, self.date.isoformat(), self.time.strftime('%I:%M %p'), self.completed])
    

