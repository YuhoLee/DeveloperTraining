use world;

select * from countrylanguage;

select * from city;

select * from country;

-- 1)
select Code as code
, Name as name
from country
where Code = (
				select CountryCode
                from city
                where name = "kabul"
                );

-- 2)
select c.Name as name
, l.Language as language
, l.Percentage as percentage
from country c join countrylanguage l
on c.Code = l.CountryCode
where l.percentage = 100.0 and l.IsOfficial = "T"
order by c.Name asc;

-- 3)
-- select distinct ci.Name as name
-- ,  l.language as language
-- , co.name as name
-- from city ci join countrylanguage l join country co
-- on IsOfficial = "T" and ci.CountryCode = co.Code and ci.name = "Amsterdam"
-- where language = (
-- 					select distinct language
-- 					from countrylanguage, city
-- 					where IsOfficial = "T" and city.CountryCode = (
-- 																	select CountryCode
-- 																	from city
-- 																	where Name = "Amsterdam")
-- 										   and countrylanguage.CountryCode = (
-- 																	select CountryCode
-- 																	from city
-- 																	where Name = "Amsterdam"));

select c.Name as 'name'
, cl.Language as 'language'
, ct.Name as 'name'
from city c inner join countrylanguage cl
on c.CountryCode = cl.CountryCode
inner join country ct
on c.CountryCode = ct.Code
where c.Name = 'Amsterdam' and cl.IsOfficial = 'T';
 
 -- 4)
 select co.Name as name
 , co.Capital as capital
 , ci.Name as "수도"
 , ci.Population as "수도인구"
 from city ci join country co
 on co.name like "%United%" and co.Capital is not null and co.Capital = ci.ID
 where ci.ID in (
					select Capital
					from Country
					where name like "%United%");
                        
-- 5)
select distinct co.Name as name
 , co.Capital as capital
 , case when co.Capital is null then '수도없음'
        else ci.Name
		end "수도"
 , case when co.Capital is null then '수도없음'
        else ci.Population
		end "수도인구"
 from city ci join country co
 on co.name like "%United%" and (co.Capital = ci.ID or co.Capital is null)
 where ci.ID in (
					select Capital
					from Country
					where name like "%United%")
order by name asc;
                        
-- 6)
select count(*)
from country c join countrylanguage l
on c.Code = l.CountryCode and l.IsOfficial = 'T'
where l.Percentage > (
						select max(Percentage)
                        from countrylanguage
                        where CountryCode = 'CHE'
					);
                    
-- 7)
select language 
from country join countrylanguage
on country.code = countrylanguage.CountryCode 
and country.name = "south korea" 
and countrylanguage.IsOfficial = 'T';

-- 8)
select country.name
, country.Code
, count(city.CountryCode)
from country inner join city
on country.Code = city.CountryCode
where country.Name like "Bo%"
group by city.CountryCode;

-- 9)
select 
c.Name, c.Code, if(count(*)=1, '단독', count(*)) 도시개수
from country c left join city t
on c.code = t.CountryCode
where c.name like 'Bo%'
group by c.name;
                    
-- 10)
select CountryCode countrycode
, Name name
, max(Population) as popul
from city
where Population = (
					select max(Population)
                    from city
					);

-- 11)
select co.Name as name
, ci.CountryCode as code
, ci.Name as name
, ci.Population as popultaion
from country co join city ci
on co.Code = ci.CountryCode
where ci.population = (
					select min(Population)
                    from city
					);
                    
-- 12)
select CountryCode countrycode
, Name name
, Population population
from city
where population > (
					select population
					from city
                    where CountryCode = 'KOR' and Name = 'seoul'
                    );
                    
-- 13)
select l.CountryCode countrycode
, l.Language language
from countrylanguage l join city c
on l.CountryCode = c.CountryCode
where c.Name = 'San Miguel' and l.IsOfficial = 'T'
order by countrycode asc;

-- 14)
select Code countrycode
, max(ci.Population) max_pop
from country co join city ci
on co.Code = ci.CountryCode
group by ci.CountryCode
order by ci.CountryCode asc;

-- 15)
select Code countrycode
, ci.Name as name
, max(ci.Population) max_pop
from country co join city ci
on co.Code = ci.CountryCode
where ci.Population in (
						select max(population)
                        from city
                        group by CountryCode
                        )
group by ci.CountryCode
order by ci.CountryCode asc;

select *
from city c join city i
where c.CountryCode = i.CountryCode and c.Population = i.Population and c.Name != i.Name;

select * from city;


-- 16)
select Code countrycode
, co.Name as name
, ci.Name as name
, max(ci.Population) as max_pop
from country co join city ci
on co.Code = ci.CountryCode
where ci.Population in (
						select max(population)
                        from city
                        group by CountryCode
                        ) or co.Population = 0
group by ci.CountryCode
order by ci.CountryCode asc;

-- 17)
create view summary as
select Code countrycode
, co.Name as country
, ci.Name as city
, max(ci.Population) as max_pop
from country co join city ci
on co.Code = ci.CountryCode
where ci.Population in (
						select max(population)
                        from city
                        group by CountryCode
                        ) or co.Population = 0
group by ci.CountryCode
order by ci.CountryCode asc;

-- 18)
select countrycode as code
, country as name
, city as name
, max_pop as population
from summary
where countrycode = 'KOR';