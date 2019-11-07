##### merge_sort_06170235.py

class Solution(object):
    #函式一merge：排序並合併，有參考
    def merge(self, left_arr, right_arr):
        if len(left_arr) == 0:#如果左邊沒有元素了，就直接回傳右邊的
            return right_arr
        elif len(right_arr) == 0:#右邊也一樣
            return left_arr
        else:
            if left_arr[0] < right_arr[0]:
                return [left_arr[0]] + self.merge(left_arr[1:], right_arr)
            #如果左邊第一個值比右邊第一個值小，就先取出它，並把剩下的元素繼續跟右邊的比
            else:
                return [right_arr[0]] + self.merge(left_arr, right_arr[1:])
            #相反也一樣

    #函式二mergeSort：把陣列不斷平均分割成兩半
    def mergeSort(self, arr):#參考我在Quick Sort的分堆寫法
        if len(arr) <= 1:#分割到每個array裡都只剩一個元素，就直接返回該array
            return arr
        
        m = len(arr) // 2#中間的。array有奇數個元素的話，右邊會比左邊多一個元素
        
        left_arr = []#創一個左邊的array，讓index比m小的放進去
        right_arr = []#創一個右邊的array，讓index跟m一樣和比m大的放進去
        
        for i in range(len(arr)):
            if i < m:
                left_arr.append(arr[i])
            else:
                right_arr.append(arr[i])
        return self.merge(self.mergeSort(left_arr), self.mergeSort(right_arr))#繼續分
