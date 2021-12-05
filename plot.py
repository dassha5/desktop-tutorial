# Бондаренко Дарина


import matplotlib.pyplot as plt
from convert_market_data_to_json import dict_of_data_for_plot

title_list = ['Ціна', 'Замовлення',
              'Код замовлення', 'Кількість']

dict_of_values_for_plots = {}

for key, val in dict_of_data_for_plot.items():
    for val_key, val_value in val.items():
        try:
            dict_of_values_for_plots[val_key].append(val_value)
        except:
            dict_of_values_for_plots[val_key] = [val_value]

styles = ['g--', 'm', 'b--']
line_width = ['2', '4', '3']
for final_key, final_val in dict_of_values_for_plots.items():
    if final_key != 'date':

        for id, val in enumerate(dict_of_values_for_plots[final_key]):
            plt.plot(val, styles[id], linewidth=line_width[id], alpha=0.7)

        plt.title(title_list[0])
        title_list.pop(0)
        plt.legend(['Програмно-апаратна організація компютера IDM РС', 'Посібник з експлуатації ПЕОМ IBM РС', 
                    'Операційна система MS DOS 3.3', 'Асемблер для IBM РС', 'Мова програмування C', 'TURBO PASCAL для професіоналів'])
        plt.savefig(final_key, dpi=200)
        plt.clf()