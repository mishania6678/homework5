with open('data.txt') as f:
    average = 0
    for string in f:
        average += int(string.split()[1])
        if int(string.split()[1]) < 20000:
            print(string.split()[0])
    f.seek(0)
    print(average / sum(1 for _ in f))
    f.close()
