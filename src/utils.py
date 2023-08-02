from datetime import datetime
import io
import json
from src import keys
import re


def format_number_of_card(number_str):

    """
    Процедура маскирует номер карты или счета
    :param number_str: неформатированная строка с номером счета или карты, номер должен быть последним в строке
    :return: возвращает ту же строку с замаскированным номером
    """

    if len(number_str) < 16:
        return ''

    number_list_all = number_str.split(' ')
    number_card = number_list_all[len(number_list_all) - 1]

    is_bill = len(number_card) > 16
    if is_bill:
        result = f"**{number_card[-4:]}"
    else:
        number_list = re.findall("\d{4}", number_card)

        number_list[1] = f"{number_list[1][:2]}**"
        number_list[2] = "****"

        result = ' '.join(number_list)

    number_list_all[len(number_list_all) - 1] = result
    result = ' '.join(number_list_all)

    return result


def find_operation_by_id(operations_list, operation_id):

    """
    Находит операцию в переданном json по id
    :param operations_list: json с данными об операциях
    :param operation_id: id нужной операции
    """

    for operation in operations_list:
        if operation[keys.KEY_ID] == operation_id:
            return operation


def get_5_last_operations():

    """
    Возвращает 5 последних операций, отсортированных по убыванию даты
    """

    with io.open('operations.json', encoding='utf-8') as file:
        parsed_json = json.load(file)
        result = []
        dates = {}

        for operation in parsed_json:
            if keys.KEY_STATE in operation:
                if operation[keys.KEY_STATE] == keys.STATE_EXECUTED:
                    date_time = datetime.strptime(operation[keys.KEY_DATE], '%Y-%m-%dT%H:%M:%S.%f')
                    dates[date_time] = operation[keys.KEY_ID]

        sorted_dates = dict(sorted(dates.items()))
        sorted_dates = dict(reversed(list(sorted_dates.items())))

        count = 0
        for date, operation_id in sorted_dates.items():
            operation_dict = find_operation_by_id(parsed_json, operation_id)
            operation_dict[keys.KEY_DATE_OBJ] = date
            result.append(operation_dict)
            count += 1
            if count == 5:
                break

        return result
