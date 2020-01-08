## Hash Table
### 資料夾目錄
* [原理](https://github.com/ChengShaoChi/Learning-Note/blob/master/HW4/Hash%20Table%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Hash%20Table%E8%88%87Hash%20function%E5%8E%9F%E7%90%86.md)
* [程式碼](https://github.com/ChengShaoChi/Learning-Note/blob/master/HW4/hash_table_06170235.py)
### 簡述
* 雜湊表，也叫哈希表，是根據 **鍵（Key）** 直接查詢在內存存儲位置的資料結構。也就是說，它透過 **雜湊函數（Hash Function）** ，將所需查詢的數據映射到表中一個位置來查詢記錄，加快了查找速度。
  * `雜湊函數`：也叫雜湊演算法，是將不固定長度訊息的輸入，演算成固定長度**雜湊值**的輸出。
  * `雜湊值`：不同明文所計算出來的雜湊值必須是不相同的，甚至只改變明文中任何一個字元時，雜湊值的輸出也必須有很大的差異。雜湊值就像是一個無法冒充的識別碼，每一份文件都有其特殊的雜湊值，且無法被偽造，故有「數位指紋（Digital Fingerprint）」之稱。
* 三種功能：
```
1. add：新增。
2. remove：刪除。
3. contains：是否包含。
```
參考資料：    
[雜湊表- 維基百科，自由的百科全書 - Wikipedia ](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)    
[第四章雜湊與亂數演算法 - 翻轉工作室](http://www.tsnien.idv.tw/Security_WebBook/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E9%9B%9C%E6%B9%8A%E8%88%87%E4%BA%82%E6%95%B8%E6%BC%94%E7%AE%97%E6%B3%95.html)
