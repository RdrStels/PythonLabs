# Дана строка символов.
#  Сформировать новую строку, состоящую из символов с номерами три, шесть, девять и т.д. данной строки.
s = str(input("Введите символы: "))
if len(s) < 3:
    print("short")
else:
    for x in range(2, len(s), 3):
        print(s[x], end='')