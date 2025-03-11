import re


def goods_calculate():
    with open("file_xml.xml", "r", encoding="utf-8") as file:
        file_str = file.read()
        price_pattern = r"<price>(\d+)</price>"
        quantity_pattern = r"<quantity>(\d+)</quantity>"
        name_pattern = r"<name>(.*?)</name>"
        price_list = re.findall(price_pattern, file_str)
        quantity_list = re.findall(quantity_pattern, file_str)
        name_list = re.findall(name_pattern, file_str)
        sum_goods = 0
        for n, p, q in zip(name_list, price_list, quantity_list):
            print(f"Товар: {n}; цена за штуку: {p}; кол-во: {q}")
            sum_goods += int(p) * int(q)
        return f"Общая стоимость товаров на складе: {sum_goods}"


print(goods_calculate())
