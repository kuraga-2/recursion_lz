# функция для поиска НОДа
def nod (a, b):
    if b == 0:
        return a
    else:
        return nod(b, a%b)

# главная функция
def main(): 
    print('Это программа для поиска НОДа двух чисел')
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print("НОД чисел ",a," и ",b," равен",nod(a,b)) 
main()