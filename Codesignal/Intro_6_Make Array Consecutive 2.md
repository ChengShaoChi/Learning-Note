## Make Array Consecutive 2
* 題目：Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
* 例子：For statues = [6, 2, 3, 8], the output should be makeArrayConsecutive2(statues) = 3. Ratiorg needs statues of sizes 4, 5 and 7.
* 我的理解與學習筆記：最大的數減最小的數加1代表如果沒有缺的話應該會有幾個雕像，再減掉現在共有幾個，就得到缺幾個了。
```Python
def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) + 1 - len(statues)
```
