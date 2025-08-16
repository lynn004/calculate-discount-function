-- 1. Create a new database called salesDB
CREATE DATABASE salesDB;

-- 2. Drop (delete) the database called demo
DROP DATABASE demo;

--WEEK 2 ASSIGNMENT:

--3.  retrieve the checkNumber, paymentDate, and amount from the payments table.
USE DATABASE salesDB;
SELECT checkNumber, paymentDate, amount
FROM payments;

--4. retrieve the orderDate, requiredDate, and status of orders currently 'In Process' from the orders table. 
--Sort the results in descending order of orderDate
USE DATABASE salesDB;
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

--5.query to display the firstName, lastName, and email of employees:job title is 'Sales Rep'
-- and order them in descending order of employeeNumber.
USE DATABASE salesDB;
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

--6. query to retrieve all the columns and records from the offices table.
USE DATABASE salesDB;
SELECT *
FROM offices;

--7.query to fetch the productName and quantityInStock from the products table.
USE DATABASE salesDB;
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;

-- WEEK 3 ASSIGNMENT:

-- 1. Create table
CREATE TABLE IF NOT EXISTS student (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fullName VARCHAR(100),
    age INT
);

-- 2. Insert at least 3 records into the student table
INSERT INTO student (fullName, age)
VALUES
    ('Alice Johnson', 20),
    ('Brian Otieno', 22),
    ('Catherine Njeri', 19);

-- 3. Update the age of the student with ID 2 to 20
UPDATE student
SET age = 20
WHERE id = 2;












