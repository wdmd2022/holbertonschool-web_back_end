-- this SQL script lists all bands with `Glam rock` as their main style,
-- ranked by longevity. It uses the metal_bands sql table dump and the
-- column names must be: `band_name` and `lifespan` (in years)
-- lifespan is computed using attributes `formed` and `split`
-- script can be executed on any database
SELECT band_name,
(COALESCE(split, 2020) - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC
