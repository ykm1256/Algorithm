-- 코드를 입력하세요
SELECT * FROM FOOD_PRODUCT
where price = (select max(price) from food_product);

# SELECT * FROM FOOD_PRODUCT