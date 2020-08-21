拆分book表
--
--   存图书信息   存作者信息   存出版社信息
--   表字段内容自己拟定
--   关系自己拟定
--   创建出你所设计的数据表

--作家表
create table 作家(
id int primary key auto_increment,
name varchar(30),
sex char,
remark text
);

create table 出版社(
id int primary key auto_increment,
pname varchar(30),
address varchar(100),
tel char(16)
);

create table 图书(
id int primary key auto_increment,
bname varchar(30),
price float,
a_id int,
p_id int,
foreign key (a_id) references 作家(id),
foreign key (p_id) references 出版社(id)
);

create table author_publication(
id int primary key auto_increment,
aid int,
pid int,
foreign key (aid) references 作家(id),
foreign key (pid) references 出版社(id)
);

练习:
--1. 查询每位老师教授的课程数量
select teacher.tname,count(teacher_id)
from teacher left join course
on teacher.tid = course.teacher_id
group by teacher.tname;

--2. 查询学生的信息及学生所在班级信息
select student.sname,gender,caption
from student left join class
on class.cid = student.class_id;

--3. 查询各科成绩最高和最低的分数,形式 : 课程ID  最高分  最低分
select course_id as 课程ID,
max(number) as 最高分,
min(number) as 最低分
from score
group by course_id;

--4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select stu.sid,sname,avg(number)
from student as stu left join score
on stu.sid = score.student_id
group by stu.sid,stu.sname
having avg(number)>85;


--5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select sid,sname from student
where sid in
(select student_id from score
where course_id=2 and number>80);


select student.sid,sname
from student left join score
on student.sid = score.student_id
where score.course_id=2 and number>80;

--6. 查询各个课程及相应的选修人数
select cname,count(student_id) as 人数
from course left join score
on course.cid = score.course_id
group by cname
order by 人数;


视图操作

--针对多张表创建的视图,往往就是起到简化查询操作的目的
--不会进行写操作
create view student_hobby as
select cls.id,cls.name,cls.score,hobby.hobby
from cls left join hobby
o;n cls.name=hobby.name;

--针对一张表创建的视图,增删改查都可以
create view good_student as
select * from cls where score>85;

--第一个函数
create function max_score() returns float
begin
    return (select score from cls
    order by score desc limit 1);
end

--将Lucy的分数改为最高分+1 获取最高分的人是谁
-- 变量名不要跟字段名重名
create function stu() returns varchar(30)
begin
    declare max_score int;
    declare query_name varchar(30);

    set max_score=(select score from cls
    order by score desc limit 1);

    update cls set score=max_score+1
    where name="Lucy";

    select name from cls
    order by score desc
    limit 1 into query_name;

    return query_name;
end

--带有参数函数
create function queryNameById(uid int(10))
returns varchar(20)
begin
return  (select name from cls
where id=uid);
end $$

练习: 写一个函数,传入两个同学的姓名,
返回这两个同学的分数只差
create function exercise(name1 varchar(30),name2 varchar(30))
returns float
begin
    declare score1 float;
    declare score2 float;
    select score from cls where name=name1 into score1;
    select score from cls where name=name2 into score2;
    return score1-score2;
end $$

--简单的存储过程
create procedure st()
begin
    select name,age from cls;
    select name,score from cls order by score desc;
end

--带有参数的存储过程
create procedure p_in ( in num int )
begin
    select num;
    set num=100;
    select num;
end $$

create procedure p_out ( out num int )
begin
    select num;
    set num=100;
    select num;
end $$

create procedure p_inout ( inout num int )
begin
    select num;
    set num=100;
    select num;
end $$