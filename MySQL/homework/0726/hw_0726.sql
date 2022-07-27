select * from dept;

select * from emp;

-- 1)
select e.ename as "이름"
, e.job as "업무"
, e.sal as "급여"
from dept d join emp e
on d.deptno = e.deptno
where d.loc = "CHICAGO";

-- 2)
select e.empno as "사원번호"
,e.ename as "이름"
, e.job as "업무"
, e.deptno as "부서번호"
from dept d join emp e
on d.deptno = e.deptno
where e.empno not in(
					select distinct mgr
                    from emp
                    where mgr is not null
                    );

-- 3)
-- BLAKE와 같은 상사를 가진 사람들이라 BLAKE는 미포함시켰음.
select ename as "이름"
, job as "업무"
, mgr as "상사번호"
from emp
where mgr = (
			 select mgr
             from emp
             where ename = "BLAKE")
			and ename != "BLAKE";
            
-- 4)
select *
from emp
order by hiredate asc
limit 5;

-- 5)
select e.ename as "이름"
, e.job as "업무"
, d.dname as "부서명"
from dept d join emp e
on d.deptno = e.deptno
where mgr = (
				select empno
                from emp
                where ename = "JONES"
			);