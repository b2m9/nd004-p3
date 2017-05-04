"""
1.) What are the most popular 3 articles of all time?

select articles.title, count(*) as c
    from log, articles
    where path = ('/article/' || articles.slug)
    group by articles.title
    order by c desc
    limit 3;
"""
