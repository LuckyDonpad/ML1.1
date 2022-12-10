# принимает таблицу истинности выражения и выводит на экран доказательство ее общезначимости выражения
def proof_general_validity(table: list[list]):
    validity = table[0][1]
    for row in table:
        if row[1] != validity:
            print(f"Т.к. вариант {row[0]} возвращает значение {row[1]}, "
                  f"а вариант {table[0][0]} возвращает значение {table[0][1]} "
                  f"выражение не является общезначимым")
            return
    print(f"Т.к. на всех вариантах выражение возвращает значение {validity}, является общезначимым")


# принимает таблицу истинности и выводит на экран все варианты на которых выражение возвращает ЛОЖЬ
def show_all_false(table: list[list]):
    falses = []
    for row in table:
        if not row[1]:
            falses.append(row[0])
    if len(falses) == 0:
        print("На всех вариантах выражение возвращает истину")
    else:
        print("Выражение возвращает ложь на данных варантах:")
        print(*falses, sep="\n")
