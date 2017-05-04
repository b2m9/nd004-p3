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
select date, trunc(ratio::numeric * 100, 2) from
    (select to_char(day, 'DD Mon YYYY') as date,
        (status_not_ok::float / status_ok::float) as ratio
            from status_per_day_in_july) as sub
    where ratio >= 0.01;
"""
