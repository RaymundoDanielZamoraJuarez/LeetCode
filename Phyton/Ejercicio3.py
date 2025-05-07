class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ogString=list(s)
        subString = []
        highLen=0
        subLen=0
        if len(ogString)!=1:
            for i in range(0,len(ogString)):
                subString.append(ogString[i])
                if subString.count(subString[subLen]) > 1:
                    if subLen>highLen:
                        highLen=subLen
                    dupeIndex=subString.index(subString[subLen])
                    if dupeIndex<1:
                        subString.pop(dupeIndex)
                        subLen-=1
                    else:
                        for j in range(0,dupeIndex+1):
                                subString.pop(0)
                                subLen-=1
                subLen+=1
            if subLen>highLen:
                highLen=subLen
            return highLen
        else:
            return 1
