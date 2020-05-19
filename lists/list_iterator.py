
from nodes import SingleListNode as sn
#from ..exceptions import EmptyListException,InvalidPositionException,NoSuchElementException
from iterator import Iterator as it
#from exceptions import EmptyListException,InvalidPositionException,NoSuchElementException



class list_iterator(it):
    def __init__(self,head):
        self.first = head
        self.current_node = head

    def __iter_(self):
        return self

    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.

    def has_next(self):
        if self.current_node.next_node:
            return True
        return False
        
        

    # Returns the next element in the iteration.
    # Throws NoSuchElementException

    def next(self): 
        self.previous = self.current_node
        self.current_node = self.current_node.next_node
        return self.previous.get_element()
        


    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.

    def rewind(self):
        self.current_node = self.first


class double_linked_iterator(list_iterator):
    def __init__(self,head,tail):
        list_iterator.__init__(self,head)
        self.last = tail
        self.current_node = tail
    # Returns true iff the iteration has more elements in the reverse direction.
    # In other words, returns true if previous would return an element rather than throwing an exception.
    def has_previous(self): 
        if self.last.previous:
            return True
        return False
    
    # Returns the previous element in the iteration.
    # Throws NoSuchElementException
    @abstractmethod
    def previous(self):
        self.node_to_get = self.current_node
        self.current_node = self.current_node.previous_node
        return self.node_to_get.get_element()

    # Restarts the iteration in the reverse direction. After fullForward, if the iteration is not empty, previous will return the last element in the iteration.
    @abstractmethod
    def full_forward(self): pass

    
