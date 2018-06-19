use spiderData;
DROP EVENT IF EXISTS loadDataToMySQL
CREATE EVENT loadDataToMySQL
ON SCHEDULE EVERY 8 HOURS STARTS NOW()
ON COMPLETION PRESERVE
DO 
BEGIN
    load data local infile "/root/end1.txt" into table operrecord_18061901 fields terminated by ' ';
    load data local infile "/root/end2.txt" into table operrecord_18061901 fields terminated by ' ';
END 

