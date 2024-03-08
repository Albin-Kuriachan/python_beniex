
-- 1) Set suitable SQL contraints to column while creating tables.

	select * from sales_order
	select * from customer_master
	
	ALTER TABLE customer_master
	MODIFY COLUMN Customer_ID VARCHAR(50) NOT NULL;
	ALTER TABLE customer_master 
	ADD PRIMARY KEY (Customer_ID);
	
	ALTER TABLE sales_order 
	MODIFY COLUMN OrderDate DATE;
	ALTER TABLE sales_order 
	ADD PRIMARY KEY (Sales_ID);




-- 2) Write a command to display first 10 rows.
	SELECT so.OrderDate,so.Sales_ID,so.Customer_ID,cm.Customer,so.Item,so.Unit_Cost,so.Total,cm.Region  FROM sales_order so
	JOIN customer_master cm ON cm.Customer_ID = so.Customer_ID LIMIT 10;


-- 3)Identify unique items?
	SELECT DISTINCT Item FROM sales_order;

-- 4) Identify any unit cost is negative?
	SELECT * FROM sales_order WHERE Unit_Cost < 0;
    
-- 5) Identify minimum and maximum unit price happened for same item.
	SELECT Item, MIN(Unit_Cost) AS Min_Unit_Cost, MAX(Unit_Cost) AS Max_Unit_Cost FROM sales_order GROUP BY Item;

-- 6) Identify the Total sales happened in the year of 2021?
	SELECT SUM(Total) AS Total_Sales_2021 FROM sales_order WHERE YEAR(OrderDate) = 2021;
    
    
 -- 7) Which item is sold maximum in the year 2021?   
    SELECT Item, SUM(Units) AS Total_Units_Sold FROM sales_order WHERE YEAR(OrderDate) = 2021 
    GROUP BY Item ORDER BY Total_Units_Sold DESC LIMIT 1;
    
-- 8) Identify the region with highest and lowest sales.
	SELECT cm.Region, SUM(so.Total) AS total_sales FROM customer_master AS cm
	JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID
	GROUP BY cm.Region ORDER BY total_sales DESC LIMIT 1;

	SELECT cm.Region, SUM(so.Total) AS total_sales FROM customer_master AS cm
	JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID GROUP BY cm.Region ORDER BY total_sales ASC LIMIT 1;
    

-- 9) Identify the customer name having highest sales for the year 2022.

	SELECT cm.Customer, SUM(so.Total) AS Total_Sales FROM sales_order so
	INNER JOIN customer_master cm ON so.Customer_ID = cm.Customer_ID
	WHERE YEAR(so.OrderDate) = 2022 GROUP BY cm.Customer ORDER BY Total_Sales DESC LIMIT 1;


-- 10) Which item has highest and lowest unit cost?

	SELECT Item, MAX(Unit_Cost) AS Highest_Unit_Cost FROM sales_order GROUP BY Item ORDER BY Highest_Unit_Cost DESC LIMIT 1;
	
	SELECT Item, MIN(Unit_Cost) AS Lowest_Unit_Cost FROM sales_order GROUP BY Item ORDER BY Lowest_Unit_Cost ASC LIMIT 1;

	

-- 11) Identify items starts with letter 'P'.
	SELECT so.OrderDate,so.Sales_ID,so.Customer_ID,cm.Customer,so.Item,so.Unit_Cost,so.Total,cm.Region  FROM sales_order so
	JOIN customer_master cm ON cm.Customer_ID = so.Customer_ID WHERE Item LIKE 'P%';


-- 12) Filter the table having items Pen and Pencil.
	SELECT so.OrderDate,so.Sales_ID,so.Customer_ID,cm.Customer,so.Item,so.Unit_Cost,so.Total,cm.Region  FROM sales_order so
	JOIN customer_master cm ON cm.Customer_ID = so.Customer_ID WHERE Item IN ('Pen', 'Pencil');

-- 13) Filter the table with unit cost between 1 and 100.
	SELECT * FROM sales_order WHERE Unit_Cost BETWEEN 1 AND 100;


-- 14) Identify the customer with more no of transaction(no of entries).
	SELECT Customer_ID, COUNT(*) AS Transaction_Count FROM sales_order
	GROUP BY Customer_ID ORDER BY Transaction_Count DESC LIMIT 1;

-- 15) Identify which item has maximum sales in each region.
	SELECT cm.Region, so.Item, SUM(so.Total) AS Total_Sales
	FROM sales_order so
	INNER JOIN customer_master cm ON so.Customer_ID = cm.Customer_ID
	GROUP BY cm.Region, so.Item
	ORDER BY cm.Region, Total_Sales DESC;



-- 16) Create 5 more scenarios using important inbuilt functions of MySQL.

-- 16.1: Counting the number of unique customers
	SELECT COUNT(DISTINCT Customer_ID) AS Unique_Customers FROM sales_order;

-- 16.2: Getting the average total sales
	SELECT AVG(Total) AS Average_Sales FROM sales_order;

-- 16.3 : Getting the latest order date
	SELECT MAX(OrderDate) AS Latest_Order_Date FROM sales_order;

-- 16.4: Calculating the total sales per customer
	SELECT cm.Customer, SUM(so.Total) AS Total_Sales FROM sales_order so
	INNER JOIN customer_master cm ON so.Customer_ID = cm.Customer_ID GROUP BY cm.Customer;

-- 16.5: Calculating the total sales per month
	SELECT YEAR(OrderDate) AS Year, MONTH(OrderDate) AS Month, SUM(Total) AS Total_Sales
	FROM sales_order GROUP BY YEAR(OrderDate), MONTH(OrderDate);




