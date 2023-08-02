from src import utils
from src import keys


def get_last_operations():

    """
    Основная функция. Возвращает список 5 последних операций в виде строки
    """

    last_5_operations = utils.get_5_last_operations()
    result = ""

    for operation in last_5_operations:
        date_time = operation[keys.KEY_DATE_OBJ]
        date = date_time.strftime("%d.%m.%Y")
        description = operation[keys.KEY_DESCRIPTION]

        operation_from = operation[keys.KEY_FROM] if keys.KEY_FROM in operation else ''
        operation_from_format = utils.format_number_of_card(operation_from)

        operation_to = operation[keys.KEY_TO]
        operation_to_format = utils.format_number_of_card(operation_to)

        operation_from_to = f"{operation_from_format} -> {operation_to_format}" if operation_from_format != '' else operation_to_format

        amount = operation[keys.KEY_OPERATION_AMOUNT]
        amount_sum = amount[keys.KEY_AMOUNT]
        amount_name = amount[keys.KEY_CURRENCY][keys.KEY_NAME]

        result += f"{date} {description}\n{operation_from_to}\n{amount_sum} {amount_name}\n\n"

    return result.strip()


def main():
    message = get_last_operations()
    print(message)


if __name__ == '__main__':
    main()
