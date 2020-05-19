from .singly_linked_list import SinglyLinkedList
from .nodes import DoubleListNode
from .doubly_linked_list_iterator import DoublyLinkedListIterator
from ..exceptions import EmptyListException, NoSuchElementException, InvalidPositionException

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        SinglyLinkedList.__init__(self)

    def insert_first(self, element): 
        new_node = DoubleListNode(element, self.head, None)
        if not self.head:
            self.tail = new_node
        else:
            self.head.set_previous(new_node)
        self.head = new_node
        self.num_elements += 1
        
    def insert_last(self, element): 
        new_node = DoubleListNode(element, None, self.tail)
        if not self.head: 
            self.head = new_node
        else:    
            self.tail.set_next(new_node)
        self.tail = new_node
        self.num_elements += 1

    def insert(self, element, position):
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        elif position == 0:
            return self.insert_first(element)
        elif position == self.size():
            return self.insert_last(element)
        prev_node = self.head
        cur_node = self.head
        idx = 0
        while prev_node:
            if position == idx:
                new_node = DoubleListNode(element, cur_node, prev_node)
                prev_node.set_next(new_node)
                cur_node.set_previous(new_node)
                self.num_elements += 1
                break
            prev_node = cur_node
            cur_node = cur_node.get_next()
            idx += 1

    def remove_first(self): 
        if self.num_elements == 1:
            old_node = self.head
            self.make_empty()
            return old_node.get_element()
        elif self.num_elements == 0:
            raise EmptyListException()
        old_head = self.head
        self.head = self.head.get_next()
        self.head.set_previous(None)
        self.num_elements -= 1
        return old_head.get_element()

    def remove_last(self):
        if self.size() == 0:
            raise EmptyListException()        
        elif self.size() == 1:
            old_node = self.head
            self.make_empty()
            return old_node.get_element()
        elif self.size() == 2:
            self.head.set_next(None)
            old_node = self.head
            self.tail.set_previous(None)
            self.tail = self.head
            self.num_elements -= 1
            return old_node.get_element()
        else:
            old_node = self.tail
            new_tail = self.tail.get_previous()
            new_tail.set_next(None)
            self.tail.set_previous(None)
            self.tail = new_tail
            self.num_elements -= 1
            return old_node.get_element()

    def remove(self, position):
        if position < 0 or position > self.size() - 1:
            raise InvalidPositionException()
        elif position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == position:
                prev_node = cur_node.get_previous()
                next_node = cur_node.get_next()
                prev_node.set_next(next_node)
                next_node.set_previous(prev_node)
                self.num_elements -= 1
                return cur_node.get_element()
            cur_node = cur_node.get_next()
            idx += 1

    def iterator(self): 
        return DoublyLinkedListIterator(self)
                