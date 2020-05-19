<<<<<<< Updated upstream
from ..tad_iterator import TwoWayIterator

class DoublyLinkedListIterator(TwoWayIterator):
    def __init__(self, doubly_linked_list):
        pass

    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
    def has_next(self): pass

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    def next(self): pass

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    def rewind(self): pass

    # Returns true iff the iteration has more elements in the reverse direction.
    # In other words, returns true if previous would return an element rather than throwing an exception.
    def has_previous(self): pass
    
    # Returns the previous element in the iteration.
    # Throws NoSuchElementException
    def previous(self): pass

    # Restarts the iteration in the reverse direction. After fullForward, if the iteration is not empty, previous will return the last element in the iteration.
    def full_forward(self): pass
=======
from ..tad_iterator import TwoWayIterator
from aed_ds.exceptions import EmptyListException, NoSuchElementException

class DoublyLinkedListIterator(TwoWayIterator):
    def __init__(self, doubly_linked_list):
        self.doubly_linked_list = doubly_linked_list
        self.rewind()

    def has_next(self): 
        return self.current_node != None
        

    def next(self): 
        if not self.has_next():
            raise NoSuchElementException()
        element = self.current_node.get_element()
        self.current_node = self.current_node.get_next()
        return element        

    def rewind(self): 
        self.current_node = self.doubly_linked_list.head

    def has_previous(self):
        return self.current_node != None
    
    def previous(self): 
        if not self.has_previous():
            raise NoSuchElementException()
        element = self.current_node.get_element()
        self.current_node = self.current_node.get_previous()
        return element

    def full_forward(self): 
        self.current_node = self.doubly_linked_list.tail
>>>>>>> Stashed changes
