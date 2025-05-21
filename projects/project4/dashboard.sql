-- Create a sales table
CREATE TABLE sales (
    id INT PRIMARY KEY,
    product VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    sale_date DATE
);

-- Insert sample data
INSERT INTO sales VALUES (1, 'Laptop', 10, 999.99, '2025-01-01');
INSERT INTO sales VALUES (2, 'Phone', 25, 499.99, '2025-01-02');
INSERT INTO sales VALUES (3, 'Tablet', 15, 299.99, '2025-01-03');

-- Query total revenue by product
SELECT product, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;
