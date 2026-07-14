class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        
        for i in s:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        dic2 = {}
        for i in t:
            if i in dic2.keys():
                dic2[i] += 1
            else:
                dic2[i] = 1
        if dic.items() == dic2.items():
            return True           
        else:
            return False