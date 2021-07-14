# -*- coding: utf-8 -*-
# Created by mayn on 2021/7/12
# Copyright (c) 2021 mayn. All rights reserved.
# 49、字母异位词分组

class Solution(object):
    def groupAnagrams(self, strs):
        """
        使用排序后的单词作为key来保存这整个数组
        :type strs: List[str]  ["eat", "tea", "tan", "ate", "nat", "bat"]
        :rtype: List[List[str]]  [
              ["ate","eat","tea"],
              ["nat","tan"],
              ["bat"]
            ]
        """
        result = {}
        for word in strs:
            sort_word = "".join(sorted(word))
            tmp = result.get(sort_word, [])
            tmp.append(word)
            result[sort_word] = tmp
        return list(result.values())

    def groupAnagrams2(self, strs):
        """
        哈希表法
        :type strs: List[str]  ["eat", "tea", "tan", "ate", "nat", "bat"]
        :rtype: List[List[str]]  [
              ["ate","eat","tea"],
              ["nat","tan"],
              ["bat"]
            ]
        """
        result = {}
        for word in strs:
            chars = [0]*26
            for char in word:
                chars[ord(char)-ord('a')] += 1
            key = tuple(chars)
            tmp = result.get(key, [])
            tmp.append(word)
            result[key] = tmp
        return list(result.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    output = sol.groupAnagrams2(strs)
    print(output)
