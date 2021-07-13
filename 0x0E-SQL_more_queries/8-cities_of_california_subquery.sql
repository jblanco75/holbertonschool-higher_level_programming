-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The database name will be passed as an argument of the mysql command
SELECT name, id
FROM hbtn_0d_usa.cities
WHERE state_id = (
      	       	 SELECT id
		 FROM hbtn_0d_usa.states
		 WHERE name = "California")
ORDER BY id;
