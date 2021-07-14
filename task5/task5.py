with open('data.txt', 'r+') as f:
    try:
        print(input('Введите числа через пробел:'), file=f, end=' ')
        f.seek(0)
        print(sum([sum(map(int, ''.join(i.split()))) for i in f]))
        f.close()
    except ValueError:
        print('Неправильный формат входных данных')
