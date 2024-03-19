class HashMap:

    MAXIMUM_LOAD_FACTOR = .75

    class _Item:

        def __init__(self, key, value=None):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self.key < other.key

    def __init__(self):
        self._hash_table = [] # there are better ways
        for bucket in range(11):
            self._hash_table.append([])

        # 11 lists in my hash table
        self._number_of_items = 0

    def _resize(self):
        new_hash_table = []
        for bucket in range(2*len(self._hash_table)):
            new_hash_table.append([])
        for bucket in self._hash_table:
            for item in bucket:
                new_index = hash(item.key) % len(new_hash_table)
                new_hash_table[new_index].append(item)
        self._hash_table = new_hash_table

    # O(1) - constant hash and calculate index, get the item from the bucket
    def __setitem__(self, key, value):
        bucket_index = hash(key) % len(self._hash_table)
        for items in self._hash_table[bucket_index]:
            if items.key == key:
                old_value = items.value
                items.value = value
                return old_value

        # if we didn't update a value, add a new Key/Value pair
        self._hash_table[bucket_index].append(self._Item(key, value))
        self._number_of_items += 1

        if self._number_of_items / len(self._hash_table) > self.MAXIMUM_LOAD_FACTOR:
            self._resize()

    # O(1)
    def __getitem__(self, key):
        bucket_index = hash(key) % len(self._hash_table)
        for item in self._hash_table[bucket_index]:
            if item.key == key:
                return item.value
        raise KeyError

    # O(1)
    def __delitem__(self, key):
        bucket_index = hash(key) % len(self._hash_table)
        for item in self._hash_table[bucket_index]:
            if item.key == key:
                value = item.value
                item_to_delete = self._Item(key)
                self._hash_table[bucket_index].remove(item_to_delete)
                self._number_of_items -= 1
                return value
        raise KeyError

    def __len__(self):
        return self._number_of_items

    def __iter__(self):
        for bucket_index in range(len(self._hash_table)):  # scan entire table
            for item in self._hash_table[bucket_index]:
                yield item.key



class Assignment:

    def __init__(self, name, score):
        self._name = name
        self.score = score

    def __hash__(self):
        # hash values have to be based on immutable properties only
        return hash(self._name) #+ hash(self.score)
        # return 0 # this is terrible, they will all end int eh same bucket

    def __eq__(self, other):
        return self.name == other.name and self.score == other.score

first_quiz = Assignment("Quiz 1", 10)
second_quiz = Assignment("Quiz 1", 10)
#print(hash(first_quiz))
#print(hash(second_quiz))

second_quiz = first_quiz
#print(hash(first_quiz))
#print(hash(second_quiz))

gradebook = { first_quiz : 10 }

gradebook['Eric'] = 10
gradebook['Jeb'] = 10

customBook = HashMap()
customBook['Eric'] = 10
customBook['Jeb'] = 10


for item in customBook:
    print(item)