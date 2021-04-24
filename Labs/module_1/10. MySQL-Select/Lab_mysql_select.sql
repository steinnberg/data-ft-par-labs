/*Who Have Published What At Where?*/

SELECT authors.au_id, au_fname, au_lname, titles.title, titles.title_id, publishers.pub_name
from authors
INNER JOIN titleauthor
ON authors.au_id = titleauthor.au_id
INNER JOIN titles
ON titles.title_id = titleauthor.title_id
INNER JOIN publishers
ON publishers.pub_id = titles.pub_id;
 

 /* Who Have Published How Many At Where*/
 
 SELECT authors.au_id, au_fname, au_lname, titles.title, titles.title_id, publishers.pub_name, COUNT(titles.title_id) as title
from authors
INNER JOIN titleauthor
ON authors.au_id = titleauthor.au_id
INNER JOIN titles
ON titles.title_id = titleauthor.title_id
INNER JOIN publishers
ON publishers.pub_id = titles.pub_id
group by authors.au_id;


/*Best Selling Authors*/
 SELECT authors.au_id, au_lname, au_fname, SUM(sales.qty)
FROM authors
INNER JOIN titleauthor
ON titleauthor.au_id = authors.au_id
INNER JOIN sales
ON titleauthor.title_id = sales.title_id
GROUP BY authors.au_id
ORDER BY SUM(sales.qty) DESC
LIMIT 3;


/*Best Selling Authors Ranking*/
 SELECT authors.au_id, au_lname, au_fname, SUM(sales.qty)
FROM authors
INNER JOIN titleauthor
ON titleauthor.au_id = authors.au_id
INNER JOIN sales
ON titleauthor.title_id = sales.title_id
GROUP BY authors.au_id
ORDER BY SUM(sales.qty) DESC;

select a.au_id as AuthorsID,
a.au_fname as FirstName,
a.au_lname as LastName,
sum(COALESCE(s.qty, 0)) as total
from authors a
left join titleauthor ta on a.au_id = ta.au_id
left join sales s on ta.title_id = s.title_id
group by a.au_id
order by total desc;
