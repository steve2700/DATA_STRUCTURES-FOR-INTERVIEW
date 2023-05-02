I learned about using the MOD IN SQL TO SELECT EVEN NUMBERS 
I learned about using DISTINCT WHICH DONT INCLUDE DUPLICATES
SELECT DISTINCT CITY FROM STATION WHERE ID%2 = 1;
DISTINCT is used to remove duplicates from the query result. In this case, we want to query for city names from the STATION table that have an even ID number. It's possible that multiple rows in the table have the same city name, so using DISTINCT ensures that only unique city names are returned in the query result.






