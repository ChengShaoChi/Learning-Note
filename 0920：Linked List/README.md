## Linked List
**Linked List（連結串列）**  
* 使用 **node（節點）** 來記錄、表示、儲存資料（data），並利用每個node中的 **pointer** 指向下一個node，藉此將多個node串連起來，形成Linked list，並以 **NULL** 來代表Linked list的終點。若實際打開每個node的內部，至少會包含data與pointer。  
![image](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/LinkedList/Intro/f1.png?raw=true)    

![image](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/BasicDataStructures/LinkedList/Intro/f2.png?raw=true)

**Linked List 跟 Array的比較：**  
* Linked List  
    * 優點：插入和刪除資料容易、快速。  
    * 缺點：因為Linked list沒有index，若要找到特定node，需要從頭開始往後查詢。  
* Array（結構陣列）  
    * 優點：查詢資料容易、快速。  
    * 缺點：插入和刪除資料麻煩，因為會造成資料移動頻繁。    
![image](https://miro.medium.com/max/2548/1*nDwDbeHwOz_Kl4zRIMbe_A.png)    

參考資料：    
[Linked List: Intro(簡介)](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)    
[用python實作linked-list - Tobby Kuo - Medium](https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d)
