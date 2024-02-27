-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, date_format(start_date, '%Y-%m-%d') as 'START_DATE'
, date_format(end_date, '%Y-%m-%d') as 'END_DATE',
if ((timestampdiff(day, start_date, end_date) + 1) >= 29, '장기 대여', '단기 대여')
as 'RENT_TYPE'
from car_rental_company_rental_history
where start_date like '2022-09%'
order by history_id desc