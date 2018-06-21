use spiderData
CREATE EVENT IF NOT EXISTS loadDataToMySQL
ON SCHEDULE EVERY 28800 second
ON COMPLETION PRESERVE
DO load data local infile "/root/end1.txt" into table operrecord_18061901 fields terminated by ' ';
