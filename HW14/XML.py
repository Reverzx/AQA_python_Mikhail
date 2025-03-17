import xml.etree.ElementTree as ET


def goods_calculate():
    try:
        tree = ET.parse('file_xml.xml')
        root = tree.getroot()
        sum_goods = 0
        try:
            for product in root.findall('product'):
                name = product.find('name').text
                price = product.find('price').text
                quantity = product.find('quantity').text
                print(f"Товар: {name}; цена за штуку: {price}; кол-во: {quantity}")
                sum_goods += int(price) * int(quantity)
            return f"Общая стоимость товаров на складе: {sum_goods}"
        except ValueError:
            print("Ошибка: некорректные данные в файле")
    except FileNotFoundError:
        return "Ошибка: файл 'file_xml.xml' не найден."


print(goods_calculate())
