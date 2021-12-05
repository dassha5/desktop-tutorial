# Бондаренко Дарина


import operator
from dataclasses import dataclass
import json
import codecs
import dateparser

@dataclass
class Market:
    code: int
    name: str
    author: str
    price: int

@dataclass
class MarketData:
    customer: str
    ordercode: int
    productcode: float
    number: float

    def __eq__(self, other):
        return self.code == other.code and self.date == other.date

    def __lt__(self, other):
        return self.code < other.code and dateparser.parse(self.date) < dateparser.parse(other.date)

# Json був зроблений за допомогою Tabula
with codecs.open("tabula-zad5.json", "r", 'utf-8') as f:
    tabula_dict = json.load(f)

market_data_array = []

for json_item in tabula_dict:
    data_list = json_item['data']

    for data in data_list:
        market_data_array.append(MarketData(str(data[0]["text"]),
                                            int(data[1]["text"]),
                                            float(str(data[2]["text"])),
                                            float(str(data[3]["text"])),
                                            float(str(data[4]["text"])),
                                            float(str(data[5]["text"])),
                                            float(str(data[6]["text"])),
                                            float(str(data[7]["text"]))))

markets_array = [Market(1001, "Програмно-апаратна організація комп'ютера IDM РС"), Market(1002, "Посібник з експлуатації ПЕОМ IBM РС"), 
     Market(1003, "Операційна система MS DOS 3.3"), Market(1004, "Асемблер для IBM РС"), Market(1005, "Мова програмування C"), Market(1006, "TURBO PASCAL для професіоналів")]


class AnalysisMarketsPrices:

    def __init__(self, codecustomer, code, author, name, price, number, impost):
        self.codecustomer = codecustomer # Код замовника
        self.code = code # Код товару
        self.name = name # Назва
        self.author = author  # Автор
        self.price = price  # Ціна
        self.number = number  # Кількість 
        self.impost = impost  # Податок на додану вартість 
        self.averagePrice = self.calculateAveragePrice(self.price, self.number, self.impost)  # Сума

    def calculateAveragePrice(self, price, number, impost):
        return round((price * number) + impost)

    def __str__(self) -> str:
        return f"Code {self.codecustomer}, {self.code}, {self.name} {self.author} {self.price} {self.number} {self.impost} {self.averagePrice}"


analysisMarketsPrices = []

for data in market_data_array:
    analysisMarketsPrices.append(AnalysisMarketsPrices(
        code=data.code,
        date=data.date,
        potato=data.price,
        cabbage=data.number,
        onion=data.impost))

sorted_by_code = sorted(analysisMarketsPrices, key=operator.attrgetter("code"))