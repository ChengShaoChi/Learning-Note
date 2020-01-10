## Web Security: Active Defense
觀看CS50.tv中的[影片](https://www.youtube.com/watch?v=htHq6wCM5Hc)後做的筆記。

* `Active Defense`：主動防禦，指網路安全領域的防禦策略。
* `Web Security`：網路安全。
  * 一般而言需要符合三點安全要素：
    * 保密性：透過加密等方法確保資料的保密性。
    * 完整性：要求使用者取得的資料是完整不可被竄改的。
    * 可用性：保證網站服務的持續可訪問性。
  * 常見影響網路安全的攻擊手法：    
    * SQL Injection：使用惡意的 SQL 語法去影響資料庫內容。
    * XSS（Cross-Site Scripting）：XSS 亦即將惡意程式碼注入到網頁，讓看到網頁的使用者會受影響，概念是透過表單輸入建立一些惡意網址、圖片網址或JavsScript程式碼在HTML中，當使用者觀看頁面時即會觸發。
    * CSRF：跨站請求偽造，又稱為One-Click Attack或Session Riding，是一種挾制使用者在當前已登入的網路應用程式上執行非本意的操作的攻擊方法。
    * DoS：阻斷式攻擊（Denial of Service Attack），又稱為洪水攻擊，是一種網路攻擊手法，其目的在於使目標電腦的網路或系統資源耗盡，使服務暫時中斷或停止，導致真正的使用者無法使用服務。
    * 檔案上傳漏洞：許多網路應用程式讓使用者上傳檔案到伺服器端，由於我們不知道使用者會上傳什麼類型的檔案，若不留意就會造成很大的問題。
    * 加密安全
  
參考資料：    
[Web 資訊安全（Security）簡明入門教學指南](https://blog.techbridge.cc/2016/11/05/web-security-tutorial-introduction/)
