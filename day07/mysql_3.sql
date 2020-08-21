--练习1: 使用book 表完成
--1. 统计每位作家图书的平均价格
select author,avg(price) from book
group by author;

--2. 统计每个出版社出版图书的数量
select publication,count(*) from book
group by publication;

--3. 查看总共有多少个出版社
select count(distinct publication) from book;

--4. 筛选出那些出版过超过50元的图书的出版社,并按照其
--出版图书的平均价格降序排序
select publication,avg(price) from book
group by publication
having max(price) >= 50
order by avg(price) desc;


--5. 统计相同时间出版图书的最高价格和最低价格
select publication_date,max(price),min(price)
from book group by publication_date;

--外键 cascade
alter table person
add foreign key(dept_id)
references dept(id)
on delete cascade on update cascade;

--练习: 根据之前设计的朋友圈表格进行修改
--完成数据表的设计和关系的设计
--用户表
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(64)
);

--朋友圈表
create table pyq(
id int primary key auto_increment,
image char(20),
content text,
time datetime,
user_id int,
foreign key(user_id) references user(id)
);

--点赞评论
create table  user_pyq(
id int primary key auto_increment,
u_id int,
p_id int,
`like` bit,
`comment` text,
foreign key(u_id) references user(id),
foreign key(p_id) references pyq(id)
);











