
# def add(item_list, key, value):
#     item_list.append((key, value))
 
def get(item_list, key):
    for item in item_list:
        if item[0] == key:
            return item[1]
    

def hashing_func(key):
    return key % len(hash_table)

# def add(hash_table, key, value):
#     hash_key = hashing_func(key)
#     hash_table[hash_key] = value 
 

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key] = value 

def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

hash_table = [None] * 32


if __name__ == "__main__":
    # print (hash_table) 

    # print (hash_table)
    # Output: 
    # ['Nepal', None, None, None, None, None, None, None, None, None]

    insert(hash_table, 10, 'Giraffe')
    insert(hash_table, 25, 'Lion')
    insert(hash_table, 30, 'Tiger')
    print (hash_table)

    print(get(hash_table, 10))

    # print (search(hash_table, 10)) # Output: Nepal
    # print (search(hash_table, 25)) # Output: India
    # print (search(hash_table, 30)) # Output: None

    # pet_id = [('25', 'Sparky'), ('20', 'Leela'), ('10', 'Jonah')]

    # print (get(pet_id, '20')) # Output: India
    # print (add(pet_id, '100', 'Annie')) 

    # # Output: None, python returns 'None' by default if the searched item is not found in the list

    # insert(hash_table, 25, 'USA')
    # print (hash_table)
    # # Output: 
    # # ['Nepal', None, None, None, None, 'USA', None, None, None, None]