if __name__ == '__main__':
    n = (input()).split()
    c = []
    for x in n:
        c.append(x)
    res = []
    [res.append(x) for x in c if x not in res]
    g = sorted(res)
    print(g[len(g)-2])
