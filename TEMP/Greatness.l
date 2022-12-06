%{
#include<stdio.h>
%}
%%

bool|int|float|switch|case|if|else|for|end|break printf("It is a Keyword");
[-,+]?[0-9]+ printf("Constants");
[,.'"]+ printf("Punctuation Chars");
[!@#$%^&*()]+ printf("Special Chars");
[a-zA-Z]+ printf("Identifiers");
%%

int main()
{
	yyin=fopen("input.txt","r");
	yylex();
}
int yywrap()
{
return(1);
}	