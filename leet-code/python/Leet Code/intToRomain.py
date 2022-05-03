class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        table = ["I","V","X","L","C","D","M"]
        answer = ""
        i = 0
    
        while num != 0 :
            temp = ""
            digit = num % 10
        
            if   digit == 4 : 
                temp = table[i] + table[i+1]
            elif digit == 9 : 
                temp = table[i] + table[i+2]
            else :
                if digit > 4 :
                    temp = table[i+1] 
                    digit -= 5
                while digit != 0 : 
                    temp += table[i]  
                    digit -= 1
            
            num //= 10
            i += 2 
            answer = temp + answer
        
        return answer


s = Solution()
print(s.intToRoman(55))