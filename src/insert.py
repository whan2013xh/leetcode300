# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-07-19
    FileName   : insert.py
    Author     : Honghe
    Descreption: 57、插入区间
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        排序法：将新区间插入到前面的区间列表里，就变化成56的题目，然后使用排序法解答就行
        其实还有个优化点，不是直接排序
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res = []
        for interval in intervals:
            if len(res)==0 or interval[0]>res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

    def insert2(self, intervals, newInterval):
        """
        :param intervals:
        :param newInterval:
        :return:
        """
        res = []
        for i, interval in enumerate(intervals):
            if len(res)==0 or res[-1][1]<newInterval[0]:
                res.append(interval)
            elif res[-1][0]>newInterval[1]:
                res.append(i-1, newInterval)
                res += intervals[i:]
                return res
            elif res[-1][0]<=newInterval[0]:
                if interval[0]>newInterval[1]:
                    res[-1][1] = max(res[-1][1], newInterval[1])
                    res += intervals[i:]
                    return res
                elif interval[1]<newInterval[1]:
                    res[-1][1] = interval[1]
                else:
                    res[-1][1] = interval[1]
                    if i<len(intervals)-1:
                        res += intervals[i+1:]
                    return res
        return res

    def insert3(self, intervals, newInterval):
        """
        排序法优化版：给的区间已经是排好序的，所以可以直接遍历。把场景考虑全就行。
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i, interval in enumerate(intervals):
            if interval[1]<newInterval[0]:
                res.append(interval)
            elif interval[0]>newInterval[1]:
                res.append(newInterval)
                res+=intervals[i:]
                return res
            else:
                tmp = interval+newInterval
                newInterval =[min(tmp), max(tmp)]
        res.append(newInterval)
        return res


if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    sol = Solution()
    res = sol.insert3(intervals, newInterval)
    print(res)
