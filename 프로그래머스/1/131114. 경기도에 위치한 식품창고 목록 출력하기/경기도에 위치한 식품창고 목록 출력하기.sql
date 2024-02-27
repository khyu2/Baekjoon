-- 코드를 입력하세요
SELECT warehouse_id, warehouse_name, address, if (freezer_yn is null, 'N', freezer_yn) as 'FREEZER_YN' from food_warehouse
where tlno like '031%'
order by warehouse_id