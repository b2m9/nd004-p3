# ## QUERY FOR FIRST QUESTION
# Select top 3 articles
TOP_ARTICLES = """
    select title, visits
        from visits_per_article
        order by visits desc
        limit 3;
"""

# ## QUERY FOR SECOND QUESTION
# Select authors sorted by visits of their respective articles
TOP_AUTHORS = """
    select authors.name, sum(visits_per_article.visits) as total
        from authors, visits_per_article
            where authors.id = visits_per_article.author_id
            group by authors.name
            order by total desc;
"""
# ## QUERY FOR THIRD QUESTION
# Select all dates with an error rate of more than 1%
# Less readable query but no post-processing needed
ERROR_DATES = """
select date, trunc(ratio::NUMERIC * 100, 2) from 
    (select to_char(day, 'DD Mon YYYY') as date,
        (status_not_ok::float / status_ok::float) as ratio 
            from status_per_day_in_july) as sub
    where ratio >= 0.01;
"""

"""
1.) What are the most popular 3 articles of all time?

create materialized view visits_per_article as
    select articles.title as title,
        articles.author as author_id,
        count(*) as visits
            from log, articles
            where path = ('/article/' || articles.slug)
            group by title, author;





2.) Who are the most popular authors of all time?

select authors.name, sum(visits_per_article.visits) as total
    from authors, visits_per_article
        where authors.id = visits_per_article.author_id
        group by authors.name
        order by total desc;



3.) On which days did more than 1% of requests lead to errors?

create materialized view status_per_day_in_july as
    select date_trunc('day', time) as day,
            count(*) filter (where status = '200 OK') as status_ok,
            count(*) filter (where status != '200 OK') as status_not_ok
                from log
                    group by day;

select to_char(day, 'DD Mon YYYY') as date,
    status_ok as ok, status_not_ok as not_ok
    from status_per_day_in_july
    where status_ok * 0.01 <= status_not_ok;

select * from 
    (select to_char(day, 'DD Mon YYYY') as date,
        (status_not_ok::float / status_ok::float) as ratio 
            from status_per_day_in_july) as sub
    where ratio >= 0.01;
"""
