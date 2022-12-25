from core.expression import Expression


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


def input_messages_consequence():
    print("Введите количество посылок")
    n_messages = int(input())
    messages = []
    for _ in range(n_messages):
        print("Введите посылку")
        message = Expression(str(input()).upper().replace(' ', ''))
        messages.append(message)
    print("Введите следствие")
    consequence = Expression(input_expression())
    return [messages, consequence]
