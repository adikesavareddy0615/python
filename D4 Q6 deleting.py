def delchar(s,c):
    
    if (len(c)==1):
        for i in range(len(s)):
            if (c is not s[i]):
                print( s[i])
            else:
                continue

delchar('apple','p')


def delchar (s,c):
    if len(c) == 1:
        for i in range(len(s)):
            if c not in s[i]:
                print(s[i])
            else:
                continue
string = input("enter the string:") 
char = input("enter the character that is to be removed:")            
delchar(string,char)
