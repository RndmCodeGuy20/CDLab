/*Prints Line number of a line to stdout*/
%{
    #include <stdio.h>
%}
%%
[A-Z][a-z]+ {printf("Name : %s\n", yytext);}
%%
int main()
{
    yyin = fopen("file.txt", "r");
yylex();
return 0;
}

int yywrap(void){}