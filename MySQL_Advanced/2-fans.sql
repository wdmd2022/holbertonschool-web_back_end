-- this SWL script ranks the country origins of bands (from the provided
-- metal_bands.sql file) by number of (non-unique) fans. Requirements:
-- * column names must be `origin` and `nb_fans`
-- * script can be executed on any database
SELECT origin, SUM(fans) nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
