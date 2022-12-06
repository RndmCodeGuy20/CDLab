%{
#include<stdio.h>
#include<string.h>
int words=0;
int lines=0;
int digits=0;
int questions=0;
int specChar = 0;
int smallL = 0;
int capitalL = 0;
%}
%%

[0-9]"/"[0-9]"/"[2000-2100]+ printf("Date: %s\n",yytext);
["\n"] {lines++;}
[I|II|III|IV|V|VI|VII|VIII]+ printf("Semesters : %s\n",yytext);
[0-9]+ {digits++;}
[!@#$%^&*()#?] {specChar++;}
[a-z] {smallL++;}
[A-Z] {capitalL++;}
[" "] {words++;}
"Question"[1-9]+ {questions++;}
%%
int yywrap(void){}
int main(){
	yyin = fopen("text2.txt","r");
	yylex();
    printf("No. of Digits: %d\n",digits);
    printf("No. of Small Letters: %d\n",smallL);
    printf("No. of Capital Letters: %d\n",capitalL);
    printf("No. of Words: %d\n",words);
    printf("No. of Lines: %d\n",lines);
    printf("No. of Questions: %d\n",questions);
	return 0;
}