# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-03
    FileName   : numberToWords-1608.py
    Author     : Honghe
    Descreption: 
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        unit = ["Thousand","Million","Billion","Trillion"]
        res = []
        length = len(str(num))
        max_unit = length//3
        num_str = str(num)
        if num==0:
            return "Zero"
        for i in range(max_unit,-1,-1):
            if i==0:
                one_unit = ""
            else:
                one_unit = unit[i-1]
            start = len(num_str)-(i+1)*3 if (i+1)*3<len(num_str) else 0
            end = len(num_str)-(i)*3
            if start!=end:
                tmp_num = int(num_str[start:end])
                self.change(tmp_num,one_unit,res)
        return " ".join(res)

    def change(self,num,unit,res):
        numbers = {0:["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"],
                   1:["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"],
                   2:["Twenty"],
                   3:["Thirty"],
                   4:["Forty"],
                   5:["Fifty"],
                   6:["Sixty"],
                   7:["Seventy"],
                   8:["Eighty"],
                   9:["Ninety"]}
        if num//100!=0:
            hundred_num = numbers[0][num//100-1]
            res.append(hundred_num)
            res.append("Hundred")
        tmp=num
        num = num%100
        flag = True
        if num//10!=0:
            if num//10==1:
                ten_num = numbers[1][num%10]
                res.append(ten_num)
                flag=False
            else:
                ten_num = numbers[num//10][0]
                res.append(ten_num)
        num = num%10
        if num!=0 and flag:
            one_num = numbers[0][num -1]
            res.append(one_num)
        if unit and tmp!=0:
            res.append(unit)


if __name__ == '__main__':
    sol = Solution()
    num = 100000
    print(sol.numberToWords(num))

