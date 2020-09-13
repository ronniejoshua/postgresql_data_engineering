COPY product_orders FROM '/Users/ronniejoshua/Downloads/posgresql_data_engineering/sqlappdev/data/product_orders.csv' DELIMITER ',' CSV HEADER;
COPY products FROM '/Users/ronniejoshua/Downloads/posgresql_data_engineering/sqlappdev/data/products.csv' DELIMITER ',' CSV HEADER;
COPY orders FROM '/Users/ronniejoshua/Downloads/posgresql_data_engineering/sqlappdev/data/orders.csv' DELIMITER ',' CSV HEADER;
COPY customers FROM '/Users/ronniejoshua/Downloads/posgresql_data_engineering/sqlappdev/data/customers.csv' DELIMITER ',' CSV HEADER;
