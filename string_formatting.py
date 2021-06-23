def print_formatted(number):
    hi = len(bin(n)[2:])
    for i in range(1 , number+1):
        print(str(i).rjust(hi," "),str(oct(i)[2:]).rjust(hi," "),str(hex(i)[2:].upper()).rjust(hi," "),str(bin(i)[2:]).rjust(hi," "))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
    
    
#https://github.com/dabeet-lucifer/hackerrank_python
