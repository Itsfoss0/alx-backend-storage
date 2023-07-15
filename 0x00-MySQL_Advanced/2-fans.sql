-- rank the origin of metal rock bands

SELECT origin, SUM(fans) as nb_fans from metal_bands
GROUP BY  origin
ORDER BY nb_fans desc;
