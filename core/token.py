class Token(str):
    def __init__(self, token):
        self.token = token.upper().replace(' ', '')

    # Принимает токен
    # Возвращает значение Истина, если токен - операция, иначе Ложь
    def is_operation(self):
        assert len(self.token) == 1
        return self.token in "~>|&-"

    # Принимает токен
    # Возвращает значение Истина, если токен - переменная, иначе Ложь
    def is_variable(self):
        assert len(self.token) == 1
        return self.token.isalpha()

    # Принимает токен обозначающий операцию
    # Возвращает приоритет операции
    # приоритет - число от одного до пяти включительно: чем больше число, тем выше приоритет
    def get_priority(self):
        assert len(self.token) == 1
        if not Token.is_operation(self):
            raise SyntaxError("Undefined operation")
        return "~>|&-".find(self.token) + 1

    # Принимает токен обозначающий операцию
    # Возвращает значение Истина, если токен - бинарная операция, иначе Ложь
    def is_binary_operation(self):
        return self.token in "&|>~"

    # Принимает токен обозначающий операцию
    # Возвращает значение Истина, если токен - унарная операция, иначе Ложь
    def is_unary_operation(self):
        return self.token == '-'
