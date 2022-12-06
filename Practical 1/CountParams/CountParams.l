%{
    #include<stdio.h>
    int words = 0;
    int lines = 0;
    int digits = 0;
    int questions = 0;
    int specialChar = 0;
    int smallChar = 0;
    int capitalChar = 0;
%}

%%
[0-9]"/"[0-9]"/"[2000-2100]+ {printf("Date : %s\n", yytext);}
["\n"] {lines++;}
[I|II|III|IV|VII|VIII|IX|X]+ {printf("Semesters : %s\n", yytext);}
[0-9]+ {digits++;}
[!@#$%^&*()?] {specialChar++;}
[a-z] {smallChar++;}
[A-Z] {capitalChar++;}
[" "] {words++;}
"Question"[1-9]+ {questions++;}
%%

int yywrap(void){

}

int main(){
    yyin = fopen("questions.txt", "r");
    yylex();

    printf("\nNum Digits : %d\n", digits);
    printf("\nNum Letters : %d\n", smallChar);
    printf("\nNum Capital Letters : %d\n", capitalChar);
    printf("\nNum Words : %d\n", words);
    printf("\nNum Lines : %d\n", lines);
    printf("\nNum Questions : %d\n", questions);

    return 0;
}