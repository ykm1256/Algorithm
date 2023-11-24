-- 코드를 입력하세요
SELECT u.user_id as user_id, u.nickname as nickname, sum(price) as total_sales from used_goods_board as b
inner join used_goods_user as u
on b.writer_id = u.user_id
where b.status = "DONE"
group by u.user_id
having total_sales >= 700000
order by total_sales asc;

# select writer_id, sum(price) as price from used_goods_board
# group by writer_id
# having price >= 700000;