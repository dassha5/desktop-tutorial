from prettytable import PrettyTable
from data1 import dt

x = PrettyTable()

x.field_names = ["Код замовника", "Код товару", "Назва", "Автор",
                 "Ціна", "Кількість", "Податок на додану вартість", "Ціна"]
for i in range(0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )


def opentable():
    print('\nЗаявка на постачання товарів')
    print(x)