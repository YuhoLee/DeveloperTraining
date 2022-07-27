-- 3)
select * 
from country
where Code = 'KOR';

-- 4)
select Code as code
, Name as name
, GNP as gnp
, GNPOld as gnpold
, abs(GNP - GNPOld) as gnp변동량
from country
where GNPOld > 0
order by gnp변동량 asc;

-- 5)
select distinct Continent as continent 
from country
order by length(continent) asc;

-- 6)
select concat(Name, "은", Continent, "에 속하며 인구는 ", Population, "명이다.") as 정보
from country
order by Name asc;

-- 7)
select Name as name
, Continent as continent
, GNP as gnp
, Population as population
from country
where IndepYear is null and population > 10000 
order by population asc;

-- 8)
select Code as code
, Name as name
, Population
from country
where Population between 100000000 and 200000000
order by Population desc
limit 3;

-- 9)
select Code as code
, Name as name
, IndepYear as indepyear
from country
where indepyear in(800, 1810, 1811, 1901)
order by indepyear asc ,code desc;

-- 10)
select Code as code
, Name as name
, Region as region
from country
where region like "%Asia%" and name like "_o%";

-- 11)
select concat(char_length("홍길동")) as 한글
, concat(char_length("hong")) as 영문;

-- 12)
select Code as code
, Name as name
, GovernmentForm as governmentform
from country
where governmentform like "%republic%" and char_length(name) >= 10
order by char_length(name) desc;

-- 13)
select Code as code
, Name as name
from country
where left(code,1) in('a','e','i','o','u')
order by name asc
limit 2,3;

-- 14)
select Name as name
, concat(left(name,2), repeat("*",char_length(name)-4), right(name,2)) as guess
from country;

-- 15)
select distinct replace(Region," ", "_") as 지역들
from country
order by char_length(Region) desc;

-- 16)
select Name as name
, SurfaceArea as surfacearea
, Population as population
, round(surfacearea/population,3) as "1인당 점유면적"
from country
where population >= 100000000
order by round(surfacearea/population,3) asc;

-- 17)
select curdate() as "오늘"
, dayofyear(curdate()) as "올해 지난 날"
, from_days(to_days(curdate())+100) as "100일 후";

-- 18)
select Name as name
, Continent as continent
, LifeExpectancy
, 	   case when LifeExpectancy > 80 then '장수국가'
            when LifeExpectancy > 60 then '일반국가'
            else '단명국가'
		end "구분"
from country
where Continent = 'asia' and LifeExpectancy is not null
order by LifeExpectancy asc;

-- 19)
select Name as name
, GNP as gnp
, GNPOld as gnpold
,           case when GNPOld is null then '신규'
            else abs(GNP-GNPOld)
		end "gnp 향상"
from country
order by name asc;

-- 20)
select weekday('2020-05-05')
, case when weekday('2020-05-05') = 5 or weekday('2020-05-05') = 6 then '불행'
  else '행복'
   end "행복여부"