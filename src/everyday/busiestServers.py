# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-30
    FileName   : busiestServers.py
    Author     : Honghe
    Descreption: 1606. 找到处理最多请求的服务器
"""
from sortedcontainers import SortedList
import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        超时了
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        deals = [0]*k
        last_quest = [0]*k
        for index,cur in enumerate(arrival):
            server_index = index%k
            if last_quest[server_index]<=cur:
                deals[server_index]+=1
                last_quest[server_index]=cur+load[index]
            else:
                for i in range(k-1):
                    next_index = (server_index+i+1)%k
                    if last_quest[next_index]<=cur:
                        deals[next_index] += 1
                        last_quest[next_index] = cur+load[index]
                        break
        max_re = max(deals)
        return [index for index,i in enumerate(deals) if i==max_re]

    def busiestServers2(self, k, arrival, load):
        deals = [0]*k
        last_quest = SortedList(range(k))
        busy = []
        for i,(start,t) in enumerate(zip(arrival,load)):
            while busy and busy[0][0]<=start:
                last_quest.add(busy[0][1])
                heapq.heappop(busy)
            # 如果没有可用的服务器
            if len(last_quest)==0:
                continue

            #
            j = last_quest.bisect_left(i%k)
            if j==len(last_quest):
                j=0
            id = last_quest[j]
            deals[id]+=1
            heapq.heappush(busy, (start+t,id))
            last_quest.remove(id)
        max_re = max(deals)
        return [index for index, i in enumerate(deals) if i == max_re]


if __name__ == '__main__':
    sol = Solution()
    k=1
    arrival = [1]
    load = [1]

    print(sol.busiestServers(k,arrival,load))

