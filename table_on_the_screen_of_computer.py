# Бондаренко Дарина


from prettytable import PrettyTable
from markets_data import market_data_array
from markets_data import markets_array

first_table = PrettyTable()

date_format = "%d.%m.%y"

market_data_field_names = ['Замовник', 'Код замовлення', 'Код товару', 'Кількість']

first_table.field_names = market_data_field_names

for market_data in market_data_array:
    first_table.add_row ([market_data.customer,
                         market_data.order code,
                         market_data.product code,
                         market_data.number])

code_one_table = PrettyTable()

code_one_table.field_names = market_data_field_names

for market_data in market_data_array:
    if market_data.code == 1001:
        code_one_table.add_row([market_data.customer,
                                market_data.order code,
                                market_data.product code,
                                market_data.number])
                                
code_two_table = PrettyTable()

code_two_table.field_names = market_data_field_names

for market_data in market_data_array:
    if market_data.code == 1002:
        code_two_table.add_row([market_data.customer,
                                market_data.order code,
                                market_data.product code,
                                market_data.number])
                                
code_three_table = PrettyTable()

code_three_table.field_names = market_data_field_names

for market_data in market_data_array:
    if market_data.code == 1003:
        code_two_table.add_row([market_data.customer,
                                market_data.order code,
                                market_data.product code,
                                market_data.number])

for market_data in market_data_array:
    if market_data.code == 1004:
        code_two_table.add_row([market_data.customer,
                                market_data.order code,
                                market_data.product code,
                                market_data.number])

for market_data in market_data_array:
    if market_data.code == 1005:
        code_two_table.add_row([market_data.customer,
                                market_data.order code,
                                market_data.product code,
                                market_data.number])

for market_data in market_data_array:
    if market_data.code == 1006:
        code_two_table.add_row([market_data.customer,
                                market_data.order code,
                                market_data.product code,
                                market_data.number])

second_table = PrettyTable()

second_table.field_names = ['Код', 'Назва', 'Автор', 'Ціна']

for market in markets_array:
    second_table.add_row([market.code, market.name])

while True:
    command = str(input(
        "Для виводу Табл.1 натисніть 1. Для виводу Табл.2 натисніть 2. \n"
        "Для виводу код замовника за кодом товару напишіть  Код і номер товару, наприклад Код 1001\n"
        "Щоб завершити роботу натисніть "
        "будь-яку іншу клавішу \n"))

    if command == "1":
        print(first_table)
    elif command == "2":
        print(second_table)
    elif command == "Код 1001":
        print(code_one_table)
    elif command == "Код 1002":
        print(code_two_table)
    elif command == "Код 1003":
        print(code_three_table)
    elif command == "Код 1004":
        print(code_three_table)
    elif command == "Код 1005":
        print(code_three_table)
    elif command == "Код 1006":
        print(code_three_table)
    else:
        print("Кінець роботи")
        break