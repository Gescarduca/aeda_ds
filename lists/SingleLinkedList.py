from list import List
from nodes import DoubleListNode as dn
from nodes import SingleListNode as sn
#from exceptions import InvalidPositionException as ipe



class single_linked_list(List):
    # Returns true iff the list contains no elements.
    def __init__(self):
        self.head = None
        self.tail = None
        self.number_elements = 0

    def is_empty(self):
        if self.head == None:
            return False
        return True
            

    # Returns the number of elements in the list.
    def size(self):
        return self.number_elements
    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):pass
        

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self): pass

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position): pass

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element): pass

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new_node  = sn(element,self.head)
        new_node.next_node = self.head
        self.head = new_node
        self.number_elements += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        #print("t") 
        new_node = sn(element,None)
        if self.head is None:
            self.head = new_node
            #print("teste")
            return
        node_to_iterate = self.head
        while node_to_iterate.next_node:
            node_to_iterate = node_to_iterate.next_node
        node_to_iterate.next_node = new_node
        self.number_elements +=1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if position>self.size() or position < 0:
            #raise ipe() it is supposed to raise the exception but the import is a bit funky cant quite get it
            # to work, run time complains about non existing module
            #print("Outside of boundaries")
            raise Exception("Invalid Position!")
            
        else:
            number = 0
            if position == 0:
                self.insert_first(element)
            elif position == self.size():
                self.insert_last(element)
            else:
                node_to_iterate = self.head
                while node_to_iterate:
                    number += 1
                    if number == position-1:
                        node_to_iterate.next_node = sn(element,node_to_iterate.next_node)
                        #print("teste1")
                        return
                    else:
                        node_to_iterate = node_to_iterate.next_node
                        #print("teste")
        
                    

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self): pass

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self): pass
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position): pass
    
    # Removes all elements from the list.
    def make_empty(self): pass

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self): pass


    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.element)
            current_node = current_node.next_node

    def display(self):
        print("teste")



llist = single_linked_list()
llist.insert_first("A")
llist.insert_last("B")
llist.insert("D",3)
llist.insert("C",2)


#llist.insert_first("C")





llist.print_list()