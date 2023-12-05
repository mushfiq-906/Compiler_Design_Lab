def Validate(str):
    if not((str[0] >= 'a' and str[0] <= 'z')
		or (str[0] >= 'A' and str[0] <= 'Z')
		or str[0] == '_'):
        return False
    for i in range(1,len(str)):
        if not((str[i] >= 'a' and str[i] <= 'z')
			or (str[i] >= 'A' and str[i] <= 'Z')
			or (str[i] >= '0' and str[i] <= '9')
			or str[i] == '_'):
            return False
    return True

keyword = ["if","else","do","while","break","continue","int","double","float","return","char",
           "case","sizeof","long","short","typedef","switch","for","unsigned","void","static",
           "struct","goto","true","false","const","class","union","namespace","and","or"]

operator = ["+","-","/","*","++","--","<",">","<=",">=","==","!="]
operator_name =["addition","subtraction","division","multiplication","increment","decrement","less than","greater than","less equal","greater equal","equal","not equal"]


if __name__ == '__main__':
    while True:
        print("Enter any String: ")
        str = input().split()
        # if Validate(str) and str not in keyword:
        #     print(f'{str} is a valid identifier')
        # else:
        #     print(f'{str} is not a valid identifier')
        # index = operator.index(str)
        # print(operator_name[index])
        opr = []
        id = []
        for lexeme in str:
            if Validate(lexeme):
                id.append(lexeme)
            if lexeme in operator:
                opr.append(lexeme)
        if opr.__len__() == 0 and id.__len__()==0:
            if str[0][1] == "+" and str[0][2]=="+":
                id.append(str[0][0])
                opr.append("++")
            elif str[0][1] == "-" and str[0][2] == "-":
                id.append(str[0][0])
                opr.append("--")
            elif str[0][0] == "+" and str[0][1]=="+":
                id.append(str[0][2])
                opr.append("++")
            elif str[0][0] == "-" and str[0][1] == "-":
                id.append(str[0][2])
                opr.append("--")
        print(str)
        print(f"Identifier: {id}")
        print(f"Operator: {opr}")
