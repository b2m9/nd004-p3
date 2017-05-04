"""
1.) What are the most popular 3 articles of all time?

create materialized view visits_per_article as
    select articles.title as title,
        articles.author as author_id,
        count(*) as visits
            from log, articles
            where path = ('/article/' || articles.slug)
            group by title, author;

select title, visits
    from visits_per_article
    order by visits desc
    limit 3;



2.) Who are the most popular authors of all time?

select authors.name, sum(visits_per_article.visits) as total
    from authors, visits_per_article
        where authors.id = visits_per_article.author_id
        group by authors.name
        order by total desc;



3.) On which days did more than 1% of requests lead to errors?

create materialized view status_per_day as
    select to_char(time, 'YYYY-MM-DD') as day,
            count(*) filter (where status = '200 OK') as status_ok,
            count(*) filter (where status != '200 OK') as status_not_ok
                from log
                    group by day;

select *
    from status_per_day
    where status_ok * 0.01 <= status_not_ok;
"""
