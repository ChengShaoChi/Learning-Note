## Binary Search Tree功能說明
### 目錄
* [新增](#新增)
* [刪除](#刪除)
* [查詢](#查詢)
* [修改](#修改)

### 新增
* 根據BST的原理，向一個二元搜尋樹b中插入一個節點s的規則為：    
（新插入節點總是葉子節點）
  * 如果b是空樹，就把s所指節點作為根節點新增。    
  * 如果s**等於或小於**b根節點之值，就把s所指節點新增到**左**子樹中。    
  * 如果**大於**，就把s所指節點新增到**右**子樹中。    


參考資料：[二元搜尋樹- 維基百科，自由的百科全書 - Wikipedia](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)

    我有個BST，如下圖一，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BST.png?raw=true"/></div>    
<div align=center>▲圖一</div>
<br />

    現在我想要新增值為8的節點進去，如下圖二，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Insert8.png?raw=true"/></div>    
<div align=center>▲圖二</div>
<br />

    1. 8跟根節點10比，8＜10，往左邊移動。
    2. 8跟節點5比，8＞5，往右邊移動。
    3. 8跟節點7比，8＞7，往右邊移動。
    4. 右邊是空的，8新增進去。
<br />

    現在我想要再新增值為17的節點進去，如下圖三，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Insert17.png?raw=true"/></div>    
<div align=center>▲圖三</div>
<br />

    1. 17跟根節點10比，17＞10，往右邊移動。
    2. 17跟節點15比，17＞15，往右邊移動。
    3. 右邊是空的，17新增進去。

### 刪除
* 必須讓刪除資料完的BST仍然維持BST的原理，以要刪除的節點「有幾個子節點」分成三類且規則為：    
（如果有重複，要全部刪除）
 1. 沒有子節點：直接刪除該節點。    
 2. 有一個子節點：刪除該節點並把它替換成其子節點。
 3. 有兩個子節點：刪除該節點並把它替換成其右子樹裡的最左節點或其左子樹裡的最右節點。    
<br />

    我有個BST，如下圖四，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BST(2).png?raw=true"/></div>    
<div align=center>▲圖四</div>
<br />

    現在我想要刪除8，如下圖五，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Delete8.png?raw=true"/></div>    
<div align=center>▲圖五</div>
<br />

    8沒有子節點，直接刪除。
<br />

    現在我想要刪除7，如下圖六，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Delete7.png?raw=true"/></div>    
<div align=center>▲圖六</div>
<br />

    7有一個子節點，把它替換成其子節點8。
<br />

    現在我想要刪除10，如下圖七，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Delete10.png?raw=true"/></div>    
<div align=center>▲圖七</div>
<br />

    10有兩個子節點，把它替換成其右子樹裡的最左節點12。
    
### 查詢
* 根據BST的原理，在一個二元搜尋樹b中查詢s的規則為：    
（須返回含有target且離root最近（如果有重複）的TreeNode）
  * 如果是空樹，就回傳None。    
  * 如果s**等於**b根節點之值，就回傳b根節點。
  * 如果s**小於**b根節點之值，就查詢**左**子樹。    
  * 如果**大於**，就查詢**右**子樹。
<br />

    我有個BST，如下圖八，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BST(2).png?raw=true"/></div>    
<div align=center>▲圖八</div>
<br />

    現在我想要尋找值為12的節點，如下圖九，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Search.png?raw=true"/></div>    
<div align=center>▲圖九</div>
<br />

    1. 12跟根節點10比，12＞10，往右邊移動。
    2. 12跟節點15比，12＜15，往左邊移動。
    3. 12跟節點12比，12＝12，找到12。

### 修改
* 必須讓修改資料完的BST仍然維持BST的原理，把m改成n的我的想法與步驟為：    
（如果有重複，要全部修改）
  * 刪掉樹裡所有的m。
  * 有幾個m就再新增幾個n到正確的位置。    
<br />

    我有個BST，如下圖十，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/BST(2).png?raw=true"/></div>    
<div align=center>▲圖十</div>
<br />

    現在我想要把12改成4，如下圖十一，
<div align=center><img src="https://github.com/ChengShaoChi/Learning-Note/blob/master/Image/Modify12.png?raw=true"/></div>    
<div align=center>▲圖十一</div>
<br />

    1. 找到12。
    2. 把12刪掉。
    3. 找到4該存在的正確位置並新增。
