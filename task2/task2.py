with open('data.txt') as f:
    print('Кол-во строк:', sum(1 for _ in f))
    f.seek(0)
    for index, string in enumerate(f):
        print(f'Кол-во слов в {index + 1}-ой строке:', ' '.join(string.split()).count(' ') + 1)
    f.close()
