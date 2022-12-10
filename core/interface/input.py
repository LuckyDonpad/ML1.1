# возвращает логическое выражение введенное с клавиатуры в верхнем регистре без пробелов
def input_expression():
    print("Please input logical expression\n",
          "'~' - equal\n",
          "'>' - implication\n",
          "'|' - or\n",
          "'&' - and\n",
          "'-' - not\n")
    expression = str(input()).upper().replace(' ', '')
    return expression


# принимает словарь с переменными и заполняет его значениями введенными с клавиатуры
def input_values(variables) -> dict:
    for key in variables.keys():
        print("Введите значение переменной", key)
        variables[key] = int(input())
    return variables