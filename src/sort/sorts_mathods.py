# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-01
    FileName   : sorts_mathods.py
    Author     : Honghe
    Descreption: 排序算法
"""


def bubble_sort(arr):
    """
    冒泡排序算法：提前结束优化
    :param arr:
    :return:
    """
    if not arr:
        return []
    n = len(arr)
    for i in range(n - 1):
        flag = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    return arr


def bubble_sort2(arr):
    """
    冒泡排序算法：提前结束优化+冒泡边界优化
    :param arr:
    :return:
    """
    if not arr:
        return []
    n = len(arr)
    flag = True
    last_index = n - 1
    while flag:
        flag = False
        for j in range(last_index):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last_index = j + 1
                flag = True
    return arr


def select_sort(arr):
    """
    选择排序
    :param arr:
    :return:
    """
    if not arr:
        return []
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def select_sort2(arr):
    """
    选择排序:双向选择优化
    :param arr:
    :return:
    """
    if not arr:
        return []
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        max_index = i
        for j in range(i + 1, n - i):
            if arr[j] < arr[min_index]:
                min_index = j
            if arr[j] > arr[max_index]:
                max_index = j
        if min_index == max_index:
            return arr
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
        if max_index == i:
            max_index = min_index
        if max_index != n - i - 1:
            arr[max_index], arr[n - i - 1] = arr[n - i - 1], arr[max_index]
    return arr


def insert_sort(arr):
    if not arr or len(arr) == 1:
        return arr
    n = len(arr)
    for i in range(1, n):
        cur = arr[i]
        j = i - 1
        while arr[j] > cur and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur
    return arr


def insert_sort2(arr):
    """
    折半插入优化，其实优化效果有限
    :param arr:
    :return:
    """
    if not arr or len(arr) == 1:
        return arr
    n = len(arr)
    for i in range(1, n):
        cur = arr[i]
        left = 0
        right = i - 1

        while left <= right:
            mid = (right - left) // 2 + left
            if arr[mid] > cur:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = cur
    return arr


def shell_sort(arr):
    """
    希尔排序
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    length = len(arr)
    gap = length // 2
    while gap > 0:
        # 切分成不同的子序列
        for i in range(gap):
            # 下面就是简单插入排序
            for j in range(i + gap, length, gap):
                cur = arr[j]
                k = j - gap
                while k >= 0 and arr[k] > cur:
                    arr[k + gap] = arr[k]
                    k -= gap
                arr[k + gap] = cur
        gap //= 2
    return arr


