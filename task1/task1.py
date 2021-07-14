with open('data.txt', 'w') as f:
    while True:
        text = input()
        if text == '': break
        f.write(f'{text}\n')
    f.close()
