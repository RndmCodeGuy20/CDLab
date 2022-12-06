%{
    #include<stdio.h>
    int n = 0;
%}

%%
int | float | printf {n++; printf("%s is a keyword!\n", yytext);}
[a-zA-Z][a-zA-Z0-9]* {n++; printf("%s is an identifier!\n", yytext);}
[(|)|{|}|,|;|#|&] {n++; printf("%s is a symbol!\n", yytext);}
[=|++|-|*|+] {n++; printf("%s is an operator!\n", yytext);}
\".*\" {n++; printf("%s is a string!\n", yytext);}
\<.*\> {n++; printf("%s is a preprocessor directive!\n", yytext);}
%%

int main(){
    yyin = fopen("c-file.txt", "r");
    yylex();

    printf("\nTotal no. of tokens = %d\n", n);
    return 0;
}

int yywrap(void){}