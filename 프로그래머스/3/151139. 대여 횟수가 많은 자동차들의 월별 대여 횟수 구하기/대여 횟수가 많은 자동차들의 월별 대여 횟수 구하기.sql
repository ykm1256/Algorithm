-- 코드를 입력하세요
# SELECT car_id, count(*) from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
# where start_date <= "2022-08-01" and end_date >= "2022-10-31"
# group by car_id

select month(a.start_date) as month, a.car_id, count(*) as records from CAR_RENTAL_COMPANY_RENTAL_HISTORY as a
inner join (select car_id, count(*) as record from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(start_date) >= 8 and month(start_date) <= 10
        group by car_id
        having count(*) >= 5) as b
on a.car_id = b.car_id
where start_date between "2022-08-01" and "2022-10-31"
group by a.car_id, month
order by month asc, a.car_id desc;

