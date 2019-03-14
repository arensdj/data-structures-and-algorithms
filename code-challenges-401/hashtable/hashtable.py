
def add(item_list, key, value):
    item_list.append((key, value))
 
def get(item_list, key):
    for item in item_list:
        if item[0] == key:
            return item[1]
    
def hash(key):
    return key % len(hash_table)


def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key] = value 
 


if __name__ = "__main__":
    hash_table = [None] * 32
    print (hash_table) 

    pet_id = [('25', 'Sparky'), ('20', 'Leela'), ('10', 'Jonah')]

    print (get(pet_id, '20')) # Output: India
    print (add(pet_id, '100')) 

    # Output: None, python returns 'None' by default if the searched item is not found in the list

    insert(hash_table, 10, 'Nepal')
    print (hash_table)
    # Output: 
    # ['Nepal', None, None, None, None, None, None, None, None, None]
    
    insert(hash_table, 25, 'USA')
    print (hash_table)
    # Output: 
    # ['Nepal', None, None, None, None, 'USA', None, None, None, None]