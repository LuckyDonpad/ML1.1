from core.token import Token


class Expression(object):
    def __init__(self, infix=''):
        self.infix = infix.upper().replace(" ", "")  # выражение в инфиксной записи
        self.postfix = self.get_postfix(infix)  # выражение в ОПЗ
        self.variables_dict = self.get_variables_dict()  # словарь переменных

    # принимает выражение в инфиксной записи и возвращает это выражение в ОПЗ
    def get_postfix(self, infix: str):
        infix = list(self.infix)
        output = []
        stack = []
        # прочитать токен
        for token in infix:
            token = Token(token)
            # Если токен — число или переменная, то добавить его в очередь вывода
            if token.is_variable() or token.isnumeric():
                output.append(token)
            # Если токен — операция op1, то
            elif token.is_operation():
                # Пока на вершине стека присутствует токен-операция op2, и у op1 приоритет
                # меньше либо равен приоритету op2, переложить op2 из стека в выходную
                # очередь.
                while stack and stack[-1].is_operation() and (
                        token.get_priority() <= stack[-1].get_priority()):
                    output.append(stack.pop())
                # Положить op1 в стек
                stack.append(token)
            # Если токен — открывающая скобка, то положить его в стек.
            elif token == "(":
                stack.append(token)
            # Если токен — закрывающая скобка:
            elif token == ")":
                # Пока токен на вершине стека не является открывающей скобкой, перекладывать
                # токены-операции из стека в выходную очередь.
                while len(stack) > 0 and stack[-1] != '(':
                    output.append(stack.pop())
                # Если стек закончился до того, как был встречен токен-«открывающая скобка», то в
                # выражении пропущена открывающая скобка
                if len(stack) == 0:
                    raise SyntaxError("opening par is missing")
                # Выкинуть открывающую скобку из стека, но не добавлять в очередь вывода.
                else:
                    stack.pop()
        stack.reverse()
        # Если больше не осталось токенов на входе
        # Пока есть токены в стеке
        for token in stack:
            # Если токен на вершине стека — открывающая скобка, то в выражении
            # присутствует незакрытая скобка
            if token.token == '(':
                raise SyntaxError("closing par is missing")
            # Переложить токен-операцию из стека в выходную очередь
            output.append(token)
        return output

    # принимает строку-выражение, возвращает словарь где переменные - ключи, значение - 0
    def get_variables_dict(self):
        expression = sorted(self.infix)
        variables = {}
        for symbol in expression:
            if symbol.isalpha():
                variables[symbol] = 0
        return variables

    # ввод значений переменных с клавиатуры
    def input_values(self):
        for key in self.variables_dict.keys():
            print("Введите значение переменной", key)
            self.variables_dict[key] = int(input())

    # возвращает результат вычисления бинарной операции
    def evaluate_binary(self, a: bool, op: Token, b: bool):
        if op.token == "&":
            return a and b
        elif op.token == '|':
            return a or b
        elif op.token == '>':
            return not a or b
        elif op.token == '~':
            return (not a or b) and (a or not b)
        else:
            raise Exception

    # возвращает результат вычисления унарной операции
    def evaluate_unary(self, a: bool, op: Token):
        if op == '-':
            return not a
        else:
            raise Exception

    # возвращает результат вычисления выражения
    def evaluate(self):
        stack = []
        for token in self.postfix:
            if token.is_variable():
                stack.append(self.variables_dict[token.token])
            elif token.is_operation():
                if token.is_binary_operation():
                    b = bool(stack.pop())
                    a = bool(stack.pop())
                    stack.append(self.evaluate_binary(a, token, b))
                elif token.is_unary_operation():
                    a = bool(stack.pop())
                    stack.append(self.evaluate_unary(a, token))
                else:
                    raise Exception
        return stack[-1]

    # возвращает таблицу истинности в виде двумерного массива
    def evaluate_table(self):
        table = []
        for variant in range(2 ** len(self.variables_dict.keys())):
            variant = str(bin(variant))[2::]
            variant = '0' * (len(self.variables_dict) - len(variant)) + variant
            index = 0
            for key in self.variables_dict.keys():
                self.variables_dict[key] = int(variant[index])
                index += 1
            answer = self.evaluate()
            table.append([variant, bool(answer)])
        return table
