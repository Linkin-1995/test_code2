--创建一个数据库 books
create database books charset=utf8;

--数据库中创建一个数据表 book 使用utf8编码
--字段如下: 类型和约束自定
--id 书名 作者 出版社  价格  备注

use books;

create table book(
id int primary key auto_increment,
bname varchar(60) not null,
author varchar(30) not null,
publication varchar(50) comment "出版社",
price float,
`comment` text
);


--在book数据表中插入若干数据 (>8)
--
--作者 : 老舍 鲁迅  冰心 巴金 沈从文 钱钟书 茅盾
--价格 : 30--120
--出版社: 中国文学  人民教育  机械工业
insert into book
(bname,author,publication,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","人民教育出版社",44,"你心中的围城是什么");

insert into book
(bname,author,publication,price)
values
("林家铺子","茅盾","中国文学出版社",51),
("巨人传","忘了","人民教育出版社",47);


--查找训练:
--查找30多元的图书
select * from book
where price >= 30 and price < 40;

--查找人民教育出版社出版的图书
select * from book
where publication="人民教育出版社";

--查找老舍写的,中国文学出版社出版的
select * from book where author="老舍" and
publication="中国文学出版社";

--查找备注不为空的
select * from book
where comment is not null;

--查找70多元的,只看书名和价格
select bname,price from book
where price>=70 and price < 80;

--查找鲁迅写的或者茅盾写的图书
select * from book
where author = "鲁迅" or author="茅盾";

select * from book
where author in ("鲁迅","茅盾");

--修改示例
update class_1 set score=73,sex='w' where name="Eva";

update class_1 set score=score+1 where score > 90;

--alter修改表结构
alter table hobby  add tel char(11) after price;
alter table hobby drop level;
alter table hobby modify tel char(16) not null;
alter table hobby change tel phone char(16);
alter table class_1 rename cls;


--时间日期示例
select * from marathon where  registration_time < now();

--now()函数可以作为默认值
alter table marathon
modify registration_time datetime
default now();

--练习: 使用book表完成
--
--1. 将呐喊价格改为45
update book set price=45 where bname="呐喊";

--2. 修改所有老舍的作品,增加5元
update book set price = price + 5
where author="老舍";

--3. 修改价格字段数据类型为 decimal(5,2)
alter table book modify price decimal(5,2);

--4. 增加一个字段,字段名为出版时间,
--类型为date 在价格后
alter table book add publication_date
date after price;

--5. 将所有老舍的作品出版时间改为 2016-10-1
update book set publication_date="2016-10-01"
where author="老舍";

--6. 修改所有中国文学出版社图书出版时间为
-- 2018-10-1但是不要修改老舍的
update book set publication_date="2018-10-01"
where publication="中国文学出版社" and author!="老舍";

--7. 修改所有出版时间为null的改为2020-1-1
update book set publication_date="2020-01-01"
where publication_date is null;

--8. 删除所有价格超过70元的图书
delete from book where price>70;


--练习: sanguo 表 高级查询语句
--1. 查找所有蜀国人信息,按照攻击力排名
select * from sanguo
where country="蜀"
order by attack desc;

--2. 将赵云攻击力设为360 防御设为70
update sanguo set attack=360,defense=70
where name="赵云";

--3. 将吴国英雄攻击力超过300的改为300,最多改2个
update sanguo set attack=300
where country="吴" and attack>300
limit 2;

--4. 查找攻击力超过200的魏国英雄名字和攻击力,
--   并且显示为姓名  攻击力
select name as 姓名,attack as 攻击力
from sanguo
where country="魏" and  attack>200;

--5. 所有英雄按照攻击力降序排序,如果攻击力相同规则
--   按照防御降序排序
select * from sanguo
order by attack desc,defense desc;

--6. 查找名字为3个字的英雄
select * from sanguo where name like "___";

--7. 查找比魏国攻击力最高的人攻击力还要高的蜀国英雄
select * from sanguo
where country="蜀" and
attack > (select attack from sanguo
where country="魏"
order by attack desc
limit 1);

--8. 找到魏国防御力排名前2的英雄
select * from sanguo
where country="魏"
order by defense desc
limit 2;
--9. 查找所有女性角色同时查找所有男性角色中攻击力少于
--   250的
select * from sanguo where gender="女"
union
select * from sanguo where gender="男"
and attack < 250;










