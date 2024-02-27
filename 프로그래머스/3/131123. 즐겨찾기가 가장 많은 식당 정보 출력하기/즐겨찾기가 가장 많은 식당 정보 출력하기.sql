select food_type, rest_id, rest_name, favorites from rest_info
where favorites = (select max(favorites) from rest_info as r
                  where r.food_type = rest_info.food_type)
order by food_type desc