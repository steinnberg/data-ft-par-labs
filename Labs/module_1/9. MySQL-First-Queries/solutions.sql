SELECT * FROM foo.new;
select distinct(prime_genre) from new;

select prime_genre, count(*)
from new
where rating_count_tot >0
 group by prime_genre
 order by count(*) desc;
 
select prime_genre, count(*)
from new
 group by prime_genre
 order by count(*) desc;
 
select prime_genre, count(*)
from new
 group by prime_genre
 order by count(*) asc
 limit 10;

select * from new
order by user_rating desc;

select * from new
order by user_rating desc, rating_count_tot desc
limit 3;

select sum(rating_count_tot) , avg(user_rating)
from new
where price > 0

/*Which is the genre with most apps*/