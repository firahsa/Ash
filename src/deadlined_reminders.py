from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta): # inherits from Iterable and sets metaclass parameter as ABCMeta

    @abstractmethod # contains no implementation on its own
    def is_due(self):
        pass

class DeadlinedReminder(ABC, Iterable): # inherits from ABC class and Iterable

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


class DateReminder(DeadlinedReminder): # inherits from DeadlinedReminder
    def __init__(self, text, date): ## init takes these parameters 
        self.date = parse(date, dayfirst=True)  # parse function stores date parameter on to self.
        self.text = text 
   
    # def __str__(self):
       # return f"{self.text} ({self.date})"

    # reminder = DateReminder("Take out the trash", "2022-01-08") # customises the way that the object is printed
    # print(reminder)  # Output: Take out the trash (2022-01-08)   

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self): # setting up the built in iter function
        return iter([self.text, self.date.isoformat()]) # Passing it a list of the reminders text and formatted version of the date by calling self.date.isoformat


