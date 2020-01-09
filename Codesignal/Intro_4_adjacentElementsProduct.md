## adjacentElementsProduct
* 題目：Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
* 意思：輸入一組整數，找到具有最大乘積的兩個相鄰數字，並傳回其乘積。
* 例子：For inputArray = [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21. 7 and 3 produce the largest product.
* 我的理解與學習筆記：找到具有最大乘積的相鄰元素對並返回該乘積。先創一個list，放每兩個兩個的乘積，再找出其中最大的。
```Python
def adjacentElementsProduct(inputArray):
    list = []
    for i in range(len(inputArray)):
        if i + 1 < (len(inputArray)):
            n = inputArray[i] * inputArray[i + 1]
        list.append(n)
    return max(list)
```
參考資料：
[CodeeFights-Python/adjacentElementsProduct.py at master · RohitBattepati/rohitb · GitHub](https://github.com/RohitBattepati/CodeeFights-Python/blob/master/adjacentElementsProduct.py)
