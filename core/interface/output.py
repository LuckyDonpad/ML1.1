# принимает таблицу истинности и словарь с именами переменых и выводит на экран
def output_table(table: list[list], variables: dict):
    for variable in variables.keys():
        print(variable, end=" ")
    print("Expression \n")
    for row in table:
        values = row[0]
        result = row[1]
        for value in values:
            print(value, end=" ")
        print(result)
    print("\n")
