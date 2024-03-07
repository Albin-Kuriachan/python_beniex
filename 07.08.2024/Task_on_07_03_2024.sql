
-- Create a Schemas in name Employee 

use Employee; 

-- Create table Employe_Info  
CREATE TABLE Employee_Info (
    Employee_ID INT NOT NULL PRIMARY KEY,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL,
    Hire_Date DATE NOT NULL,
    Phone_Number VARCHAR(15) NOT NULL,
    Email VARCHAR(100) NOT NULL
);

-- Inserting data to the table Employee_Info
INSERT INTO  my.employee_info VALUES (1, 'Albin', 'Kuriachan', 'IT', 'Manager', 25, 60000, '2022-01-01', '1234567890', 'ak@gmail.com');
INSERT INTO my.employee_info VALUES (2, 'Amit', 'Kumar', 'HR', 'HR Specialist', 28, 55000, '2022-02-15', '9876543210', 'akumar@gmail.com');
INSERT INTO my.employee_info VALUES (3, 'Priya', 'Patel', 'Marketing', 'Marketing Executive', 30, 65000, '2022-03-01', '5555555555', 'ppatel@gmail.com');
INSERT INTO my.employee_info VALUES (4, 'Rahul', 'Sharma', 'Finance', 'Financial Analyst', 32, 70000, '2022-04-01', '1112223333', 'rsharma@gmail.com');
INSERT INTO my.employee_info VALUES (5, 'Sunita', 'Singh', 'IT', 'Developer', 35, 75000, '2022-05-15', '9998887777', 'ssingh@gmail.com');
INSERT INTO my.employee_info VALUES (6, 'Deepak', 'Gupta', 'Sales', 'Sales Manager', 40, 80000, '2022-06-01', '7777777777', 'dgupta@gmail.com');
INSERT INTO my.employee_info VALUES (7, 'Neha', 'Verma', 'HR', 'HR Manager', 45, 85000, '2022-07-15', '6666666666', 'nverma@gmail.com');
INSERT INTO my.employee_info VALUES (8, 'Aarti', 'Yadav', 'Finance', 'Accountant', 28, 60000, '2022-08-01', '4444444444', 'ayadav@gmail.com');
INSERT INTO my.employee_info VALUES (9, 'Manoj', 'Thakur', 'Marketing', 'Marketing Assistant', 33, 70000, '2022-09-15', '3333333333', 'mthakur@gmail.com');
INSERT INTO my.employee_info VALUES (10, 'Anjali', 'Joshi', 'IT', 'System Administrator', 38, 80000, '2022-10-01', '2222222222', 'ajoshi@gmail.com');

-- Selcet all the data in the table  
SELECT * FROM employee_info

-- Selcet sorted data
SELECT Employee_ID,First_Name, Last_Name, Department, Position FROM Employee_Info;

-- Select employees with a age grater than 18
SELECT * FROM my.employee_info WHERE Age > 18;

-- Select employees with a salary between 50000 and 70000
SELECT * FROM My.employee_Info WHERE salary between 70000 and 80000;

-- Select employees with letter y in first name
SELECT * FROM Employee_Info WHERE First_Name LIKE '%y%';

-- Select employees with  last name start with letter s
SELECT * FROM Employee_Info WHERE Last_Name LIKE 's%';

-- Find the average salaryy of the employee
SELECT AVG(Salary) AS Average_Salary FROM Employee_Info;

-- Find the cout of employees in each department
SELECT Department, COUNT(*) AS Num_Employees FROM Employee_Info GROUP BY Department;

-- Find the total number of employees
SELECT COUNT(*) AS Total_Employees FROM Employee_Info;

-- Select the employee info based on the age in assending order
SELECT * FROM Employee_Info ORDER BY Age ASC;

-- Select the employee info with particular ID
SELECT * FROM Employee_Info WHERE Employee_ID IN (1,3,10,5);

-- Select the employee with age less than 50 and work in IT department
SELECT * FROM Employee_Info WHERE Age < 50 and Department = 'IT';

-- Select the employee with age less than 26 or work in IT Marketing department

SELECT * FROM Employee_Info WHERE Age < 26 or Department = 'Marketing';

--  Select distinct departments
SELECT DISTINCT Department FROM Employee_Info;

-- To delete a column
ALTER TABLE Employee_Info DROP COLUMN Hire_Date ;

-- To delete a raw
DELETE FROM Employee_Info WHERE Employee_ID = 10;

-- Add new column
ALTER TABLE Employee_Info ADD COLUMN Date_of_Birth DATE;

-- update the column Date_of_Birth
UPDATE Employee_Info SET Date_of_Birth = '1998-08-31'   WHERE Employee_ID = 1;



SELECT * FROM employee_info








