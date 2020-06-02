# from .tad_dictionary import Dictionary
# from ..exceptions import NoSuchElementException, DuplicatedKeyException
# from ..lists.singly_linked_list import SinglyLinkedList

from aed_ds.dictionaries.tad_dictionary import Dictionary
from aed_ds.dictionaries.item import Item
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.exceptions import DuplicatedKeyException
from aed_ds.exceptions import NoSuchElementException
import ctypes


class HashTable(Dictionary):
    def __init__(self, size=101):
        self.limit = size
        self.current_number_of_elements = 0
        self.vec = (ctypes.py_object * size)()
        for a in range(self.limit):
            self.vec[a] = SinglyLinkedList()

    def hashing_func(self, key):
        return sum([ord(c) for c in key]) % self.limit

    def has_key(self,key,list_to_search):
        place_to_search = list_to_search
        piter = place_to_search.iterator()
        while piter.has_next():
            obj_to_compare = piter.next()
            if key == obj_to_compare.get_key():
                return obj_to_compare
            else:
                return False

    def size(self):
        return self.current_number_of_elements

    def is_full(self):
        if self.current_number_of_elements == self.limit:
            return True

    def get(self, k):
        hash_key = self.hashing_func(k)
        slot = self.vec[hash_key]
        element = self.has_key(k,slot)
        if not element:
            raise NoSuchElementException
        else:
            return element.get_value()

    def insert(self, k, v):
        hash_key = self.hashing_func(k)
        key_exists = False
        slot = self.vec[hash_key]
        item = Item(k, v)
        #need to check if the key in items already exists
        if slot.is_empty():
            slot.insert_first(item)
        else:
            true_key = self.has_key(k,slot)
            if true_key == False:
                slot.insert_first(item)
            else:
                raise DuplicatedKeyException
        self.current_number_of_elements+=1

    def update(self, k, v):
        hash_key = self.hashing_func(k)
        slot = self.vec[hash_key]
        if not self.has_key(k,slot):
            raise NoSuchElementException
        else:
            item_to_update = self.has_key(k,slot)
            item_to_update.set_value(v)

    def remove(self, k):
        hash_key = self.hashing_func(k)
        slot = self.vec[hash_key]
        list_iter = slot.iterator()
        position = 0
        while list_iter.has_next():
            if k == list_iter.next().get_key():
                slot.remove(position)
            else:
                position+=1
        self.current_number_of_elements-=1

    def keys(self):
        my_list = []
        for bucket in self.vec:
            bucket_iter = bucket.iterator()
            while bucket_iter.has_next():
                element = bucket_iter.next().get_key()
                my_list.append(element)
        return my_list

    def values(self):
        my_list = []
        for bucket in self.vec:
            bucket_iter = bucket.iterator()
            while bucket_iter.has_next():
                element = bucket_iter.next().get_value()
                my_list.append(element)
        return my_list

    def items(self):
        my_list_of_buckets = []
        for bucket in self.vec:
            bucket_iter = bucket.iterator()
            my_list_per_bucket = []
            while bucket_iter.has_next():
                key = bucket_iter.next().get_key()
                value = bucket_iter.next().get_value()
                kv = (key,value)
                my_list_per_bucket.append(kv)
            my_list_of_buckets.append(my_list_per_bucket)
