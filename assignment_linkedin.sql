use pixel;
create table skills (
	id int,
    technology varchar(255) not null);


INSERT INTO skills (id,technology) 
Values ('1', 'dsa'),
('1', 'tableau'),
('1', 'sql'),
('2', 'r'),
('2', 'bi');

select id
from skills 
where technology in ('dsa','sql')
group by id 
having count(distinct technology) = 2;

select * from skills where technology in ('dsa','sql');