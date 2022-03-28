# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-23
    FileName   : findKthNumber.py
    Author     : Honghe
    Descreption: 440. 字典序的第K小数字
"""

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1
        k-=1
        while k:
            step = self.steps(n,cur)
            # 如果子树节点数量小于K，那么层次遍历像右遍历兄弟节点
            if step<=k:
                cur+=1
                k-=step
            else:
                # 否则说明K在这个子树里，那么向下遍历子节点
                cur*=10
                k-=1
        return cur

    def steps(self, n, root):
        """
        求以root为根节点的子树所有节点个数
        :param n:
        :param root:
        :return:
        """
        steps=0
        start = root
        end = root
        while start<=n:
            steps+=min(n,end)-start+1
            end = end*10+9
            start = start*10
        return steps




if __name__ == '__main__':
    sol = Solution()
    n=2
    k = 2
    print(sol.findKthNumber(n,k))