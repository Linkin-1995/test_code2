--创建class学生表
create table class_1 (
id int primary key auto_increment,
name varchar(30) not null,
age tinyint unsigned,
sex enum('m','w','o'),
score float default 0);

--官方方法创建
CREATE TABLE `class_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  `sex` enum('m','w','o') DEFAULT NULL,
  `score` float DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--创建兴趣爱好表
create table `hobby` (
id int primary key auto_increment,
name varchar(30) not null,
hobby set("sing","dance","draw"),
`level` char,
price decimal(7,2),
remark text
);


--向class_1中插入数据
insert into class_1 values
(1,"Lily",18,'w',87),
(2,"Lucy",18,'w',91);

insert into class_1
(name,age,sex,score)
values
("Joy",19,'m',91),
("Tom",19,'m',89),
("Emma",17,'w',93);


--向hobby中插入数据
insert into hobby values
(1,"Joy","sing,dance",'A',63800.00,"骨骼惊奇,练舞奇才"),
(2,"Lily","sing",'B',20000.00,"天籁之音");

--分数大于90的男生或者小于70的女生
select * from class_1 where
(score>90 and sex='m') or
(score < 70 and sex='w');



