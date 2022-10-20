# mySQL指令
 

#### 創立database
```php
CREATE DATABASE website
```


#### 創立table

<img width="696" alt="截圖 2022-10-20 下午4 00 12" src="https://user-images.githubusercontent.com/107464637/196896577-57edc864-0039-4c3f-8003-11ea094e3715.png">

```php
create table member(
    -> id bigint(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT"獨立編號",
    -> name varchar(255) NOT NULL COMMENT"姓名", 
    -> username varchar(255) NOT NULL COMMENT"帳戶名稱", 
    -> password varchar(255) NOT NULL COMMENT"帳戶密碼",
    -> follower_count int unsigned NOT NULL default'0' COMMENT"追蹤者數量",
    -> time datetime NOT NULL default CURRENT_TIMESTAMP COMMENT"註冊時間");   
```

#### 要求三

```php
INSERT INTO member(id , name , password , follower_count , time) VALUES (1, 'kevin','test','test',600,default);
```
<img width="570" alt="截圖 2022-10-19 下午5 18 07" src="https://user-images.githubusercontent.com/107464637/196901750-8ddd7852-e047-46ef-95bf-d63e88484f6c.png">


```php
 SELECT * FROM member;
```
 
 <img width="545" alt="截圖 2022-10-19 下午5 18 14" src="https://user-images.githubusercontent.com/107464637/196901504-ef009a0d-509a-4b14-81cb-b248b026c9df.png">

```php
 SELECT * from member ORDER BY time;
 
 SELECT * from member ORDER BY time DESC;
 
 SELECT * from member ORDER BY time DESC LIMIT 1,3;
 
 SELECT * from member WHERE username = 'test';
 
 SELECT * from member WHERE username = 'test' and password = 'test'
  
 UPDATE member SET name = 'test2' WHERE username = 'test';
 
 ```
#### 要求四

```php 
   SELECT count(*) as '總共有幾筆資料' from member;
   SELECT sum(follower_count)as average from member;
   SELECT avg(follower_count)as average from member;
   ```
