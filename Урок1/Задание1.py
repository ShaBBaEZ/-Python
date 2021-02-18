a = int(input('Введите целое число:'))
b = int(input('Введите второе целое число:'))
c = input('Введите арифметический знак в формате + - / *:')
d = (a + b)
e = (a - b)
f = (a * b)
g = (a / b)
if c == '+':
    print(d)
elif c == '-':
    print(e)
elif c == '*':
    print(f)
elif c == '/':
    print(g)
else:
    print('Вы ввели нерпавильное значение')
