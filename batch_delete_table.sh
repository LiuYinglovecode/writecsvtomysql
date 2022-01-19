mysql -u root -p -e "Select CONCAT( 'drop table ', table_name, ';' )  FROM information_schema.tables   Where table_name LIKE 'example%';"  > re.txt
