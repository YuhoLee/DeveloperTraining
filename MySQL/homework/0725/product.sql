-- 1)
DROP DATABASE IF EXISTS pd;

CREATE DATABASE pd;

USE pd;

DROP TABLE IF EXISTS product;

CREATE TABLE product (
  Code char(5) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  Name char(52) CHARACTER SET utf8mb4 NOT NULL,
  Price INT(10) NOT NULL DEFAULT 0,
  Quantity INT(6) NOT NULL DEFAULT 0,
  PRIMARY KEY (Code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 2)
INSERT INTO product VALUES("P0001", "삼성 스마트TV", 4000000, 20), ("P0002", "삼성 노트북", 1500000, 100), ("P0003", "삼성 에어컨", 1000000, 53), ("P0004", "삼성 비스포크 냉장고", 3000000, 14), ("P0005", "삼성 공기청정기", 1100000, 45), ("P0006", "삼성 스마트폰", 900000, 200);

-- 3)
select Code as "상품코드"
, Name as "상품이름"
, Price as "원가"
, round(Price * 0.85) as "15% 할인가"
from product;

-- 4)
update product 
set Price = price * 0.8
where Name like "%TV%";

select *
from product;

-- 5)
select concat(FORMAT(sum(Price * Quantity), 0), "원") as "상품 총금액"
from product