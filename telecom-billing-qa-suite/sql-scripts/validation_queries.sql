SELECT * FROM Billing WHERE status='Unpaid';
SELECT c.name, SUM(b.amount) FROM Customers c JOIN Billing b ON c.id=b.customer_id GROUP BY c.name;
