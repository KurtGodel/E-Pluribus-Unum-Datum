DROP TABLE IF EXISTS statistics;
CREATE TABLE statistics (
    statistic_id smallint,
    region_id smallint,
    year smallint,
    value double precision
);
DROP TABLE IF EXISTS statlookup;
CREATE TABLE statlookup (
    statistic_id smallint,
    statistic_name text,
    start_year smallint,
    end_year smallint
);
DROP TABLE IF EXISTS regionlookup;
CREATE TABLE regionlookup (
    region_name text,
    region_id smallint
);

\copy statistics FROM 'stat1.csv' DELIMITER ',' CSV
\copy statistics FROM 'stat2.csv' DELIMITER ',' CSV
\copy statistics FROM 'stat3.csv' DELIMITER ',' CSV
\copy statistics FROM 'stat4.csv' DELIMITER ',' CSV
\copy statistics FROM 'stat5.csv' DELIMITER ',' CSV
\copy statistics FROM 'stat6.csv' DELIMITER ',' CSV
\copy statistics FROM 'stat7.csv' DELIMITER ',' CSV
\copy statistics FROM 'stat8.csv' DELIMITER ',' CSV
\copy statistics FROM 'stat9.csv' DELIMITER ',' CSV
\copy statlookup FROM 'statlookup.csv' DELIMITER ',' CSV
\copy regionlookup FROM 'regionlookup.csv' DELIMITER ',' CSV
