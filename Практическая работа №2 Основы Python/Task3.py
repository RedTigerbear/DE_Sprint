from logging import exception
from tokenize import String
from soupsieve import match

def m_load(value) -> String:
    match value:
        case "2":
            return "MM"
        case "1":
            return "M"

def c_load(value) -> String:
    match value:
        case "9":
            return "CM"
        case "8":
            return "DCCC"
        case "7":
            return "DCC"
        case "6":
            return "DC"
        case "5":
            return "D"
        case "4":
            return "CD"
        case "3":
            return "CCC"
        case "2":
            return "CC"
        case "1":
            return "C"

def x_load(value) -> String:
    match value:
        case "9":
            return "XC"
        case "8":
            return "LXXX"
        case "7":
            return "LXX"
        case "6":
            return "LX"
        case "5":
            return "L"
        case "4":
            return "XL"
        case "3":
            return "XXX"
        case "2":
            return "XX"
        case "1":
            return "X"

def i_load(value) -> String:
    match value:
        case "9":
            return "IX"
        case "8":
            return "XIII"
        case "7":
            return "XII"
        case "6":
            return "XI"
        case "5":
            return "V"
        case "4":
            return "IV"
        case "3":
            return "III"
        case "2":
            return "II"
        case "1":
            return "I"

#ввод числа
xt = input("Введите число от 1 до 2000: ")

#проверка, что это число
if xt.isnumeric():
    x = int(xt)
else:
    raise Exception("Введено не число")

#проверка на вхождение в диапазон 1-2000
if x > 2000:
    raise Exception("Введено число больше 2000")
elif x < 1:
    raise Exception("Введено число меньше 1")

#обработка
xt_len = len(xt)
xr = ""

if xt_len == 4:
    xr = m_load(xt[0]) + c_load(xt[1]) + x_load(xt[2]) + i_load(xt[3])
elif xt_len == 3:
    xr = c_load(xt[0]) + x_load(xt[1]) + i_load(xt[2])
elif xt_len == 2:
    xr = x_load(xt[0]) + i_load(xt[1])
else:
    xr = i_load(xt[0])

print(xr)