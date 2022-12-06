SDTIndex = {

}

assignment = "a = b + c"
inc = "a++"
dec = "a--"
whileSt = "while(cond)"
cond = "a<=b"


def handleLoop(strBody):
    pass


def main():
    # handleAssignmentOperator(assignment)
    handleIncrementDecrement(inc)
    handleIncrementDecrement(dec)


def handleAssignmentOperator(strBody):
    ass_str = strBody
    temp = ass_str.split(" ")
    SDTIndex[101] = f"{101}. T{1} = {temp[2]} + {temp[4]}"
    SDTIndex[102] = f"{102}. T{1} = {temp[0]}"

    print(SDTIndex)


def handleConditional(strBody):
    ass_str = strBody
    temp = ass_str.split(" ")
    SDTIndex[101] = f"{101}. T{1} = {temp[2]} + {temp[4]}"
    SDTIndex[102] = f"{102}. T{1} = {temp[0]}"

    print(SDTIndex)


def handleIncrementDecrement(strBody):
    ass_str = strBody
    temp = ""
    if ass_str[1] == "+":
        SDTIndex[101] = f"{101}. T{1} = {ass_str[0]} + 1"

    if ass_str[1] == "-":
        SDTIndex[101] = f"{101}. T{1} = {ass_str[0]} - 1"

    print(SDTIndex)
    # SDTIndex[101] = f"{101}. T{1} = {temp[2]} + 1"
    # SDTIndex[102] = f"{102}. T{1} = {temp[0]}"

    # print(SDTIndex)


if __name__ == '__main__':
    main()
