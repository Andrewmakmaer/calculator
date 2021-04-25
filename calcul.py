number_list = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
dict_operators = {'+': 1, '-': 1, '*': 2, '/': 2}


# replacing "(-...)" with "(0-...)"
# or "(+...)" with "(...)"
def piece_replacement(replace_in_str, operator, start):
    prom = start + 3
    while not replace_in_str[prom] in dict_operators and replace_in_str[prom] != ')':
        prom += 1
    if operator == '+':
        return (replace_in_str.replace(replace_in_str[start + 1: prom],
                                       "{}".format(replace_in_str[start + 2: prom])))
    else:
        return (replace_in_str.replace(replace_in_str[start + 1: prom],
                                       "0-{}".format(replace_in_str[start + 2: prom])))


# case check (-...) and (+...)
def negativ_transformer(n_string):
    for item in range(len(n_string)):
        if n_string[item] == '(' and n_string[item + 1] == '-' and n_string != ")":
            n_string = piece_replacement(n_string, '-', item)
        elif n_string[item] == '(' and n_string[item + 1] == '+' and n_string != ")":
            n_string = piece_replacement(n_string, '+', item)
    return n_string


def string_validator(v_string):
    quantity_open_brackets = 0
    quantity_close_brackets = 0
    number = ""
    for item in v_string:
        if item in number_list or item == ".":
            number = item
        elif item in dict_operators:
            if number:
                number = ""
            else:
                raise ValueError
        elif item == "(":
            quantity_open_brackets += 1
        elif item == ")":
            quantity_close_brackets += 1
        else:
            raise ValueError
    if quantity_open_brackets != quantity_close_brackets:
        raise ValueError


def operator_of_operations(transforming_list, operator):
    if operator == "+":
        transforming_list[-1] = transforming_list[-2] + transforming_list.pop()
    elif operator == "-":
        transforming_list[-1] = transforming_list[-2] - transforming_list.pop()
    elif operator == "*":
        transforming_list[-1] = transforming_list[-2] * transforming_list.pop()
    elif operator == "/":
        if transforming_list[-1] == 0:
            raise ZeroDivisionError
        else:
            transforming_list[-1] = transforming_list[-2] / transforming_list.pop()
    return transforming_list


def main(calc_string):
    calc_string = calc_string.replace(" ", "")
    calc_string = negativ_transformer(calc_string)
    try:
        string_validator(calc_string)
    except ValueError:
        return "Input Error"

    list_num = []
    list_operation = []
    number = ""

    # the next item belongs to a number not yet an operator
    for item in calc_string:
        if item in number_list or (item == '.' and number):
            number += item
        elif item == '.':
            number += item

        elif item in dict_operators:
            if number:
                list_num.append(float(number))  # add number stack
                number = ""
            while True:
                '''If there is a lower-order character or a parenthesis before
                   a higher-order character, then we simply add to the stack'''
                if not list_operation or list_operation[-1] == '(' \
                        or dict_operators[item] > dict_operators[list_operation[-1]]:
                    list_operation.append(item)
                    break

                elif dict_operators[item] <= dict_operators[list_operation[-1]]:
                    # else if item is higher-order before lower-order
                    try:  # we perform the operation under item
                        list_num = operator_of_operations(list_num, list_operation.pop())
                    except ZeroDivisionError:
                        return "Error, division by zero was formed during execution"

        elif item == '(':
            list_operation.append(item)

        elif item == ')':
            if number:
                list_num.append(float(number))
                number = ""
            while list_operation[-1] != '(':  # perform all operations up to "("
                try:
                    list_num = operator_of_operations(list_num, list_operation.pop())
                except ZeroDivisionError:
                    return "Error, division by zero was formed during execution"

            list_operation.pop()

    if number:
        list_num.append(float(number))

    while list_operation:
        try:
            list_num = operator_of_operations(list_num, list_operation.pop())
        except ZeroDivisionError:
            return "Error, division by zero was formed during execution"

    result = list_num[0]
    return result


if __name__ == "__main__":
    calculation_string = str(input())
    print(main(calculation_string))
