# 数据库应用系统
## 课程要求
* 实体数量 >= 5
* OS、DBMS、开发语言不限

## 书评资讯
### 模块划分
* 图书信息管理
* 系统用户管理
* 用户数据管理

#### 图书信息管理
* 添加图书
* 修改图书信息

#### 系统用户管理
* 用户注册
* 修改用户信息
* 注销用户

#### 用户数据管理
* 增删书评
* 点赞图书
* 点赞书评

#### 特色功能
* users

  | 名字      | 类型 | 备注        |
  | --------- | ---- | ----------- |
  | user_id   |      | primary key |
  | user_name |      |             |
  | password  |      |             |
  | mail      |      |             |
  | sex       |      | male/female |
  | birthday  |      |             |

* Reviews

  | 名字      | 类型          | 备注        |
  | --------- | ------------- | ----------- |
  | review_id |               | primary key |
  | reviewer  |               | foreign key |
  | book      |               | foreign key |
  | time      |               | 时间戳      |
  | content   | varchar(5000) | 书评内容    |
  | likes     | int           | 点赞数      |
  

```mysql
use book
create table reviews
(
  review_id char(20) not null unique,
  reviewer_id int(11) not null,
  book_id char(20) not null,
  time timestamp not null ,
  content varchar(5000) not null,
  likes int default 0,

  constraint PK_reviews primary key (review_id),
  constraint FK_reviews_user foreign key (reviewer_id) references user(user_id) on delete cascade ,
  constraint FK_reviews_book foreign key (book_id) references books(book_id) on delete cascade
);
```

* Likes

  | 名字     | 类型          | 备注               |
  | -------- | ------------- | ------------------ |
  | likes_id |               | primary key        |
  | liker_id |               | 点赞人 foreign key |
  | item     |               | 被点赞 书或者书评  |
  | time     |               | 时间戳             |
  
```mysql
use book
create table likes
(
  likes_id char(20) not null unique ,
  liker_id int(11) not null ,
  item char(20) not null ,
  time timestamp default current_timestamp,

  constraint PK_likes primary key (likes_id),
  constraint FK_likes_liker foreign key (liker_id) references user(user_id) on delete cascade on update cascade
)
```