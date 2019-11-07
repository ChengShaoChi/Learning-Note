## Merge Sort
### 目錄
* [文字說明](#文字說明)
* [流程圖](#流程圖)
* [學習歷程](#學習歷程)
### 文字說明
#### Merge Sort（合併排序法）
* 是排序演算法的一種，使用Divide and Conquer的演算法來實作。
  * Divide and Conquer（分治法）：「分而治之」，就是把一個複雜的問題分成兩個或更多的相同或相似的子問題，直到最後子問題可以簡單的直接求解，原問題的解即子問題的解的合併。
  <br />
  <div align=center><img width="435" height="382.5" src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Merge%20Sort%201.png?raw=true"/></div>    
  <div align=center>▲圖一、Merge Sort步驟</div>
* 分成兩個步驟：    
   1.分割：遞迴地把目前陣列平均分割成兩半。    
   2.合併：在保持元素順序的同時將上一步得到的子陣列整合到一起。    
   <div align=center>▼圖二、Merge Sort步驟</div>    
   <div align=center><img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif"/></div>    
   
   圖片來源：[合併排序- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)
* 我的理解：把陣列不斷分割到只剩一個元素後，兩個兩個進行排序並合併，直到全部合併完成。
   
參考資料：    
[分治法- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E5%88%86%E6%B2%BB%E6%B3%95)    
[合併排序法(Merge Sort) @ 小殘的程式光廊:: 痞客邦::](https://emn178.pixnet.net/blog/post/87965707)

### 流程圖
![image](https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Merge%20Sort.png?raw=true)
### 學習歷程
先嘗試寫出分割的函式，這裡我參考我在Quick Sort的分堆寫法。
```Python
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2
    
    left_list = []
    right_list = []
    
    for i in range(len(arr)):
        if i < m:
            left_list.append(arr[i])
        else:
            right_list.append(arr[i])
    return mergeSort(left_list) + mergeSort(right_list)

arr = [9, 10, 8, 6, 7, 4, 11, 5, 9, 8]
mergeSort(arr)
```
結果顯示：[9, 10, 8, 6, 7, 4, 11, 5, 9, 8]    
修正：「+」會把小list都合成一個list，要把+改成「,」。
```Python
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2
    
    left_list = []
    right_list = []
    
    for i in range(len(arr)):
        if i < m:
            left_list.append(arr[i])
        else:
            right_list.append(arr[i])
    return mergeSort(left_list), mergeSort(right_list)

arr = [9, 10, 8, 6, 7, 4, 11, 5, 9, 8]
mergeSort(arr)
```
結果顯示：((([9], [10]), ([8], ([6], [7]))), (([4], [11]), ([5], ([9], [8]))))    
成功分割了。    

開始試著寫出合併的函式，merge這段參考[合併排序法- 使用Python(Merge sort) @ 史丹利愛碎念:: 痞客邦::](https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python)。
```Python
def merge(left_arr, right_arr):
    if len(left_arr) == 0:
        return right_arr
    elif len(right_arr) == 0:
        return left_arr
    else:
        if left_arr[0] < right_arr[0]:
            return [left_arr[0]] + merge(left_arr[1:], right_arr)
        else:
            return [right_arr[0]] + merge(left_arr, right_arr[1:])

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
        
    m = len(arr)//2
    
    left_arr = []
    right_arr = []
    
    for i in range(len(arr)):
        if i < m:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])
    return merge(mergeSort(left_arr), mergeSort(right_arr))

arr = [9, 10, 8, 6, 7, 11]
mergeSort(arr)
```
結果顯示：[6, 7, 8, 9, 10, 11]    
成功了。    

寫成class。
```Python
class Solution(object):
    def merge(self, left_arr, right_arr):
        if len(left_arr) == 0:
            return right_arr
        elif len(right_arr) == 0:
            return left_arr
        else:
            if left_arr[0] < right_arr[0]:
                return [left_arr[0]] + self.merge(left_arr[1:], right_arr)
            else:
                return [right_arr[0]] + self.merge(left_arr, right_arr[1:])
                
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
            
        m = len(arr)//2
        
        left_arr = []
        right_arr = []
        
        for i in range(len(arr)):
            if i < m:
                left_arr.append(arr[i])
            else:
                right_arr.append(arr[i])
        return self.merge(self.mergeSort(left_arr), self.mergeSort(right_arr))
        
output = Solution().mergeSort([9, 10, 8, 6, 7, 11])
output
```
結果顯示：[6, 7, 8, 9, 10, 11]    
完成。
