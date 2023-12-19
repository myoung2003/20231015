# 전체 Display
select *
from cust_sales
;



# 고객수 (id,nm으로 중복제거하면 확인가능=distinct)
select count(*),
		count(cust_id),
        count(distinct cust_id),
        sum(sales_qty*goods_price)
from cust_sales
;


# 고객별 방문일수, 최초구매일, 최근구매일,	촤근구매일-최초구매일=거래기간 : datediff(날짜1, 날짜2) , select에 쓴건 group by에도 써줘야함 
select cust_id, cust_nm,
		count(distinct sales_dt) as sales_count,
        min(str_to_date(sales_dt, '%Y%m%d')) as first_sales,
        max(str_to_date(sales_dt, '%Y%m%d')) as last_sales,
        datediff( max(str_to_date(sales_dt, '%Y%m%d')), min(str_to_date(sales_dt, '%Y%m%d')) ) as sales_range
from cust_sales
group by cust_id, cust_nm
order by count(distinct sales_dt) desc;

# 1204

#12월 꺼만 가져오기
select *
from cust_sales
where sales_dt >= '20221201'
  and sales_dt <= '20221231';

# 김씨것만 가져오기
select *
from cust_sales
where cust_nm like '김%';

#특정 나이 가져오기
select *
from cust_sales
where age in (21,23,25);

# 전체 고객수, 총매출랙 가져오기
select count(distinct cust_id),
sum(goods_price*sales_qty)
from cust_sales; 

# 고객별 (구매일수, 최초구매일, 최근구매일, 총구매금액)
select cust_id, cust_nm,
max(sales_dt) as 최근구매일,
min(sales_dt) as 최초구매일,
count(distinct sales_dt) as 구매일수
from cust_sales
group by cust_id,cust_nm
having count(distinct sales_dt) >= 70;
