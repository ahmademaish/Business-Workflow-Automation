/* Inventory and Workflow Automation Schema
Handles stock tracking and automated reorder flagging.
*/

CREATE TABLE inventory (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    current_stock DECIMAL(10, 2) NOT NULL,
    reorder_threshold DECIMAL(10, 2) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE daily_sales (
    sale_id INT PRIMARY KEY,
    item_id INT,
    quantity_sold DECIMAL(10, 2),
    sale_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (item_id) REFERENCES inventory(item_id)
);

/* System Query: Automatically flags items that need to be reordered today */
SELECT 
    i.item_name, 
    i.current_stock, 
    i.reorder_threshold 
FROM 
    inventory i
WHERE 
    i.current_stock <= i.reorder_threshold;