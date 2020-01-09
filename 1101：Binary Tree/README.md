## Binary Tree
二元樹，是每個節點最多只有兩個分支的樹結構。通常分支被稱作「左子樹」和「右子樹」。二元樹的分支具有左右次序，不能隨意顛倒。二元樹的第![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20)層至多擁有![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/de838b503259acc792dd682654445984ea6e4c6d)個節點。對任何一棵非空的二元樹，如果其葉片（終端節點）數為![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/63584d203ecb012a7bcb90f422408bbfe4018956)，分支度為2的節點數為![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/840e456e3058bc0be28e5cf653b170cdbfcc3be4)，則![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/aa746d23c7cab9729c356a8e12e734e03de9fa64)。二元樹通常作為資料結構應用，典型用法是對節點定義一個標記函式，將一些值與每個節點相關聯。這樣標記的二元樹就可以實現[二元搜尋樹](https://github.com/ChengShaoChi/Learning-Note/tree/master/HW3)和二元堆積，並應用於高效率的搜尋和排序。

||普通樹|二元樹|
|:---:|:---:|:---:|
|**節點個數**|至少為1|可以為0|
|**最大分支度**|沒有限制|2|
|**左、右次序之分**|無|有|

* 特殊類型：
  * `滿二元樹`：Full Binary Tree，深度為![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3c9a2c7b599b37105512c5d570edc034056dd40)且有![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/f24729d4eae59094b7ed114e09dcbf142f32cde8)個節點的二元樹，稱為「滿二元樹」。
  * `完全二元樹`：Complete Binary Tree，若除了最後一層是滿的或在右邊缺少連續若干節點外，其餘層都是滿的，就稱為「完全二元樹」。
* 遍歷：
  *	`廣度優先遍歷`：[BFS](https://github.com/ChengShaoChi/Learning-Note/tree/master/HW5)
  * `深度優先遍歷`：[DFS](https://github.com/ChengShaoChi/Learning-Note/tree/master/HW5)

參考資料：    
[二元樹 - 维基百科](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%8F%89%E6%A0%91)
