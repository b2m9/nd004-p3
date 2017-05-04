"""
1.) What are the most popular 3 articles of all time?

select articles.title, count(*) as visits
    from log, articles
    where path = ('/article/' || articles.slug)
    group by articles.title
    order by visits desc
    limit 3;
"""

"""
2.) Who are the most popular authors of all time

select authors.name, sum(subq.visits) as total
    from authors, 
        (select articles.title, articles.author, count(*) as visits
            from log, articles
            where path = ('/article/' || articles.slug)
            group by articles.title, articles.author
            order by visits desc) as subq
    where authors.id = subq.author
    group by authors.name
    order by total desc;
"""
