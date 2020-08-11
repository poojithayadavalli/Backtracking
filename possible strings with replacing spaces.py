"""
Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.

Input:
Input indicates the string

Output:
Print all possible strings by inserting spaces in between letters

Input:
ABC

Output:
ABC
AB C
A BC
A B C

Input:
ABCD

Output:
ABCD
ABC D
AB CD
AB C D
A BCD
A BC D
A B CD
A B C D

Input:
BGH
Output:
BGH
BG H
B GH
B G H

Input:
D
Output:
D

Input:
HJKI
Output:
HJKI
HJK I
HJ KI
HJ K I
H JKI
H JK I
H J KI
H J K I
"""
def toString(List): 
    s = "" 
    for x in List: 
        if x == '': 
            break
        s += x 
    return s 

def printPatternUtil(string, buff, i, j, n): 
    if i == n: 
        buff[j] = ''
        print(toString(buff))
        return
    buff[j] = string[i] 
    printPatternUtil(string, buff, i+1, j+1, n)
    buff[j] = ' '
    buff[j+1] = string[i] 
  
    printPatternUtil(string, buff, i+1, j+2, n)
def printPattern(string): 
    n = len(string)
    buff = [""]*(2*n) 
    buff[0] = string[0]
    printPatternUtil(string, buff, 1, 1, n)
s=input()
printPattern(s)
