def count_substring(string, sub_string):
    a = 0
    for i in range(len(sub_string)):
        if sub_string in string:
            a += 1
            return(a)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
    
    
 #https://github.com/dabeet-lucifer/hackerrank_python
