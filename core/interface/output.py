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


def output_all_premisses(data: list):
    sknf = data[0]
    additional_parts = data[1]
    for i in range(2 ** len(additional_parts)):
        output = sknf
        variant = bin(i)[2::]
        variant = variant[::-1]
        for j in range(len(variant)):
            if variant[j] == "1":
                output += additional_parts[j]
        print(output)
