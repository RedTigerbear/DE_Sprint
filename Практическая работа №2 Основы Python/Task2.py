#получаем исходную строку
phrase = input("Введите строку для проверки на палиндром: ")

#убираем пробел и определяем длину строки
phrase1 = phrase.replace(" ", "")
phrase_len = len(phrase1)

#перестраиваем буквы в обратном порядке
phrase_back = ""
for iter in range(1, phrase_len+1):
    phrase_back = phrase_back + phrase1[-iter]

#сравниваем получившееся и возвращаем результат сравнения
if phrase1 == phrase_back:
    print(True)
else:
    print(False)