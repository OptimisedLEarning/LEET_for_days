class Solution:
    def maximum69Number (self, num: int) -> int:
        string =  str(num)
        i=-1
        for j in range (len( string)):
            if string[j]=="6":
                i = j
                break
        if i == -1:
            return num 
        else: 
            return int (string[:i]+ "9"+ string[i+1:])
        