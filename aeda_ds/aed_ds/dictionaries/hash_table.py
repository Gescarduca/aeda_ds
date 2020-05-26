#from .tad_dictionary import Dictionary
#from ..exceptions import NoSuchElementException, DuplicatedKeyException
#from ..lists.singly_linked_list import SinglyLinkedList
from aeda_ds.aed_ds.dictionaries.tad_dictionary import Dictionary
from aeda_ds.aed_ds.dictionaries.item import Item

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.limit = size
        self.current_number_of_elements = 0
        #self.my_dict = {}
        self.hashmap = [[] for in range(0, self.size)]

    def hashing_func(self, key):
        return sum([ord(c) for c in key])% self.size

    def size(self):
        return self.limit

    def is_full(self): 
        if self.current_number_of_elements == limit:
            return True

    def get(self, key):
        hash_key = self.hashing_func(key)
        slot = self.my_dict[hash_key]
        for kv in slot:
            k, v  = kv
            if key == k:
                return v
            else:
                raise KeyError("Does not exist")

    def insert(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        #slot = self.my_dict[hash_key]
        slot = self.hashmap[hash_key]
        item = Item(key,value)
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
           # slot[i] = ((key, value))
           slot[i] =  item
        else:
            #slot.append((key, value))
            slot.append(item)


    def update(self, k, v): pass

    def remove(self, key):
        hash_key = self.hashing_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if k == key:
                key_exists = True
                break
        if key_exists:
            slot.remove

    def keys(self): pass

    def values(self): pass

    def items(self): pass

d = HashTable()
print(d)