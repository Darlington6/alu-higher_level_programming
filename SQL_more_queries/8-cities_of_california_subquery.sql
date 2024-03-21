-- This script lists all cities in California that can be found in the Database.
SELECT cities.id, cities.name FROM cities, states
WHERE cities.state_id = states.id
	AND states.name = 'California'
	ORDER BY cities.id ASC;
