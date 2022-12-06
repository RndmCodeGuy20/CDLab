from tabulate import tabulate

ll1 = [["", "", "",
        "S->NP VP", "S-> NP VP", "S->NP VP",
        "S->NP VP", "S->NP VP", "S->NP VP", "S->NP VP", "S->NP VP",
        "S->NP VP", "S->NP VP", "S->NP VP",
        "S->NP VP", "S->NP VP", "S->NP VP"],

       ["", "", "", "",
        "", "", "", "NP->P",
        "NP->P", "NP->P", "NP->PN", "NP->PN",
        "NP->PN", "NP->PN", "NP->D N",
        "NP->D N", "NP->D N"],

       ["", "", "", "VP->VNP", "VP->V NP", "VP->V NP", "VP->VNP", "", "", "", "", "",
        "", "", "", "", ""],

       ["N->championship", "N->ball",
        "N->toss", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", ""],

       ["", "", "",
        "V->is", "V->want", "V->won",
        "V->played", "", "", "",
        "", "", "", "", "",
        "", ""],

       ["", "", "", "",
        "", "", "", "P->me",
        "P->I", "P->you", "", "",
        "", "", "", "", ""],

       ["", "", "", "",
        "", "", "", "", "",
        "", "PN->India", "PN->Australia",
        "PN->Steve", "PN->John", "", "",
        ""],

       ["", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "D->the", "D->a", "D->an"]]
head = ["Championship", "ball", "toss", "is", "want", "won", "Played", "me", "Won", "India", "Australia", "Steve",
        "John", "the", "you", "a", "an"]

print(tabulate(ll1, "grid"))
