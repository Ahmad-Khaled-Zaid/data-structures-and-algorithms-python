class Node:
    """
    this class will instantiate a Node  with two attributes, value and next
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    this class will instantiate a LinkedList that have head attribute and insert method
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


class HashTable:
    """
    Hash Table is a Data structure that will store data in key and value pairs using buckets using 5 main methods
    set,get,hash,key to provide better efficiency
    """

    def __init__(self, size=1024):
        """
        Hash table constructor will take a size as an argument
        :param:size
        :return:None
        """
        self.size = size
        self.__buckets = [None] * self.size
        self.__keys = []

    def __hash(self, key):
        """
        this method will take a key as an argument and return  the index in the collection of buckets
        for the key
        :param key:
        :return:
        """
        return sum([ord(i) for i in key]) * 283 % self.size

    def set(self, key, value):
        hashed_key = self.__hash(key)
        if self.__buckets[hashed_key] is None:
            ll = LinkedList()
            self.__buckets[hashed_key] = ll
        self.__keys.append(key)
        self.__buckets[hashed_key].insert((key, value))

    def get(self, key):
        """
          Used to find the value that is associated with the passed key.
          :param key: Hash key
          :retern: referenced value by passed key
          """
        hashed_key = self.__hash(key)
        ll = self.__buckets[hashed_key]
        curr = ll.head
        while curr:
            if curr.value[0] == key:
                return curr.value[1]
            curr = curr.next

        return None

    def contains(self, key):
        """
           This method will take a key
           returns : True if the key exists in the hashmap, and False if it doesn't exist
           """
        hashed_key = self.__hash(key)
        ll = self.__buckets[hashed_key]
        if not ll:
            return False
        curr = ll.head
        while curr:
            if curr.value[0] == key:
                return True
            curr = curr.next
        return False

    def keys(self):
        """
           this method will return a collections of all the keys in hashmap as an object
           """
        return self.__keys


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.set("ahmad", "green")
    hash_table.set("sara", "red")
    hash_table.set("Mohammed", "black")
    print(hash_table.keys())
    print(hash_table.contains("d"))
    print(hash_table.get("ahmad"))
