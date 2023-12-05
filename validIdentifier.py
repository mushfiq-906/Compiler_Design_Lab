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
           "case","sizeof","long","short","typedef","switch","for","unsigned","void","static","struct","goto","true","false",
           "const","class","union","namespace"]

if __name__ == '__main__':
    while True:
        print("Enter any String")
        str = input()
        if Validate(str) and str not in keyword:
            print(str + ' is a valid identifier')
        else:
            print(str + ' is not a valid identifier')
