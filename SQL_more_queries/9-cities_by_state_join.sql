-- This script lists all cities in the Database.
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = states.id ORDER BY cities.id ASC;

