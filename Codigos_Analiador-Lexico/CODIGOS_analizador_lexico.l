%{
#include <stdio.h>
%}

%x CADENA
%x FUNCION
%x TERMINAL
%x TERMINALL
%x VARIABLE

%%

"entero"    { printf("Palabra reservada: entero\n"); }
"buleano"   { printf("Palabra reservada: buleano\n"); }
"flotante"  { printf("Palabra reservada: flotante\n"); }
"SI"        { printf("Palabra reservada: SI\n"); }
"EntoCes"   { printf("Palabra reservada: EntoCes\n"); }
"Para"      { printf("Palabra reservada: Para\n"); }
"MiEntras"  { printf("Palabra reservada: MiEntras\n"); }
"+"         { printf("Operador Aritmético: +\n"); }
"*"         { printf("Operador Aritmético: *\n"); }
"-"         { printf("Operador Aritmético: -\n"); }
"/"         { printf("Operador Aritmético: /\n"); }
"<"        { printf("Operador Relacional Menor que: <.\n"); }
">"        { printf("Operador Relacional Mayor que: >.\n"); }
"(=3"       { printf("Operador Relacional Menor igual que: (=3\n"); }
"E=)"        { printf("Operador Relacional Mayor igual que: E=)\n"); }
"W"         { printf("Operador Relacional: W\n"); }
"!"         { printf("Operador Relacional diferente que: !\n"); }
"<="        { printf("Asignación: <=\n"); }
"UwU"       { printf("Delimitador: UwU\n"); }
"("         { printf("Delimitador: (\n"); }
")"         { printf("Delimitador: )\n"); }
";"         { printf("Delimitador: ;\n"); }
"\n"        { printf("Salto de línea: \\n\n"); }
"\t"        { printf("Enter: \\t\n"); }
" "         { /* Ignorar espacios en blanco */ }

".|."         { printf("Variable: "); BEGIN VARIABLE; }
<VARIABLE>[A-Za-z0-9]+   { printf("%s\n", yytext); BEGIN 0; }

"CaD"         { printf("Cadena: "); BEGIN CADENA; }
<CADENA>[A-Za-z0-9]+   { printf("%s", yytext); BEGIN TERMINAL; }
<TERMINAL>"UwU"         { printf("\n"); BEGIN 0; }

[0-9]+     { printf("Número: %s\n", yytext); }

":-*"         { printf("Función: "); BEGIN FUNCION; }
<FUNCION>[A-Za-z0-9]+   { printf("%s", yytext); BEGIN TERMINALL; }
<TERMINALL>"UwU"         { printf("\n"); BEGIN 0; }

.           { printf("Identificador: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}
