if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)
    print(hash(t));
    
    
    #https://github.com/dabeet-lucifer/hackerrank_python
