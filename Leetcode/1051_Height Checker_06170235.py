class Solution:
    def heightChecker(self, heights: List[int]):
        finish = sorted(heights)
        diff = []
        for i, j in zip(heights, finish):
            if i != j:
                diff.append(i)
        return(len(diff))
        
#先把學生排好後應該會長怎樣令為finish
#檢查heights跟finish裡，一對一對應是不一樣的，算次數。
