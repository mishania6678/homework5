with open('data.txt', encoding='utf-8') as f:
    subjs_dict = {}
    for subj_inf in f:
        subj_name = subj_inf[:subj_inf.find(':')]

        for _ in range(subj_inf.count('(')):
            subj_inf = subj_inf.replace(subj_inf[subj_inf.find('('): subj_inf.find(')') + 1], '')

        lessons_amount = sum([int(i) for i in subj_inf.split() if i.isdigit()])
        subjs_dict[subj_name] = lessons_amount

    print(subjs_dict)
    f.close()
