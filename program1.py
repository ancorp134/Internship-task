# Write a program to take an input string and print the number of consecutive occurrences of any letter in the string. If the occurrence is 1 then there is no need to print the count. 
# Input: aaabcccad 
# Output: a3bc3ad

s = input()
s+="/"
i = 0
while( i < len(s) - 1) :
    cnt = 1
 
    while s[i] == s[i + 1] :
 
        i += 1
        cnt+=1
             
        if i + 1 == len(s):
            break
        
    if cnt==1 : 
            print(str(s[i]),end="")
    else :
            print(str(s[i]) + str(cnt),end = "")
    
    i += 1

     
    
 


    
