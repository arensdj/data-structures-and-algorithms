class Hashtable:
    def __init__(self):
        self.array = [None] * 1024

    def hash(self, key):
        # get the ascii code of each character in key and sum them
        sum = self.ascii(key)
        multiple_of_prime = sum * 599
        safe_index = multiple_of_prime // 1024
        # print(self.array)
        return safe_index

    def add(self, key, value):
        index = hash(key)
        # If no bucket at that index then create one and insert it there

        self.array.append((key, value))
        # print(self.array)

    def get(self, key):
        index = hash(key)
        
    def ascii(self, s):
        char_sum = 0
        for char in (s):
            char_sum += ord(char)
        return char_sum


if "__name" == "__main__":
    ht = Hashtable()
    key = ht.hash('dog')
    ht.add(key, 'woof')

    key = ht.hash('cat')
    ht.add(key, 'meow')

    print(ht.array)

#     HT = HashTable()
#     # print(_array)

#     # HT.add(10, bar)
#     # HT.add(20, baz)
#     # print(HT.get(10))

#     HT.add(‘foo’,’bar’)
#     HT.add(‘oof’,’baz’)
#     print(HT.get(‘foo’))










# def get(item_list, key):
#     for item in item_list:
#         if item[0] == key:
#             return item[1]
    
# def hashing_func(key):
#     return key % len(hash_table)

# def insert(hash_table, key, value):
#     hash_key = hashing_func(key)
#     hash_table[hash_key] = value 

# def search(hash_table, key):
#     hash_key = hash(key) % len(hash_table)    
#     bucket = hash_table[hash_key]
#     for i, kv in enumerate(bucket):
#         k, v = kv
#         if key == k:
#             return v

# hash_table = [None] * 32


# if __name__ == "__main__":
#     insert(hash_table, 10, 'Giraffe')
#     insert(hash_table, 25, 'Lion')
#     insert(hash_table, 30, 'Tiger')
#     print (hash_table)

#     # print(get(hash_table, 10))

#     # print (search(hash_table, 10)) # Output: Nepal
#     # print (search(hash_table, 25)) # Output: India
#     # print (search(hash_table, 30)) # Output: None

#     # pet_id = [('25', 'Sparky'), ('20', 'Leela'), ('10', 'Jonah')]

#     # print (get(pet_id, '20')) # Output: India
#     # print (add(pet_id, '100', 'Annie')) 

#     # Output: None, python returns 'None' by default if the searched item is not found in the list

#     # insert(hash_table, 25, 'USA')
#     # print (hash_table)
#     # Output: 
#     # ['Nepal', None, None, None, None, 'USA', None, None, None, None]