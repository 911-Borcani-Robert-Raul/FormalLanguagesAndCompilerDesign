import re
import typing

class SymbolTableEntry:
    def __init__(self, key: str, position: int):
        self.key = key
        self.position = position
    
    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.position) + ')' + '\n'

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
        self._buckets = [[] for _ in range(number_of_buckets)]
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

        return (position, len(self._buckets[position]) - 1)

    def find(self, key: str):
        """
        Finds a key of an entry in the Symbol Table.
        Parameters:
            :key: The key for which we search in the symbol table
        Return value:
            The position of the found key. If the key is not found, returns -2
        """
        position = SymbolTable._string_hash(key) % self._number_of_buckets

        for values_index in range(len(self._buckets[position])):
            values = self._buckets[position][values_index]
            if values.key == key:
                return (position, values_index)
        
        return -2

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
    
    def __str__(self):
        result = ''
        for bucket in self._buckets:
            for entry in bucket:
                result += str(entry)

        return result

tokens_file = '/Users/robert-raulborcani/Documents/Facultate/Anul_III/SEM_1/FLCD/FormalLanguagesAndCompilerDesign/lab2/token.in'
tokens = []

with open(tokens_file, 'r') as tokens_file:
    tokens = [token.strip("\n") for token in tokens_file.readlines()]


def is_number(token):
    if token[0] in '+-':
        token = token[1:]
    if token == '0':
        return True
    if token[0] == '0':
        return False
    for char in token:
        if char not in '0123456789':
            return False
    return True


def is_string(token):
    if token[0] != '"' or token[-1] != '"':
        return False
    return True


def is_constant(token):
    return is_number(token) or is_string(token)


def is_identifier(token):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQSTUVWXYZ_'
    digits = '0123456789'
    if token[0] not in characters:
        return False
    for char in token:
        if char not in characters and char not in digits:
            return False
    return True


def scan(code, tokens, identifiers, constants, pif):
    """
    Scans the fiven code using the given tokens
    Parameters:
        :code: a list of strings representing the code to be scanned, one string per line
        :tokens: a list of tokens for the language
        :identifiers: a SymbolTable where identifiers will be placed
        :constants: a SymbolTable where constants will be placed
        :pif: a list denoting the PIF
    Return value:
        String "lexically correct" if the program was succesfully scanned and not errors were found
        String "lexical error: " followed by found errors if errors were found
    """
    error_found = False
    line_index = 0
    errors_string = ''

    for line_index in range(len(code)):
        line = code[line_index]
        line_with_tokens_separated = ''
        separators = ";:()[]+-"

        char_index = 0
        while char_index < len(line):
            char = line[char_index]
            if char == '"':
                char_index += 1
                line_with_tokens_separated += '$"'
                while line[char_index] != '"':
                    line_with_tokens_separated += line[char_index]
                    char_index += 1
                line_with_tokens_separated += '"$'
                char_index += 1
                continue
            if char == ' ':
                line_with_tokens_separated += '$'
            elif char in separators:
                line_with_tokens_separated += '$' + char + '$'
            else:
                line_with_tokens_separated += char
            char_index += 1

        separators = r"\$"
        code_tokens = re.split(separators, line_with_tokens_separated)
        for token_index in range(len(code_tokens)):
            token = code_tokens[token_index]
            token = token.strip(' \t\n')
            if token == '':
                continue

            if token in tokens:
                pif.append((token, -1))
            else:
                if is_identifier(token):
                    pos = identifiers.find(token)
                    if pos == -2:
                        pos = identifiers.insert(token)
                    pif.append(('__id_identifier', pos))
                elif is_constant(token):
                    pos = constants.find(token)
                    if pos == -2:
                        pos = constants.insert(token)
                    pif.append(("__id_constant", pos))
                else:
                    errors_string += f'Error at line {line_index + 1}: unexpected token {token}\n'
                    error_found = True
    
    if error_found:
        return "lexical error: " + errors_string
    else:
        return "lexically correct"


code_file_p1 = '/Users/robert-raulborcani/Documents/Facultate/Anul_III/SEM_1/FLCD/FormalLanguagesAndCompilerDesign/lab1/p1.ppc'
code_file_p1err = '/Users/robert-raulborcani/Documents/Facultate/Anul_III/SEM_1/FLCD/FormalLanguagesAndCompilerDesign/lab1/p1err.ppc'
code_file_p2 = '/Users/robert-raulborcani/Documents/Facultate/Anul_III/SEM_1/FLCD/FormalLanguagesAndCompilerDesign/lab1/p2.ppc'
code_file_p3 = '/Users/robert-raulborcani/Documents/Facultate/Anul_III/SEM_1/FLCD/FormalLanguagesAndCompilerDesign/lab1/p3.ppc'


with open(code_file_p1, 'r') as code_file:
    code = code_file.readlines()
    identifiers = SymbolTable()
    constants = SymbolTable()
    pif = []

    message = scan(code, tokens, identifiers, constants, pif)
    print(message)

    with open("PIF.OUT", 'w') as f:
        pif_string = ''
        for entry in pif:
            pif_string += str(entry) + '\n'
        f.write(pif_string)
    
    with open("ST.OUT", 'w') as f:
        f.write("IDENTIFIERS:\n" + str(identifiers) + "\n"
                + "CONSTANTS:\n" + str(constants)) 
