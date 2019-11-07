#####heap_sort_06170235.py

class Solution(object):
    #函式一heapify：把陣列製作成Max Heap，遞增排序，有參考
    def heapify(arr, n, i):#n是heap的長度，i是root的index
        M = i#先令最大的是root
        l = i * 2 + 1#左邊小孩的index
        r = i * 2 + 2#右邊小孩的index
        
        if l < n and arr[M] < arr[l]:#如果左邊小孩的index在範圍裡（存在），且root的值小於左邊小孩的值，
            arr[l], arr[M] = arr[M], arr[l]#就交換
            
        if r < n and arr[M] < arr[r]:#右邊也一樣
            arr[r], arr[M] = arr[M], arr[r]
            
    #函式二heapSort：利用Max Heap來進行排序
    def heapSort(arr):
        n = len(arr)
        
        #如果heap的大小是n，代表有n個數字，從下面數來第一個有小孩的（index = n//2-1）開始跟它的小孩比
        for i in range(n//2-1, -1, -1):#n//2-1、n//2-2、n//2-3、...、0
            heapify(arr, n, i)

        #製造完Max Heap，開始排序
        for i in range(n-1, 0, -1):#n-1、n-2、n-3、...、1
            arr[0], arr[i] = arr[i], arr[0]#array的第一個值跟最後一個值交換
            heapify(arr, i, 0)
            #一換完位置，最大值跑到array的最後一位，就不用管它了。其他的要再跑heapify一次，index = 0跟它的小孩比
            #比完再換位置，循環
        
        print(arr)
