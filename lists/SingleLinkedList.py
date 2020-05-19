from list import List
from nodes import DoubleListNode as dn
from nodes import SingleListNode as sn
from list_iterator import list_iterator as lit
#from ..exceptions import EmptyListException
#from exceptions import InvalidPositionException as ipe
#from exceptions import EmptyListException as ele
#from exceptions import NoSuchElementException as nse



class single_linked_list(List):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.number_elements = 0

    # Returns true iff the list contains no elements.
    def is_empty(self):
        if self.head == None:
            return True
        return False
            

    # Returns the number of elements in the list.
    def size(self):
        return self.number_elements

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        try:
            if not self.head:
                raise Exception
            else:
                return self.head.get_element()
                
        except:
            print("EmptyListException")
        

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        try:
            if not self.head:
                raise Exception
            else:
                return self.tail.get_element()
        except:
            print("EmptyListException")


    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        aux = 0
        node_to_iterate = self.head
        if position<0 or position>self.size()-1:
            print("Position invalid!")
        while aux < position:
            node_to_iterate = node_to_iterate.next_node
            aux+=1
        return node_to_iterate.get_element()

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element): 
        position = 0
        node_to_iterate = self.head
        while node_to_iterate:
            if node_to_iterate.get_element() == element:
                return position
            else:
                node_to_iterate = node_to_iterate.next_node
                position+=1
        return -1


    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new_node  = sn(element,self.head)
        #new_node.next_node = self.head
        self.head = new_node
        self.number_elements += 1
        if self.tail == None:
            self.tail = self.head

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        new_node = sn(element,None)
        if self.head is None:
            self.head = new_node
            return
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            self.number_elements +=1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        try:
            if position>self.size() or position < 0:
                raise Exception
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
                        if number == position:
                            node_to_iterate.next_node = sn(element,node_to_iterate.next_node)
                            self.number_elements+=1
                            return
                        else:
                            node_to_iterate = node_to_iterate.next_node
                    
        except:
            print("InvalidPosition!")
                    

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if not self.head:
            raise Exception("EmptyListException")
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next_node
            self.number_elements-=1
            return node_to_remove.get_element()

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        try:
            if not self.head:
                raise Exception
            else:
                node_to_iterate = self.head
                node_to_remove = self.tail
                previous_node = None
                while node_to_iterate.next_node:
                    previous_node = node_to_iterate
                    node_to_iterate = node_to_iterate.next_node
                    

                self.tail = previous_node
                self.tail.set_next(None)
                #print(self.tail.get_element())
                self.number_elements-=1
                return node_to_iterate.get_element()
        except:
            print("EmptyListException") 
                

    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        number = 0
        try:
            if position < 0 or position>=self.size():
                raise Exception
            else:
                node_to_iterate = self.head
                previous_node = None
                while node_to_iterate:
                    if number == position:
                        node_to_remove = node_to_iterate
                        previous_node.set_next(node_to_remove.next_node)

                        self.number_elements-=1
                        return node_to_remove.get_element()
                    else:
                        previous_node = node_to_iterate
                        node_to_iterate = node_to_iterate.next_node
                        number+=1
        except:
            print("InvalidPositionException")
    
    # Removes all elements from the list.
    def make_empty(self):
        self.head = None
        self.tail = None
        self.number_elements = 0

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        self.my_list = lit(self.head)
        for i in range(self.number_elements):
            print(self.my_list.next())
        return self.my_list

        


    #def print_list(self):
        #current_node = self.head
        #while current_node:
            #print(current_node.element)
            #current_node = current_node.next_node

    #def display(self):
        #print("teste")

# a partir daqui corre

llist = single_linked_list()
llist.insert_first("A")
llist.insert_last("B")
#llist.insert("D",3)
llist.insert("C",1)

#find_method
#print(llist.find("C"))
#print(llist.find("D"))

#get_method
#print(llist.get(1))
#llist.insert_first("C")

#get_first_method
#print(llist.get_first())

#remove_last_node erro
#print(llist.remove_last())

#remove_first_node
#print(llist.remove_first())

#remove_node erro
#print(llist.remove(1))

#iterator
#llist.iterator()

#llist.print_list()

llist.iterator()