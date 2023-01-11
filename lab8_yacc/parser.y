%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%{
int yylex();
void yyerror(const char *s);
%}

%token SQRT
%token CHAR
%token INTEGER
%token IF
%token THEN
%token EL
%token WHILE
%token REPEAT
%token VAR
%token END
%token SPACE
%token READ
%token WRITE
%token STRUCT
%token ARRAY
%token OF

%token IDENTIFIER;
%token INTCONSTANT;
%token STRINGCONSTANT;

%token PLUS;
%token MINUS;
%token TIMES;
%token DIV;
%token MOD;
%token EQ;
%token BIGGER;
%token BIGGEREQ;
%token LESS;
%token LESSEQ;
%token EQQ;
%token NEQ;
%token AND;
%token OR;

%token SEMICOLON;
%token COLON;
%token OPEN;
%token CLOSE;
%token OPENA;
%token CLOSEA;
%token BRACKETOPEN;
%token BRACKETCLOSE;
%token COMMA;
%token HASHTAG
%token DOT

%start program 

%%
program : VAR decllist cmpdstmt END {printf("program -> 'var' decllist cmpdstmt 'end'\n");}
decllist : multiple_declarations {printf("decllist -> multiple_declarations\n");}
multiple_declarations : declaration SEMICOLON {printf("mutiple_declarations -> declaration ';'\n");} | declaration SEMICOLON decllist {printf("multiple_declarations -> declaration ';' decllist\n");}
declaration : IDENTIFIER COLON type {printf("declaration -> IDENTIFIER ',' type\n");} | STRUCT IDENTIFIER OPEN decllist CLOSE {printf("declaration -> STRUCT IDENTIFIER '(' decllist ')'\n");}
type1 : CHAR {printf("type1 -> CHAR\n");} | INTEGER {printf("type1 -> INTEGER\n");} | arraydecl {printf("type1 -> arraydecl\n");}
arraydecl : ARRAY OPENA INTCONSTANT CLOSEA OF type1 {printf("arraydecl -> ARRAY '[' INTCONSTANT ']' 'of' type1\n");}
type  : type1 {printf("type -> type1\n");}
cmpdstmt : HASHTAG stmtlist MOD {printf("cmpdstmt -> '#' stmtlist 'MOD'\n");}
stmtlist : stmt SEMICOLON {printf("stmtlist -> stmt ';'\n");} | stmt SEMICOLON stmtlist {printf("stmtlist -> stmt ';' stmtlist\n");}
stmt : simplstmt {printf("stmt -> simplstmt\n");} | structstmt {printf("stmt -> structstmt\n");}
simplstmt : assignstmt {printf("simplstmt -> assignstmt\n");} | iostmt {printf("simplstmt -> iostmt\n");} | structaccessstmt {printf("simplstmt -> structaccessstmt\n");}
assignstmt : identif EQ expression {printf("assignstmt -> identif '=' expression\n");}
expression : expression PLUS term {printf("expression -> expression '+' term\n");} | expression MINUS term {printf("expression -> expression '-' term\n");} | term {printf("expression -> term\n");} | MINUS term {printf("expression -> '-' term\n");}
term : term MOD factor {printf("term -> term 'MOD' factor\n");} | term TIMES factor {printf("term -> term '*' factor\n");} | term DIV factor {printf("term -> term '/' factor\n");} | factor {printf("term -> factor\n");} | SQRT OPEN expression CLOSE {printf("decllist -> 'sqrt' '(' expression ')'\n");}
factor : OPEN expression CLOSE {printf("factor -> '(' expression ')'\n");} | identif {printf("factor -> identif\n");}
iostmt : READ OPEN identif CLOSE {printf("iostmt -> 'read' '(' identif ')'\n");} | WRITE OPEN IDENTIFIER CLOSE {printf("iostmt -> 'write' '(' IDENTIFIER ')'\n");} | WRITE OPEN STRINGCONSTANT CLOSE {printf("iostmt -> 'write' '(' STRINGCONST ')'\n");}
structaccessstmt : identif DOT identif SEMICOLON {printf("structaccessstmt -> identif '.' identif ';'\n");}
identif : INTCONSTANT {printf("identif -> INTCONSTANT\n");} | IDENTIFIER {printf("identif -> IDENTIFIER\n");} | IDENTIFIER OPENA INTCONSTANT CLOSEA {printf("identif -> IDENTIFIER '[' INTCONSTANT ']'\n");} | IDENTIFIER OPENA IDENTIFIER CLOSEA {printf("identif -> IDENTIFIER '[' IDENTIFIER ']'\n");}
structstmt : cmpdstmt {printf("structstmt -> cmpdstmt\n");} | ifstmt {printf("structstmt -> ifstmt\n");} | whilestmt {printf("structstmt -> whilestmt\n");}
ifstmt : IF condition THEN stmtlist {printf("ifstmt -> 'if' condition 'then' stmtlist\n");} | IF condition THEN stmtlist EL stmtlist {printf("ifstmt -> 'if' condition 'then' stmtlist 'el' stmtlist\n");}
whilestmt : WHILE condition REPEAT stmtlist {printf("whilestmt -> 'while' condition 'repeat' stmtlist\n");}
condition : expression RELATION expression {printf("condition -> expression relation expression\n");}
RELATION : LESS {printf("relation -> '<'\n");} | LESSEQ {printf("relation -> '<='\n");} | EQQ {printf("relation -> '=='\n");} | LESS BIGGER {printf("relation -> '<>'\n");} | BIGGEREQ {printf("relation -> '>='\n");} | BIGGER {printf("relation -> '>'\n");}
%%
void yyerror(const char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

int main(int argc, char **argv)
{
	if(argc>1) yyin =  fopen(argv[1],"r");
	if(!yyparse()) fprintf(stderr, "\tOK\n");
} 