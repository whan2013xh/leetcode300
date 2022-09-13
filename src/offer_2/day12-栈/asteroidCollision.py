# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-17
    FileName   : asteroidCollision.py
    Author     : Honghe
    Descreption: 剑指 Offer II 037. 小行星碰撞
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for num in asteroids:
            if not stack or stack[-1]<0 or (stack[-1]>0 and num>0):
                stack.append(num)
            else:
                append_flag = False
                while stack:
                    if stack[-1]>abs(num):
                        append_flag = True
                        break
                    elif stack[-1]<0:
                        append_flag = True
                        stack.append(num)
                        break
                    elif stack[-1]==abs(num):
                        append_flag = True
                        stack.pop()
                        break
                    elif stack[-1]<abs(num):
                        stack.pop()
                if not append_flag:
                    stack.append(num)
        return stack

if __name__ == '__main__':
    sol = Solution()
    asteroids = [-2,-2,1,-2]
    print(sol.asteroidCollision(asteroids))