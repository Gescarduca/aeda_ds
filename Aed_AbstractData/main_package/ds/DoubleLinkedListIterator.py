from main_package.ds.SingleLinkedListIterator import list_iterator
#from main_package.ds.DoubleLinkedList import DoubleLinkedList as dbl
from main_package.exceptions import NoSuchElementException

class double_linked_iterator(list_iterator):
    def __init__(self, dbl):
        list_iterator.__init__(self, dbl)
        self.doubly_linked_list = dbl

    # Returns true iff the iteration has more elements in the reverse direction.
    # In other words, returns true if previous would return an element rather than throwing an exception.
    def has_previous(self):
        return self.current_node != None

    # Returns the previous element in the iteration.
    # Throws NoSuchElementException

    def previous(self):
        if not self.has_previous():
            raise NoSuchElementException
        element = self.current_node.get_element()
        self.current_node = self.current_node.get_previous()
        return element

    # Restarts the iteration in the reverse direction. After fullForward, if the iteration is not empty, previous will return the last element in the iteration.
    def full_forward(self):
        self.current_node = self.doubly_linked_list.tail