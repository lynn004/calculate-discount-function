-- 1. Create a new database called salesDB
CREATE DATABASE salesDB;

-- 2. Drop (delete) the database called demo
DROP DATABASE demo;
--3.  retrieve the checkNumber, paymentDate, and amount from the payments table.

USE DATABASE salesDB;
SELECT checkNumber, paymentDate, amount
FROM payments;

--4. retrieve the orderDate, requiredDate, and status of orders currently 'In Process' from the orders table. 
--Sort the results in descending order of orderDate
USE salesDB;

SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

