## Simple Sort
* 題目：Write a function that, given an array of integers arr, sorts its elements in ascending order.
* 意思：輸入一數列，將其中的數字依小至大排序。
* 例子：For arr = [2, 4, 1, 5], the output should be simpleSort(arr) = [1, 2, 4, 5].
* 我的理解與學習筆記：提示說Python可在同一行交換位置。

```Python
def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
    return arr
```
