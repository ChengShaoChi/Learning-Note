### 流程圖
![image]()
### 學習歷程
先照著圖二打出結構。
```Python
def heapify(arr, n, i):
    #Create a Max Heap
    
def heapSort(arr):
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
```
開始試著製造出Max Heap，heapify這段參考[Python Program for Heap Sort - GeeksforGeeks](https://www.geeksforgeeks.org/python-program-for-heap-sort/)。
```Python
def heapify(arr, n, i):
    n = len(arr)
    M = i
    l = i * 2 + 1
    r = i * 2 + 2
    
    if arr[M] < arr[l]:
        arr[l], arr[M] = arr[M], arr[l]
        
    if arr[M] < arr[r]:
        arr[r], arr[M] = arr[M], arr[r]
        
def heapSort(arr):
    n = len(arr)
    
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        
    print(arr)
    
arr = [9, 10, 8, 6, 7, 11]
heapSort(arr)
```
出現IndexError: list index out of range。    
修正：要確定小孩存在（小孩的index < n）。
```Python
def heapify(arr, n, i):
    n = len(arr)
    M = i
    l = i * 2 + 1
    r = i * 2 + 2
    
    if l < n and arr[M] < arr[l]:
        arr[l], arr[M] = arr[M], arr[l]
        
    if r < n and arr[M] < arr[r]:
        arr[r], arr[M] = arr[M], arr[r]
        
def heapSort(arr):
    n = len(arr)
    
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        
    print(arr)
        
arr = [9, 10, 8, 6, 7, 11]
heapSort(arr)
```
結果顯示：[8, 6, 7, 9, 10, 11]    
修正：不能在heapify函式裡設定n = len(arr)，不然在跑heapSort函式時，n會跟著for迴圈跑。
```Python
def heapify(arr, n, i):
    M = i
    l = i * 2 + 1
    r = i * 2 + 2
    
    if l < n and arr[M] < arr[l]:
        arr[l], arr[M] = arr[M], arr[l]
        
    if r < n and arr[M] < arr[r]:
        arr[r], arr[M] = arr[M], arr[r]
        
def heapSort(arr):
    n = len(arr)
    
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        
    print(arr)
        
arr = [9, 10, 8, 6, 7, 11]
heapSort(arr)
```
結果顯示：[6, 7, 8, 9, 10, 11]    
成功了。    

寫成class。
```Python
class Solution(object):
    def heapify(self, arr, n, i):
        M = i
        l = i * 2 + 1
        r = i * 2 + 2
    
        if l < n and arr[M] < arr[l]:
            arr[l], arr[M] = arr[M], arr[l]
        
        if r < n and arr[M] < arr[r]:
            arr[r], arr[M] = arr[M], arr[r]
            #return self.heapify(arr, n, M)

    def heapSort(self, arr):
        n = len(arr)

        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
            
        print(arr)
        
output = Solution().heapSort([9, 10, 8, 6, 7, 11])
output
```
結果顯示：[6, 7, 8, 9, 10, 11]    
完成。
