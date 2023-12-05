from tabulate import tabulate

def Is_Alpha(ch):
    if ((ch >= 'a' and ch <= 'z')
		or (ch >= 'A' and ch <= 'Z')
		or ch == '_'):
        return True
    return False

keyword = ["if","else","do","while","break","continue","int","double","float","return","char",
           "case","sizeof","long","short","typedef","switch","for","unsigned","void","static",
           "struct","goto","true","false","const","class","union","namespace","and","or"]

number = "0123456789"

operator = {
    "+":"addition",
    "-":"subtraction",
    "/":"division",
    "*":"multiplication",
    "%": "modulus",
    "=":"assignment operator",
    "++":"increment",
    "--":"decrement",
    "<": "less than",
    ">":"greater than",
    "<=":"less equal",
    ">=":"greater equal",
    "==":"equal",
    "!=":"not equal",
    "+=":"add and assign",
    "-=":"subtract and assign",
    "*=":"multiply and assign",
    "/=":"divide and assign",
    "&&": "logical and",
    "||": "logical or",
    "!": "logical not"
}

delimiter={
    ",": "comma",
    ";": "semicolon",
    "(": "opening braces",
    ")": "closing braces",
    "{": "left curly braces",
    "}": "right curly braces"
}


if __name__ == '__main__':
    file = open('../input.txt','r')
    lines = file.read().split()
    print(lines)
    table = [["Lexeme","Token Name","Attribute Value"]]
    for str in lines:

        if str in keyword:
            tr = [str,"Keyword","Null"]
            table.append(tr)
            # print(f"Lexeme:{str}   Token Name: Keyword   Attribute Value: null")
        elif str in operator:
            tr = [str, "Operator", operator[str]]
            table.append(tr)
            # print(f"Lexeme:{str}   Token Name: Operator   Attribute Value: {operator[str[0]]}")
        elif str in delimiter:
            tr = [str, "Special Symbol", delimiter[str[0]]]
            table.append(tr)
            # print(f"Lexeme:{str}   Token Name: Special Symbol   Attribute Value:{delimiter[str[0]]}")
        elif str[0]=='/' and (str[1]=='/' or str[1]=='*'):
            continue
        else:
            opr = []
            id = []
            oper = 0
            x = ""
            y = ""
            num = ""
            for ch in str:
                if Is_Alpha(ch):
                    if y!= "":
                        tr = [y,"Operator",operator[y]]
                        table.append(tr)
                        # print(f"Lexeme:{y}   Token Name: Operator   Attribute Value: {operator[y]}")
                        y = ""
                    x += ch
                elif ch in operator:
                    if x != "":
                        tr = [x, "Identifier", "pointer to symbol table entry"]
                        table.append(tr)
                        # print(f"Lexeme:{x}   Token Name: Identifier   Attribute Value: pointer to symbol table entry")
                        x = ""
                    if num != "":
                        tr = [num, "Number", "Constant"]
                        table.append(tr)
                        # print(f"Lexeme:{num}   Token Name: Number   Attribute Value: Constant")
                        num = ""
                    y += ch

                elif ch in delimiter:
                    if x != "":
                        tr = [x, "Identifier", "pointer to symbol table entry"]
                        table.append(tr)
                        # print(f"Lexeme:{x}   Token Name: Identifier   Attribute Value: pointer to symbol table entry")
                        x = ""
                    if y != "":
                        tr = [y, "Operator", operator[y]]
                        table.append(tr)
                        # print(f"Lexeme:{y}   Token Name: Operator   Attribute Value: {operator[y]}")
                        y = ""
                    if num != "":
                        tr = [num, "Number", "Constant"]
                        table.append(tr)
                        # print(f"Lexeme:{num}   Token Name: Number   Attribute Value: Constant")
                        num = ""
                    tr = [ch,"Special Symbol",delimiter[ch]]
                    table.append(tr)
                    # print(f"Lexeme:{ch}   Token Name: Special Symbol   Attribute Value:{delimiter[ch]}")

                elif ch in number:
                    num += ch

            if x != "":
                tr = [x, "Identifier", "pointer to symbol table entry"]
                table.append(tr)
                # print(f"Lexeme:{x}   Token Name: Identifier   Attribute Value: pointer to symbol table entry")
            if y != "":
                tr = [y, "Operator", operator[y]]
                table.append(tr)
                # print(f"Lexeme:{y}   Token Name: Operator   Attribute Value: {operator[y]}")
            if num !="":
                tr = [num, "Number", "Constant"]
                table.append(tr)
                # print(f"Lexeme:{num}   Token Name: Number   Attribute Value: Constant")
    print(tabulate(table,headers = "firstrow"))
