CREATE TABLE Customers (id INT PRIMARY KEY, name VARCHAR(50));
CREATE TABLE Billing (id INT PRIMARY KEY, customer_id INT, amount DECIMAL, status VARCHAR(20));
CREATE TABLE Payments (id INT PRIMARY KEY, billing_id INT, amount DECIMAL);
