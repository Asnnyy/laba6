from bidict import bidict
def z1():
    countries = {"Россия": "Москва", "Иордания": "Амман", "Турция": "Анкара", "Казахстан": "Астана", "Таиланд": "Бангкок", "Китай": "Пекин", "Грузия": "Тбилиси"}
    print(countries)
    k = "Иордания"
    capital = countries.get(k)
    print(capital)
    c = sorted(countries.items(), key=lambda item: item[1])
    print(c)
z1()

def z2():
    m = {"АВЕИНОРСТ": 1, "ДКЛМПУ": 2, "БГЁЬЯ": 3, "ЙЫ": 4, "ЖЗХЦЧ": 5, "ШЭЮ": 8, "ФЩЪ": 10}
    count = 0
    res = input("Введите Ваше слово:")
    for slovo in res.upper():
        for key in m:
            if slovo in key:
                count += m[key]
                print("Стоимость слова равняется", "=", count)
z2()

