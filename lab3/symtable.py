import typing

class SymbolTableEntry:
    def __init__(self, key: str, position: int):
        self.key = key
        self.position = position

class SymbolTable:
    """
    This is a data structure that contains the symbol table, which is a table that links a key of type string (identifier) to a position in the symbol table
    """
    def __init__(self, number_of_buckets=1000):
        """
        Creates a new SymbolTable that uses a Hashtable as a data structure
        Parameters:
            :number_of_buckets: Can be set to manually set the number of buckets of the hash table
        """
        self._number_of_buckets = number_of_buckets
        self._buckets = [[]] * number_of_buckets
        self._next_key = 1

    def insert(self, value: str):
        """
        Inserts a new entry in the symtable.
        Parameters:
            :entry: an object of type SymbolTableEntry, the entry to be inserted
        Return value:
            The position of the inserted element
        """
        entry: SymbolTableEntry = SymbolTableEntry(value, self._next_key)
        self._next_key += 1

        position = SymbolTable._string_hash(entry.key) % self._number_of_buckets
        self._buckets[position].append(entry)

        return entry.position

    def find(self, key: str):
        """
        Finds a key of an entry in the Symbol Table.
        Parameters:
            :key: The key for which we search in the symbol table
        Return value:
            The position of the found key. If the key is not found, returns -2
        """
        position = SymbolTable._string_hash(key) % self._number_of_buckets

        for values in self._buckets[position]:
            if values.key == key:
                return values.position
        
        return -2
    
    def find_by_bucket_and_position(self, bucket_index, position_index):
        """
        Finds the key found at bucket_index and position_index
        Parameters:
            :bucket_index: the index of the bucket
            :position_index: the index of the position in the bucket
        Return value:
            The found key. Throws IndexOutOfBounds if the indexes are not in the ranges of the bucket
        """
        return self._buckets[bucket_index][position_index].key

    def _string_hash(string: str, p=7):
        """
        Computes a hash of a string
        Parameters:
            :string: The string for which we want to compute the hash
            :p: A value that can be set to get different hash functions (recommended to be prime)
        Return value:
            A number representing the hash of the given string
        """
        result = 0
        multiplicator = p
        for char in string:
            result += ord(char) * multiplicator
            multiplicator *= p
        
        return result

def test_symbol_table():
    print("BEGIN TESTING")
    symtable: SymbolTable = SymbolTable()

    v1 = 'ana'
    v2 = 'are'
    v3 = 'mere'
    v4 = '32432'

    p1 = symtable.insert(v1)
    p2 = symtable.insert(v2)
    p3 = symtable.insert(v3)
    p4 = symtable.insert(v4)

    assert(symtable.find('ana') == p1)
    assert(symtable.find('mere') == p3)
    assert(symtable.find('are') == p2)
    assert(symtable.find('') == -2)
    assert(symtable.find('jsgh') == -2)
    assert(symtable.find(v4) == p4)

    print("END TESTING")
            

test_symbol_table()

# This is how the code can look like when defining separate Symbol Tables for identifiers and constants
identifiers_symtable: SymbolTable = SymbolTable()
constants_symtable: SymbolTable = SymbolTable()
