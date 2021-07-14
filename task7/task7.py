import json

with open('data.txt', 'r+') as f, open('data.json', 'w') as jf:
    firms_lst = [{}, {}]
    firms = [string.split() for string in f]
    for firma in firms:
        firms_lst[0][firma[0]] = int(firma[2]) - int(firma[3])
    firms_lst[1]['average_profit'] = sum(firms_lst[0].values()) // len(firms)
    json.dump(firms_lst, jf)

