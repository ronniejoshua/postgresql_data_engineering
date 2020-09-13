CREATE INDEX idx_lname_fname
ON customers USING btree
(last_name, first_name);

CREATE INDEX idx_product_name
ON products USING hash
(product_name);