def shell_sort_hibbard(arr):
    if len(arr) < 2:
        return arr
    length = len(arr)
    gap = 1
    # 需要先确认hibbar对应的增量初始值
    while gap < (length // 2):
        gap = gap * 2 + 1
    while gap > 0:
        # 切分成不同的子序列
        for i in range(gap):
            # 下面就是简单插入排序
            for j in range(i + gap, length, gap):
                cur = arr[j]
                k = j - gap
                while k >= 0 and arr[k] > cur:
                    arr[k + gap] = arr[k]
                    k -= gap
                arr[k + gap] = cur
        gap //= 2
    return arr


def merge_sort(arr):
    """
    自顶向下：递归，先切分，后合并
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    res = merge_arr(arr, 0, len(arr) - 1)
    return res


def merge_arr(arr, start, end):
    if start == end:
        return [arr[start]]
    mid = (end - start) // 2 + start
    return merge(merge_arr(arr, start, mid), merge_arr(arr, mid + 1, end))


def merge(arr1, arr2):
    res = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    if i < len(arr1):
        res += arr1[i:]
    if j < len(arr2):
        res += arr2[j:]
    return res


def merge_sort2(arr):
    """
    原地自顶向下：递归，先切分，原地合并
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    merge_arr2(arr, 0, len(arr) - 1)
    return arr


def merge_arr2(arr, start, end):
    if start == end:
        return
    mid = (end - start) // 2 + start
    merge_arr2(arr, start, mid)
    merge_arr2(arr, mid+1, end)
    merge2(arr, start, mid, mid + 1, end)


def merge2(arr, start1, end1, start2, end2):
    """
    原地合并：三次旋转，手摇算法
    :param arr:
    :param start1:
    :param end1:
    :param start2:
    :param end2:
    :return:
    """
    i = start1
    j = start2
    while i <j and j <= end2:
        index = j
        while i < j and arr[i] <= arr[j]:
            i += 1
        while j<= end2 and arr[j] <= arr[i]:
            j += 1

        reverse(arr, i, index - 1)
        reverse(arr, index, j-1)
        reverse(arr, i, j-1)


def reverse(arr, start, end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

def merge_sort3(arr):
    """
    自底向上：迭代，设定每次合并的小数组的步长，直到全部合并完
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    gap = 1
    # 这里不能写成gap<=len(arr)//2
    while gap<len(arr):
        for i in range(0,len(arr)-gap,2*gap):
            arr[i:i+2*gap] = merge(arr[i:i+gap],arr[i+gap:i+2*gap])
        gap*=2
    return arr

def merge_sort4(arr):
    """
    原地自底向上：整体逻辑不变，还是套用之前的手摇算法
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    gap = 1
    # 这里不能写成gap<=len(arr)//2
    while gap<len(arr):
        for i in range(0,len(arr)-gap,2*gap):
            end = i+2*gap-1 if i+2*gap-1<len(arr)-1 else len(arr)-1
            merge2(arr,i,i+gap-1,i+gap,end)
        gap *= 2
    return arr


def quick_sample_sort(arr):
    """
    朴素快排，选取左边第一个为轴
    :param arr:
    :return:
    """
    if len(arr)<=1:
        return arr
    quick_sort_part(arr,0,len(arr)-1)
    return arr


def quick_sort_part(arr,left,right):
    if left<right:
        pos = partition(arr,left,right)
        quick_sort_part(arr,left,pos-1)
        quick_sort_part(arr,pos+1,right)


def partition(arr,left,right):
    index = left+1
    low = left+1
    tmp = arr[left]
    while index<=right:
        if arr[index]<tmp:
            arr[low],arr[index] = arr[index],arr[low]
            low+=1
        index+=1
    low-=1
    arr[left],arr[low] = arr[low],arr[left]
    return low

import random

def quick_random_sort(arr):
    if len(arr)<=1:
        return arr
    quick_sort_random(arr,0,len(arr)-1)
    return arr

def quick_sort_random(arr,left,right):
    """
    随机轴，只需要随机一个索引即可
    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left<right:
        random_pos = random.randint(left,right)
        arr[left],arr[random_pos] = arr[random_pos],arr[left]
        pos = partition(arr, left, right)
        quick_sort_part(arr, left, pos - 1)
        quick_sort_part(arr, pos + 1, right)

def quick_middle_sort(arr):
    if len(arr)<=1:
        return arr
    quick_sort_middle(arr,0,len(arr)-1)
    return arr

def quick_sort_middle(arr,left,right):
    """
    三数取中法：选择三个数中，居于中间大小的数作为轴
    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        middle = (right-left)//2+left
        # 把left、right、middle三个位置元素居于中间的交换到left索引位置
        if arr[middle]<arr[left]:
            arr[middle],arr[left] = arr[left],arr[middle]
        if arr[middle]>arr[right]:
            arr[middle],arr[right] = arr[right],arr[middle]
        if arr[middle]>arr[left]:
            arr[middle],arr[left] = arr[left],arr[middle]
        pos = partition(arr, left, right)
        quick_sort_part(arr, left, pos - 1)
        quick_sort_part(arr, pos + 1, right)

def double_quick_sort(arr):
    if len(arr)<=1:
        return arr
    quick_sort_double(arr,0,len(arr)-1)
    return arr

def quick_sort_double(arr,left,right):
    if left < right:
        middle = (right - left) // 2 + left
        # 把left、right、middle三个位置元素居于中间的交换到left索引位置
        if arr[middle] < arr[left]:
            arr[middle], arr[left] = arr[left], arr[middle]
        if arr[middle] > arr[right]:
            arr[middle], arr[right] = arr[right], arr[middle]
        if arr[middle] > arr[left]:
            arr[middle], arr[left] = arr[left], arr[middle]

        index = left + 1
        low = left + 1
        high = right - 1
        tmp_low = arr[left]
        tmp_high = arr[right]
        while index <= high:
            if arr[index] < tmp_low:
                arr[low], arr[index] = arr[index], arr[low]
                low += 1
                index += 1
            elif arr[index] > tmp_high:
                while index<high and arr[high]>tmp_high:
                    high -= 1
                arr[high], arr[index] = arr[index], arr[high]
                high -= 1
            else:
                index += 1

        low -= 1
        arr[left], arr[low] = arr[low], arr[left]
        high += 1
        arr[right], arr[high] = arr[high], arr[right]
        quick_sort_double(arr,left, low-1)
        quick_sort_double(arr, low+1, high-1)
        quick_sort_double(arr, high + 1, right)

def heap_sort(arr):
    """
    堆排序：1、堆化；2、排序
    最大堆
    :param arr:
    :return:
    """
    if len(arr)<2:
        return arr

    length = len(arr)
    # 1、堆化
    for i in range(length//2,-1,-1):
        heapify(arr,i,length)

    # 2、原地排序
    for i in range(length-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i)
    return arr

def heapify(arr, start, end):
    if start>=end:
        return
    parent = start
    tmp = arr[parent]
    child = 2 * parent + 1
    while child<end:
        if child+1<end and arr[child]<arr[child+1]:
            child +=1
        if child<end and arr[child]>tmp:
            arr[parent] = arr[child]
            parent = child
            child = parent*2+1
        else:
            break
    arr[parent] = tmp


def count_sort(arr):
    if len(arr)<2:
        return arr

    max_num = float("-inf")
    min_num = float("inf")
    for i in arr:
        max_num = max(max_num,i)
        min_num = min(min_num,i)

    count_arr = [0]*(max_num-min_num+1)
    for i in arr:
        count_arr[i-min_num]+=1

    index = 0
    for pos,count in enumerate(count_arr):
        for j in range(count):
            arr[index]=pos+min_num
            index+=1
    return arr

def radix_sort(arr):
    """
    朴素基数排序
    :param arr:
    :return:
    """
    if len(arr)<2:
        return arr

    radix_size = 0
    max_arr = float("-inf")
    for i in arr:
        max_arr = max(i,max_arr)
    while max_arr:
        pass


if __name__ == '__main__':
    arr = [4, 6, 2, 1, 7, 9, 5, 8, 3, 3]
    print(count_sort(arr))
