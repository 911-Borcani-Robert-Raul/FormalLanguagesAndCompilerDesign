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
program : VAR decllist cmpdstmt END
decllist : multiple_declarations
multiple_declarations : declaration SEMICOLON | declaration SEMICOLON decllist
declaration : IDENTIFIER COLON type | STRUCT IDENTIFIER OPEN decllist CLOSE
type1 : CHAR | INTEGER | arraydecl
arraydecl : ARRAY OPENA INTCONSTANT CLOSEA OF type1
type  : type1
cmpdstmt : HASHTAG stmtlist MOD
stmtlist : stmt SEMICOLON | stmt SEMICOLON stmtlist
stmt : simplstmt | structstmt
simplstmt : assignstmt | iostmt | structaccessstmt
assignstmt : identif EQ expression
expression : expression PLUS term | expression MINUS term | term | MINUS term
term : term MOD factor | term TIMES factor | term DIV factor | factor | SQRT OPEN expression CLOSE
factor : OPEN expression CLOSE | identif
iostmt : READ OPEN identif CLOSE | WRITE OPEN IDENTIFIER CLOSE | WRITE OPEN STRINGCONSTANT CLOSE
structaccessstmt : identif DOT identif SEMICOLON
identif : INTCONSTANT | IDENTIFIER | IDENTIFIER OPENA INTCONSTANT CLOSEA | IDENTIFIER OPENA IDENTIFIER CLOSEA
structstmt : cmpdstmt | ifstmt | whilestmt
ifstmt : IF condition THEN stmtlist | IF condition THEN stmtlist EL stmtlist
whilestmt : WHILE condition REPEAT stmtlist
condition : expression RELATION expression
RELATION : LESS | LESSEQ | EQQ | LESS BIGGER | BIGGEREQ | BIGGER
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