from typing import List

#ввод строки
#my_string = input("Введите строку: ")
my_string = "{"

#проверим, что там только скобки и стока не пустая
if my_string == "":
    raise Exception("Строка пустая")
for st in my_string:
    if st not in ("[", "]", "(", ")", "{", "}"):
        raise Exception("Во введенной строке не только скобки")

br_list = [0, 0, 0]
br = []

#функция проставления индексов для введенного символа
def test (value) -> List:
    match value:
        case "(":
            return [1, 0, 0]
        case ")":
            return [-1, 0, 0]
        case "[":
            return [0, 1, 0]
        case "]":
            return [0, -1, 0]
        case "{":
            return [0, 0, 1]
        case "}":
            return [0, 0, -1]

#для каждого из символов в строке формируем список значений
#если скобка отрывается: 1, если закрывается: -1
#далее суммируем элементы двух списков
for my_st in my_string:
    br_list = ([a + b for a, b in zip(br_list, test(my_st))])

#если скобки и открывались и закрывались - будет значение 0
#проверяем, что нули - для всех типов скобок
if br_list == [0, 0, 0]:
    print(True)
else:
    print(False)
