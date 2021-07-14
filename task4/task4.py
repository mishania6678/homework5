with open('data.txt', 'r') as rf, open('new_data.txt', 'w', encoding='utf-8') as wf:
    nums_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for string in rf:
        new_string = string.replace('вЂ”', '-').replace(string.split()[0], nums_dict[string.split()[0]])
        print(new_string)
        wf.write(f'{new_string}\n')
    rf.close()
    wf.close()
