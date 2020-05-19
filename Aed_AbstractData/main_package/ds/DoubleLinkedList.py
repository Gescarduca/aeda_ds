from main_package.ds.single_linked_list import single_linked_list as sl

from main_package.ds.nodes import DoubleListNode as dln

from main_package.exceptions import EmptyListException, InvalidPositionException, NoSuchElementException

from main_package.ds.SingleLinkedListIterator import list_iterator as lit

class DoubleLinkedList(sl):

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
                raise EmptyListException
            else:
                return self.head.get_element()

        except EmptyListException:
            print("EmptyListException")

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
            if not self.head:
                raise EmptyListException
            else:
                return self.tail.get_element()



    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        aux = 0
        try:
            if position < 0 or position > self.size() - 1:
                raise InvalidPositionException
                #print("pos")
            new_pos = abs(self.size()/2)
            if position>new_pos:
                node_to_iterate = self.tail
                aux = self.size()
                while node_to_iterate:
                    if aux == position:
                        return node_to_iterate.get_element()
                    else:
                        aux-=1
                        node_to_iterate = node_to_iterate.get_previous()
            elif position<new_pos:
                node_to_iterate = self.head
                while node_to_iterate:
                    if aux == position:
                        return  node_to_iterate.get_element()
                    else:
                        aux+=1
                        node_to_iterate = node_to_iterate.get_next()
        except InvalidPositionException:
            print("Invalid Position")


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
                position += 1
        return -1

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new_node = dln(element, self.head, None)
        # new_node.next_node = self.head
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
            self.number_elements +=1
        elif not self.is_empty():
            self.head.set_previous(new_node)
            self.head = new_node
            self.number_elements += 1



    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        new_node = dln(element, None, self.tail)
        if self.head is None:
            self.head = new_node
            return
        else:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node
            self.number_elements += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        try:
            print(("start"))
            if position > self.size() or position < 0:
                raise InvalidPositionException
                print("1")
                return
            elif position == 0:
                self.insert_first(element)
                return

            elif position == self.size():
                self.insert_last(element)
                return

            else:

                new_size = abs(self.size() / 2)
            #print(new_size)
                if position > new_size:
                    my_count = self.size()
                    node_to_iterate = self.tail
                    while node_to_iterate and my_count>position:
                        node_to_iterate = node_to_iterate.get_previous()
                        my_count -= 1
                        if my_count == position+1:
                            new_node = dln(element,node_to_iterate,node_to_iterate.get_previous())
                            node_to_iterate.set_previous(new_node)
                            self.number_elements+=1
                            print("mid1")
                            break
                elif position<=new_size:
                    my_count = 0
                    node_to_iterate = self.head
                    while node_to_iterate:
                        if my_count == position-1:
                            print((node_to_iterate.get_next().get_element()))
                            print(node_to_iterate.get_element())
                            new_node = dln(element, node_to_iterate.get_next(), node_to_iterate)
                            node_to_iterate.get_next().set_previous(new_node)
                            node_to_iterate.set_next(new_node)


                            self.number_elements+=1
                            print("mid2")
                            break
                        else:
                            node_to_iterate = node_to_iterate.get_next()
                            my_count += 1

                #update_node1 = node_to_iterate.get_previous()
                #update_node1.set_next(node_to_iterate)
                #update_node2 = node_to_iterate.get_next()
                #update_node2.set_previous(node_to_iterate)
            print(("end"))
        except Exception:
            print("Invalid Position1")
    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        try:
            if not self.head:
                raise EmptyListException
            else:
                node_to_remove = self.head
                self.head = node_to_remove.next_node
                self.head.set_previous(None)
                self.number_elements -= 1
                return node_to_remove.get_element()
        except:
            print("EmptyListException")

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        try:
            if self.size() == 0:
                raise EmptyListException
            else:
                node_to_remove = self.tail
                #print(node_to_remove.get_previous().get_element())
                #print((node_to_remove.get_element()))
                self.tail = node_to_remove.get_previous()
                self.tail.set_next(None)
                self.number_elements-=1
                #print((self.tail.get_element()))
                return node_to_remove.get_element()
        except EmptyListException:
            print("EmptyList")

            # Removes and returns the element at the specified position in the list.

    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        try:
            if position < 0 or position >= self.size():
                raise InvalidPositionException
            else:
                if position == 0:
                    self.remove_first()
                elif position == self.size()-1:
                    self.remove_last()
                else:
                    new_pos = abs(self.size()/2)
                    if position>= new_pos:
                        aux = self.size()
                        node_to_iterate = self.tail
                        while node_to_iterate:
                            if aux == position:
                                node_to_remove = node_to_iterate
                                previous_node = node_to_remove.get_previous()
                                next_node = node_to_remove.get_next()
                                previous_node.set_next(next_node)
                                next_node.set_previous(previous_node)
                                #node_to_remove.set_next(None)
                                #node_to_remove.set_previous(None)
                                return node_to_remove.get_element()
                    elif position<new_pos:
                        aux = 0
                        node_to_iterate = self.head
                        while node_to_iterate:
                            if aux == position:
                                node_to_remove = node_to_iterate
                                previous_node = node_to_remove.get_previous()
                                next_node = node_to_remove.get_next()
                                previous_node.set_next(next_node)
                                next_node.set_previous(previous_node)
                                return node_to_remove.get_element()
        except InvalidPositionException:
            print("InvalidPosition")

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

    def print_list(self):
        node = self.head
        while node:
            print(node.get_element())
            node = node.get_next()
        print(self.number_elements)

if __name__ == "__main__":
    dlinked = DoubleLinkedList()
    dlinked.insert_first("A")
    dlinked.insert_last("B")
    # llist.insert("D",3)
    dlinked.insert("C", 1)
    dlinked.remove_last()
    #dlinked.iterator()
    dlinked.print_list()
    print("teste2")