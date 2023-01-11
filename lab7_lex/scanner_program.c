#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define DIM 1024*1024

int read_lines = 0;
char **string_symtable;
int len_string_symtable = DIM;
int string_symtable_pointer = 0;
char **identifier_symtable;
int len_identifier_symtable = DIM;
int identifier_sybtable_pointer = 0;
int *int_symtable;
int len_int_symtable = DIM;
int int_symtable_pointer = 0;
struct SymtableEntry{
    int code;       // 0 - token, 1 - identifier, 2 - int, 3 - string
    char *token;
    int position;
};
struct SymtableEntry* pif;
int len_pif = DIM;
int pointer_pif = 0;

void init_symbol_tables()
{
    string_symtable = malloc(len_string_symtable * sizeof(char*));
    identifier_symtable = malloc(len_identifier_symtable * sizeof(char*));
    int_symtable = malloc(len_int_symtable * sizeof(int));
    pif = malloc(len_pif * sizeof(struct SymtableEntry));
}

void add_string (char *string)
{
    string_symtable[string_symtable_pointer++] = string;
}

void add_identifier (char *identifier)
{
    identifier_symtable[identifier_sybtable_pointer++] = identifier;
}

void add_int (int number)
{
    int_symtable[int_symtable_pointer++] = number;
}

int add_string_and_get_string_index(char *string)
{
    for (int i = 0; i < string_symtable_pointer; ++i)
        if (strcmp(string, string_symtable[i]) == 0)
            return i;
    add_string(string);
    return string_symtable_pointer-1;
}

int add_identifier_and_get_identifier_index(char *identifier)
{
    for (int i = 0; i < identifier_sybtable_pointer; ++i)
        if (strcmp(identifier, identifier_symtable[i]) == 0)
            return i;
    add_identifier(identifier);
    return identifier_sybtable_pointer-1;
}

int add_int_and_get_int_index(char *number)
{
    int x = atoi(number); // NOLINT(cert-err34-c)
    for (int i = 0; i < int_symtable_pointer; ++i)
        if (x == int_symtable[i])
            return i;
    add_int(x);
    return int_symtable_pointer-1;
}

void add_to_pif(struct SymtableEntry entry)
{
    if (len_pif == pointer_pif) {
        struct SymtableEntry *new_pif = malloc(len_pif * 2 * sizeof (struct SymtableEntry));
        for (int i = 0; i < len_pif; ++i)
            new_pif[i] = pif[i];
        free(pif);
        len_pif *= 2;
        pif = new_pif;
    }
    pif[pointer_pif++] = entry;
}

struct SymtableEntry get_entry(int opcode, char *token, int pos) {
    struct SymtableEntry entry;
    entry.code = opcode;
    entry.position = pos;
    entry.token = token;
    return entry;
};

char* string_copy(char *string) {
    int size = (int)strlen(string);
    char* new_string = malloc((size+1) * sizeof (char));
    for (int i = 0; i <= size; ++i)
        new_string[i] = string[i];
    return new_string;
}