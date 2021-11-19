class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if text1 == "" and text2 == "":
            return 0
    
        self.cache = {}
        
        result = self.memo(len(text1)-1,len(text2)-1,text1,text2)
        
        return result

def memo(self,i,j,t1,t2):
    
    if i < 0 or j < 0:
        return 0
    if (i,j) in self.cache:
        return self.cache[(i,j)]
    
    if i == 0 and j == 0:
        if t1[i] == t2[j]:
            self.cache[(i,j)] = 1
        else:
            self.cache[(i,j)] = 0
        return self.cache[(i,j)]
    if t1[i] == t2[j]:
        result = 1 + self.memo(i-1,j-1,t1,t2)
    else:
        result = max(self.memo(i-1,j,t1,t2),self.memo(i,j-1,t1,t2))
        
    self.cache[(i,j)] = result
    return self.cache[(i,j)]