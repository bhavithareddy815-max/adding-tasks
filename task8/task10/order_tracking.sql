

CREATE DATABASE IF NOT EXISTS order_tracking_db;
USE order_tracking_db;

-- 4.1 Main Table – orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    status VARCHAR(50),
    amount DECIMAL(10,2)
);

-- 4.2 Log Table – order_log
CREATE TABLE IF NOT EXISTS order_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    action VARCHAR(10),
    old_status VARCHAR(50),
    new_status VARCHAR(50),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5.1 Trigger for INSERT (New Order)
DELIMITER //
CREATE TRIGGER log_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    INSERT INTO order_log(order_id, action, new_status)
    VALUES (NEW.order_id, 'INSERT', NEW.status);
END;
//
DELIMITER ;

-- 5.2 Trigger for UPDATE (Status Change)
DELIMITER //
CREATE TRIGGER log_order_update
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    INSERT INTO order_log(order_id, action, old_status, new_status)
    VALUES (OLD.order_id, 'UPDATE', OLD.status, NEW.status);
END;
//
DELIMITER ;

-- 6. View for Daily Order Activity
CREATE VIEW daily_order_report AS
SELECT 
    DATE(changed_at) AS report_date,
    COUNT(*) AS total_updates
FROM order_log
GROUP BY DATE(changed_at);

-- 7. Verification / Sample Data
-- Place new orders
INSERT INTO orders (customer_name, product_name, status, amount) 
VALUES ('Ravi', 'Laptop', 'Placed', 50000.00);

INSERT INTO orders (customer_name, product_name, status, amount) 
VALUES ('Anita', 'Smartphone', 'Placed', 60000.00);

-- Simulate status transitions
UPDATE orders SET status = 'Shipped' WHERE order_id = 1;
UPDATE orders SET status = 'Delivered' WHERE order_id = 1;
UPDATE orders SET status = 'Shipped' WHERE order_id = 2;

-- Review Audit Logs
SELECT * FROM order_log;

-- Review Daily Report
SELECT * FROM daily_order_report;