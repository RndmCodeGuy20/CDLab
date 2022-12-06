TAC = "C=A-B"

letter = [c for c in TAC]

# print(letter)

if (letter[3] == '+'):
    print(f"MOV R0, {letter[2]}\nADD R0, {letter[-1]}\nMOV {letter[0]}, R0")

elif (letter[3] == '-'):
    print(f"MOV R0, {letter[2]}\nSUBB R0, {letter[-1]}\nMOV {letter[0]}, R0")

elif (letter[3] == '/'):
    print(f"MOV R0, {letter[2]}\nDIV R0, {letter[-1]}\nMOV {letter[0]}, R0")

elif (letter[3] == '*'):
    print(f"MOV R0, {letter[2]}\nMUL R0, {letter[-1]}\nMOV {letter[0]}, R0")