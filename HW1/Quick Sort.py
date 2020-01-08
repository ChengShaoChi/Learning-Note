a = [9, 4, 13, 2, 8, 11, 8]

def QuickSort(list):
    if len(list)<=1:
        return list#如果list只有一個元素或沒有元素了，就直接返回該list
    
    pivot = list[-1]#令基準點的值等於list最後一位的值
    
    left_list = []#創一個左邊的list，讓比pivot小的放進去
    middle_list = []#創一個中間的list，讓跟pivot相等的放進去
    right_list = []#創一個右邊的list，讓比pivot大的放進去
    
    for i in list:
        if i < pivot:
            left_list.append(i)
        elif i == pivot:
            middle_list.append(i)
        else:
            right_list.append(i)
    return QuickSort(left_list) + middle_list + QuickSort(right_list)#左邊跟右邊的list還要繼續分

print(QuickSort(a))

