def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    string = ''.join(a)
    return(string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
    
  #https://github.com/dabeet-lucifer/hackerrank_python
  
