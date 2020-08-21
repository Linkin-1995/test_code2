--编写一个存储过程,传入一个学生姓名
--      通过外部变量获取学生的成绩

create procedure get_score(inout a varchar(30))
begin
set a=(select score from cls where name=a);
end $$

set @name="Lily";
call get_score(@name)