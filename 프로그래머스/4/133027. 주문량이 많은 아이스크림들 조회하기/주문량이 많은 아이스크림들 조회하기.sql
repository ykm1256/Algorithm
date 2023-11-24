-- 코드를 입력하세요
SELECT f.flavor from first_half as f
inner join july as j
on f.shipment_id = j.shipment_id
order by f.total_order + j.total_order desc
limit 3;

-- 코드를 입력하세요
SELECT f.flavor from first_half as f
inner join (select flavor, sum(total_order) as total_order from july group by flavor) as j
on f.flavor = j.flavor
group by flavor
order by sum(f.total_order) + j.total_order desc
limit 3;

# select flavor, sum(total_order) from july
# group by flavor