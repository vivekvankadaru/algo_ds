import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
class Custom_list:
    """
    Custom_list is a placeholder class for a custom implementation of a list data structure.
    This class is intended to be extended with methods and attributes that mimic or enhance
    the behavior of Python's built-in list, allowing for custom functionality as needed.
    Attributes:
        (No attributes defined yet)
    Methods:
        __str__(): Returns a string representation of the Custom_list instance.
    """
    def __init__(self):
        '''if iterable:
            self.data=iterable
        else:
            self.data=None
        '''
        pass

    def __str__(self):
        return 

    def __repr__(self):
        log.info('repr is called')

    def __len__(self):
        log.info('len is called')

    def __add__(self, other):
        print('__add__ called: self+other')

    def __mul__(self, other):
        pass

    def __get_item__(self):
        pass

    def append(self, value):
        pass


l2=Custom_list()
l2.append(4)
print(l2)
