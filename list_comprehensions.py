if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a = [i for i in range(0,x+1)]
    b = [i for i in range(0,y+1)]
    c = [i for i in range(0,z+1)]
    new = []
    for i in a:
        for j in b:
            for k in c:
                if (sum([i,j,k]) != n):
                    new.append([i,j,k])
print(new)


#https://github.com/dabeet-lucifer/hackerrank_python
