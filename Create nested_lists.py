if name == 'main':
    score_list = [];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])
    second_highest = sorted(set([score for name, score in score_list]))[1]
    print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))


#https://github.com/dabeet-lucifer/hackerrank_python
