DELIMITER $$
 
DROP PROCEDURE IF EXISTS loaddata $$
CREATE PROCEDURE loaddata (IN data_file VARCHAR(1000))
BEGIN
    DECLARE load_sql VARCHAR(4000);
 
    DROP TABLE IF EXISTS testload;
    CREATE TABLE testload (name char(10), age tinyint, city char(30));
    INSERT INTO testload VALUES("Bob",27,"New York");
 
    SET load_sql=CONCAT('LOAD DATA LOCAL INFILE ',
                        '"', data_file, '" ',
                        'INTO TABLE testload ',
                        'FIELDS TERMINATED BY ","');
    SET @sql=load_sql;
    PREPARE s1 FROM @sql;
    EXECUTE s1;
    DEALLOCATE PREPARE s1;
END$$
 
DELIMITER ; 