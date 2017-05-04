--
-- Materialised view: visits_per_article
-- title: text, author_id: integer, visits: bigint
--

create materialized view visits_per_article as
    select articles.title as title,
        articles.author as author_id,
        count(*) as visits
            from log, articles
            where path = ('/article/' || articles.slug)
            group by title, author;

--
-- Materialised view: status_per_day_in_july
-- day: timestamp, status_ok: bigint, status_not_ok: bigint
--

create materialized view status_per_day_in_july as
    select date_trunc('day', time) as day,
            count(*) filter (where status = '200 OK') as status_ok,
            count(*) filter (where status != '200 OK') as status_not_ok
                from log
                    group by day;
