import matplotlib.pyplot as plt

knteu_knue_knu_1001= [5, 6, 8, 400]
knteu_knue_knu_1002= [5, 6, 8, 400]
knteu_knue_knu_1003= [20, 25, 23, 700]
knteu_knue_knu_1004 = [5, 7, 7, 400]
knteu_knue_knu_1005 = [30, 25, 28, 300]
year = ['Кількість', 'Кількість 1 ','Кількість 2', 'Ціна']

plt.plot(year,knteu_knue_knu_1001,label= "1001")
plt.plot(year,knteu_knue_knu_1002,label = "1002")
plt.plot(year,knteu_knue_knu_1003,label = "1003")
plt.plot(year,knteu_knue_knu_1004,label = "1004")
plt.plot(year,knteu_knue_knu_1005,label = "1005")
plt.xlabel("Код на товар")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

def graph():
    plt.show()