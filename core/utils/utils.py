from copy import deepcopy


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


def get_part_cnf(variant: str, variables_dict: dict):
    variables = []
    for key in variables_dict.keys():
        variables.append(key)
    variables = sorted(variables)
    part = "("
    for i in range(len(variables)):
        if variant[i] == '1':
            part += '-'
        part += variables[i]
        part += '|'
    part = part[0:-1]
    part += ")"
    return part


def get_sknf(falses: list[str], variables_dict: dict):
    parts = []
    for fal in falses:
        parts.append(get_part_cnf(fal, variables_dict))
    sknf = ''
    for part in parts:
        sknf += part
        sknf += '&'
    return sknf[0:-1]


def get_all_premiss(table: list[list], variable_dict: dict):
    trues = []
    falses = []
    for row in table:
        if row[1]:
            trues.append(row[0])
        else:
            falses.append(row[0])
    sknf = get_sknf(falses, variable_dict)
    additional_parts = []
    for true in trues:
        additional_parts.append(get_part_cnf(true, variable_dict))
    return [sknf, additional_parts]


def get_theorem(condition: list):
    theorem = ''
    for message in condition[0]:
        theorem += f"({message.infix})&"
    theorem = theorem[0:-1]
    theorem = theorem + '>' + condition[1].infix
    print(f"Докажем методом резолюций теорему {theorem} = 1")
    theorem = f"-({theorem})"
    print(f"Приведем к виду противоречия {theorem} = 0")
    return theorem


def get_disjuncts(table: list[list], variable_dict: dict):
    falses = []
    for row in table:
        if not row[1]:
            falses.append(row[0])
    disjuncts = []
    for false in falses:
        disjuncts.append(get_part_cnf(false, variable_dict))
    return disjuncts


def get_reversed_key(key: str):
    if "-" in key:
        return key[1]
    else:
        return "-" + key


def get_new_disjunct(dis1: str, dis2: str):
    dis = dis1 + dis2
    keys = []
    new_keys = []
    tmp = ''
    for symbol in dis:
        if symbol == "-":
            tmp = "-"
        elif symbol.isalpha():
            keys.append(tmp + symbol)
            tmp = ""
    for key in keys:
        if key not in new_keys and get_reversed_key(key) not in keys:
            new_keys.append(key)
    return new_keys


def get_disjunct_from_keys(keys: list):
    dis = "("
    for key in keys:
        dis += f"{key}|"
    dis = dis[0:-1] + ")"
    return dis


def is_duplicated(dises, dis):
    for a in dises:
        if dis in a:
            return True
    return False


def is_inversion(disjuncts: list, dis1):
    for dis2 in disjuncts:
        if len(get_disjunct_from_keys(get_new_disjunct(dis1[1], dis2[1]))) <= 2:
            return [dis1, dis2
                    ]
    return False


def get_all_inversions(disjuncts: list):
    inversions = []
    for i in range(len(disjuncts) - 1):
        inversion = is_inversion(disjuncts[i::], disjuncts[i])
        if inversion != False:
            inversions.append(inversion)
    return inversions


def resolution_method(disjuncts: list):
    dcount = 0
    disjuncts_old = []
    for dis in disjuncts:
        disjuncts_old.append([f"D{dcount}", dis])
        print(f"D{dcount}", dis)
        dcount += 1

    disjuncts_new = ["starter"]
    while len(disjuncts_new) != 0:
        disjuncts_new = []
        inversions = get_all_inversions(disjuncts_old)
        for inversion in inversions:
            disjuncts_old.remove(inversion[0])
            disjuncts_old.remove(inversion[1])
            print(f"Дизюнкты, {inversion[0]} и {inversion[1]} взаимноуничтожаются")

        if len(disjuncts_old) == 1:
            print("Остался единственный дизъюнкт, теорема ложна:", *disjuncts_old)
            break
        if len(disjuncts_old) == 0:
            print("Теорема верна, т.к свелась к пустой резольенте", disjuncts_old)
            break

        for i in range(len(disjuncts_old) - 1):
            dis1 = disjuncts_old[i]
            for dis2 in disjuncts_old[i + 1::]:
                new_dis = get_disjunct_from_keys(get_new_disjunct(dis1[1], dis2[1]))
                new_dis = [f"D{dcount}", new_dis]
                dcount += 1
                print(new_dis, f"{dis1[0]}|{dis2[0]}")
                disjuncts_new.append(new_dis)

        disjuncts_old = deepcopy(disjuncts_new)
