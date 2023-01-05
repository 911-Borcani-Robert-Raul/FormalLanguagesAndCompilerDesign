/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     SQRT = 258,
     CHAR = 259,
     INTEGER = 260,
     IF = 261,
     THEN = 262,
     EL = 263,
     WHILE = 264,
     REPEAT = 265,
     VAR = 266,
     END = 267,
     SPACE = 268,
     READ = 269,
     WRITE = 270,
     STRUCT = 271,
     ARRAY = 272,
     OF = 273,
     IDENTIFIER = 274,
     INTCONSTANT = 275,
     STRINGCONSTANT = 276,
     PLUS = 277,
     MINUS = 278,
     TIMES = 279,
     DIV = 280,
     MOD = 281,
     EQ = 282,
     BIGGER = 283,
     BIGGEREQ = 284,
     LESS = 285,
     LESSEQ = 286,
     EQQ = 287,
     NEQ = 288,
     AND = 289,
     OR = 290,
     SEMICOLON = 291,
     COLON = 292,
     OPEN = 293,
     CLOSE = 294,
     OPENA = 295,
     CLOSEA = 296,
     BRACKETOPEN = 297,
     BRACKETCLOSE = 298,
     COMMA = 299,
     HASHTAG = 300,
     DOT = 301
   };
#endif
/* Tokens.  */
#define SQRT 258
#define CHAR 259
#define INTEGER 260
#define IF 261
#define THEN 262
#define EL 263
#define WHILE 264
#define REPEAT 265
#define VAR 266
#define END 267
#define SPACE 268
#define READ 269
#define WRITE 270
#define STRUCT 271
#define ARRAY 272
#define OF 273
#define IDENTIFIER 274
#define INTCONSTANT 275
#define STRINGCONSTANT 276
#define PLUS 277
#define MINUS 278
#define TIMES 279
#define DIV 280
#define MOD 281
#define EQ 282
#define BIGGER 283
#define BIGGEREQ 284
#define LESS 285
#define LESSEQ 286
#define EQQ 287
#define NEQ 288
#define AND 289
#define OR 290
#define SEMICOLON 291
#define COLON 292
#define OPEN 293
#define CLOSE 294
#define OPENA 295
#define CLOSEA 296
#define BRACKETOPEN 297
#define BRACKETCLOSE 298
#define COMMA 299
#define HASHTAG 300
#define DOT 301




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

