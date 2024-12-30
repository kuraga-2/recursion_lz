# функция для поиска НОДа
def pscl(a):
    if a == 1:  #если аргумент 1, то возвращаем 1
        return [[1]]
    triangle = pscl(a - 1)
    last_numb = triangle[-1] 
    new_numb = [1] + [last_numb[i - 1] + last_numb[i] for i in range(1, len(last_numb))] + [1] #перебираем пары и добавляем по краям 1
    return triangle + [new_numb]  #возвращаем новый треугольник

# главная функция
def main():
    numb = int(input('Введите число уровней: ')) 
    print('Треугольник паскаля с ',numb,' уровнями\n', pscl(numb))    
main()