# CREATE query
def create():
    table = input("Table name : ")
    cols = list(input("space separated column names :").split())
    sample = list(input("Space separated sample input : ").split())
    
    type = None    
    result = "CREATE " + table + "(\n"
    for i, col in enumerate(cols):
        if sample[i].isnumeric():
            type = "Number(10,3)"
        elif sample[i].isalpha():
            type = "Varchar2(10)"
        else:
            type = "Char({})".format(len(sample[i]))
            
        result += "{} {}".format(col, type)
        if i == 0:
            result += " Primary Key,\n"
        elif i == len(cols) - 1:
            result += "\n"
        else:
            result += ",\n"
    else:
        result += ");"
    return result


# DRIVER CODE
command = input("command :")

if command == 'create':
    print(create())
