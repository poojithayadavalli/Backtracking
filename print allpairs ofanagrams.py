"""
Given an array of strings, the task is to find all anagram pairs in the given array.

Input:
Input indicates a array of strings seperated by spaces

Output:
Print all pairs of anagrams in array in seperate lines

Example:

Input:
anagram gramana hello lohel
Output:
anagram gramana
hello lohel

Input:
anagram graman hello lohel
Output:
anagram gramana
hello lohel

Input:
Hello world
Output:
None

"""
NO_OF_CHARS = 256
def areAnagram(str1,str2):
    count = [0] * NO_OF_CHARS 
    i = 0
    while i < len(str1) and i < len(str2): 
        count[ord(str1[i])] += 1
        count[ord(str2[i])] -= 1
        i += 1 
    if len(str1) != len(str2): 
        return False
    for i in range(NO_OF_CHARS): 
        if count[i]: 
            return False
        return True 
def findAllAnagrams(arr: list, n: int): 
    for i in range(n): 
        for j in range(i + 1, n): 
            if areAnagram(arr[i], arr[j]): 
                print(arr[i],arr[j])
s=input().split()
findAllAnagrams(s,len(s))
