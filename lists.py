if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        b = input().split()
        for c in range(1,len(b)):
            b[c] = int(b[c])
        if (b[0] == "insert"):
            a.insert(b[1],b[2])
        elif (b[0] == "remove"):
            a.remove(b[1])
        elif (b[0] == "append"):
            a.append(b[1])
        elif (b[0] == "sort"):
            a.sort()
        elif (b[0] == "pop"):
            a.pop()
        elif (b[0] == "reverse"):
            a.reverse()
        elif (b[0] == "print"):
            print(a)

            
            
#https://github.com/dabeet-lucifer/hackerrank_python
