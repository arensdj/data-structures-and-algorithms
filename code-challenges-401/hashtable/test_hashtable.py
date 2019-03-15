from hashtable import Hashtable

def test_class():
    assert Hashtable

def test_instantiation():
    assert Hashtable()

def test_create_hash():
    ht = Hashtable()
    actual = ht.hash('dog')

    assert actual == 183

def test_add_to_hashtable():
    ht = Hashtable()
    key = ht.hash('dog')
    ht.add(key, 'woof')

    key = ht.hash('cat')
    ht.add(key, 'meow')

    index = ht.get(key)
    # ht.get(key)
    assert index == 50
    


# def test_insert_into_hashtable():
#     hash_table = [None] * 32

#     insert(hash_table, 10, 'Giraffe')

#     print(hash_table)


