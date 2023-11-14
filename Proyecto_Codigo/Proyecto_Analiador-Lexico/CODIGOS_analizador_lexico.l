%{
#include <stdio.h>
%}

%x CADENA
%x FUNCION
%x TERMINAL
%x TERMINALL
%x VARIABLE

RESERVADAS "entero"|"buleano"|"flotante"|"SI"|"EntoCes"|"Para"|"MiEntras"
OP_ARITMETICO "+"|"-"|"*"|"/"
OP_RELACIONAL  "<"|">"|"(=3"|"E=)"|"!W"
ASIGNACION "<="
DELIMITADOR "UwU"|"("|")"|";"
ESPACIOBLANCO " "|"\t"
NUMERO [0-9]


%%

{RESERVADAS} { printf("Palabra reservada: %s\n",yytext); }

{OP_ARITMETICO}         { printf("Operador Aritmético: %s\n",yytext); }

{OP_RELACIONAL}       { printf("Operador Relacional: %s \n",yytext); }

{ASIGNACION}        { printf("Asignación: %s \n",yytext); }

{DELIMITADOR}       { printf("Delimitador: %s\n",yytext); }

"\n"        { printf("Salto de línea: \\n\n"); }
{ESPACIOBLANCO} {/* Ignorar */}

".|."         { printf("Variable: "); BEGIN VARIABLE; }
<VARIABLE>[A-Za-z0-9]+   { printf("%s\n", yytext); BEGIN 0; }

"CaD"         { printf("Cadena: "); BEGIN CADENA; }
<CADENA>[A-Za-z0-9]+   { printf("%s", yytext); BEGIN TERMINAL; }
<TERMINAL>"UwU"         { printf("\n"); BEGIN 0; }

{NUMERO}+     { printf("Número: %s\n", yytext); }

":-*"         { printf("Función: "); BEGIN FUNCION; }
<FUNCION>[A-Za-z0-9]+   { printf("%s", yytext); BEGIN TERMINALL; }
<TERMINALL>"UwU"         { printf("\n"); BEGIN 0; }

.           { printf("TOKEN INVALIDO"); }

%%

int main() {
    yylex();
    return 0;
}
