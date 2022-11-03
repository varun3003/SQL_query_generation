<<<<<<< Updated upstream

# CREATE query 
=======
# CREATE query
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    
# INSERT query 
def insert():
    table = input("Table name : ")
    cols = list(input("space separated column names :").split())
    data = []
    while True:
        line = input()
        if line:
            data.append(line)
        else:
            break
        
    #to_date(current_date,'dd/mm/yyyy')
    
    result = "INSERT INTO {} (".format(table)
    for i, col in enumerate(cols):
        result += col
        if i == len(cols)-1:
            result += ") values ("
        else:
            result += "' " 
    
    
    for values in data:
        if "Manager" in values:
            values = values.replace("Manager", "Manager NULL")
        values = values.split()
        
        result = "INSERT INTO {} (".format(table)
        for i, col in enumerate(cols):
            result += col
            if i == len(cols)-1:
                result += ") values ("
            else:
                result += ", "
        
        for value in values:
            print(value)
    
=======
>>>>>>> Stashed changes


# DRIVER CODE
command = input("command :")

if command == 'create':
<<<<<<< Updated upstream
    print(create())
elif command == 'insert':
    insert()




=======
    print(create())
>>>>>>> Stashed changes
