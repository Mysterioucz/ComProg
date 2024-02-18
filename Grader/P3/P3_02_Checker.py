import string
pos = input().strip()
def main():
    row_pos = string.ascii_letters.find(row)
    if row_pos%2 == int(col)%2:
        print("Black")
    else:
        print("White")
        
if len(pos) <= 3:
    row,col = pos[0],pos[1:].strip()
    if col.isnumeric():check_col= 1<=int(col)<=52
    else: check_col= False
    if not row.isalpha() and not check_col:
        print("Invalid row and column")
    elif not row.isalpha():
        print("Invalid row")
    elif not check_col:
        print("Invalid column")
    else:
        main()
else:
    pos = pos.split(",")
    for e in pos:
        if "row" in e:
            eq1 = e.find("=")+1
            row = e[eq1:].strip()
        elif "col" in e:
            eq2 = e.find("=")+1
            col = e[eq2:].strip()
    if col.isnumeric():check_col= (1<=int(col)<=52)
    else: check_col= False
    if (not row.isalpha() and not check_col)or(len(row)>1 and not check_col):
        print("Invalid row and column")
    elif (not row.isalpha()) or len(row)>1:
        print("Invalid row")
    elif not check_col:
        print("Invalid column")
    else:
        if not 1<=int(col)<=52:
            print("Invalid column")
        else:
            main()
