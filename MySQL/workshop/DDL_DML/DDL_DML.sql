select @@autocommit;
set autocommit=false;
start transaction;

-- 1) 
select count(Code) as "전체"
, count(IndepYear) as "독립 연도 보유"
from country;

-- 2)
select sum(LifeExpectancy) as "합계"
, avg(LifeExpectancy) as "평균"
, max(LifeExpectancy) as "최대"
, min(LifeExpectancy) as "최소"
from country;

-- 3)
select Continent as continent
, count(*) as "국가 수"
, sum(Population) as "인구 합"
from country
group by Continent
order by 2 desc;

-- 4)
select Continent as continent
, sum(SurfaceArea) as "표면적 합"
from country
group by continent
order by 2 desc
limit 3;

-- 5)
select continent
, sum(gnp) as "gnp 합"
from country
where Population > 50000000
group by Continent
order by 2 asc;

-- 6)
select continent
, sum(gnp) as "gnp 합"
from country
where Population > 50000000
group by Continent
having sum(gnp) >= 5000000
order by 2 asc;

-- 7)
select IndepYear as indepyear
, count(IndepYear)
from country
group by Indepyear
having count(IndepYear) >= 10;

select Continent 
, avg(gnp) as cavg
from country
group by Continent;

-- 8)
select Continent as continent
, Name as name
, t.tavg "전세계 평균"
, a.cavg "대륙 평균"
from country c join (
						select Continent as con
                        , avg(gnp) as cavg
                        from country
                        group by Continent
					) a join (
								select avg(GNP) as tavg
                                from country
							) t
on c.Continent = a.con
order by continent asc;

-- 9)
insert into countrylanguage values ('AAA', '외계어', 'F', 10);
-- countrylanguage는 country의 국가 코드를 가져와서 외래키로 사용하고 있기 때문에 
-- country에 추가하려는 코드가 없다면 countrylanguage에 추가할 수 없다.

insert into countrylanguage values ('ABW', '외계어', 'F', 10);

-- delete from countrylanguage
-- where Language = '외계어';

-- 10)
insert into countrylanguage values ('ABW', 'Dutch', 'F', 10);
-- countrylanguage는 CountryCode와 Language가 한 세트가 되어 메인키로 구성되기 때문에
-- 삽입 시 CountryCode와 Language가 모두 같은 경우는 불가능하다.

insert into countrylanguage values ('ABW', '외계어', 'F', 10);

-- delete from countrylanguage
-- where Language = '외계어';

-- 11)
insert into country values (Code='TCode', Region='TRegion', Code2 = 'TC');
-- Not Null에 해당하는 부분이 넣어준 데이터 외에도 존재

-- 12)
update city set population = 1.1 * population where ID = 2331;

select ID
, Name
, Population
from city
where ID = 2331;

-- 13)
delete from country where Code = 'USA';
-- 'USA'가 현재 다른 테이블에 있는 왜래키와 엮여있어서 삭제가 불가능함. 
-- 성공하기 위해서는 엮여있는 다른 데이터를 먼저 삭제한 후 실행하거나 CASCADE를 사용하는 방법도 있음.

-- 14)
rollback;

-- 15)
create schema ssafydb default character set utf8 collate utf8_bin;

-- 16)
drop table if exists user;

-- 17)
-- default null 옵션을 주니 에러 발생하여 뺐음.
create table user(
	id varchar(50) not null
    , name varchar(100) not null default '익명'
    , pass varchar(100) not null
    ,primary key (id)
);

-- 18)
insert into user values ('ssafy', '1234', '김싸피'), ('hong', '5678', '홍싸피'), ('test', 'test', '테스트');

-- 19)
update user set pass = concat(id,'@',pass) where id = 'test';

select * from user;

-- 20)
delete from user where id = 'test';

select * from user;

-- 21)
commit;