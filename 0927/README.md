## Stack & Queue  
**Stack**：像是把盤子疊起來，要拿只能拿最上面的，先進後出。  
* 為什麼要有stack？
    * 因為有undo（復原）和回到上一頁的需求。  
* 必須有的功能：  
    * Push：把資料輸進Stack。  
    * Pop：刪除最上面的資料。  
    * Top：回傳最上面的資料。  
    * Getmin：回傳最小的資料。
    * IsEmpty：確認Stack裡是否有資料。  
    * getSize：回傳Stack裡的資料個數。  

**Queue**：像是在排隊，先進先出。  
* 必須有的功能：  
    * Push：把資料從Queue的最後輸進去。  
    * Pop：從前面刪除資料。  
    * Peek：回傳最前面的資料。  
    * Empty：回傳Queue是否為空。  
    * IsEmpty：確認Queue裡是否有資料。  
    * getFront：回傳front所指向的資料。  
    * getBack：回傳back所指向的資料。  
    * getSize：回傳Queue裡的資料個數。
