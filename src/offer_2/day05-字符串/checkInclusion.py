# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-23
    FileName   : checkInclusion.py
    Author     : Honghe
    Descreption: 
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        if len2<len1:
            return False
        count = {}
        for word in s1:
            count[word]=count.get(word,0)+1

        i=0
        while i<=len2-len1:
            tmp = {}
            j=i
            while j<i+len1:
                if s2[j] not in count:
                    i=j+1
                    break
                tmp[s2[j]]=tmp.get(s2[j],0)+1
                j+=1
            if j==i+len1:
                if tmp==count:
                    return True
                else:
                    i+=1
        return False

    def checkInclusion2(self, s1, s2):
        """
        滑动窗口法，这个
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        if len2 < len1:
            return False
        count = {}
        for word in s1:
            count[word] = count.get(word, 0) + 1

        need = len1
        for right in range(len2):
            if s2[right] in count:
                if count[s2[right]]>0:
                    need-=1
                count[s2[right]] -=1

            left = right - len1
            if left>=0:
                if s2[left] in count:
                    if count[s2[left]] >= 0:
                        need += 1
                    count[s2[left]] += 1

            if need==0:
                return True
        return False


if __name__ == '__main__':
    sol=Solution()
    s1 = "ab"
    s2 ="eidboaoo"
    print(sol.checkInclusion(s1,s2))

