def get_products_by_type(db_conn, prod_type):
    cursor = db_conn.cursor()
    sql_string = """
                    SELECT * 
                    FROM products 
                    WHERE product_type = %s;
                """
    # Executing a query string and passing a product type
    cursor.execute(sql_string, [prod_type])
    return cursor.fetchall()


def avoid_n_plus_one(db_conn, product_iter):
    cursor = db_conn.cursor()
    fetchall_cnt = 0
    result = 0

    for oven in product_iter:
        oven_id = oven[0]
        sql_string = """
                        SELECT * 
                        FROM product_orders 
                        WHERE product_id = %s;
                    """
        cursor.execute(sql_string, [oven_id])
        oven_order = cursor.fetchall()
        result += len(oven_order)
        fetchall_cnt += 1
    print(f"Total fetch request to the db server {fetchall_cnt} and returned {result} records")


def get_product_orders_by_type(db_conn, prod_type):
    cursor = db_conn.cursor()
    sql_string = """
                    SELECT po.* 
                    FROM product_orders AS po
                    INNER JOIN products AS p
                    ON po.product_id = p.product_id
                    WHERE p.product_type = %s;
                """
    cursor.execute(sql_string, [prod_type])
    oven_order = cursor.fetchall()
    print(f"Total fetch request to the db server 1 and returned {len(oven_order)} records")
    return len(oven_order)


def get_product_orders_by_type_quantity(db_conn, prod_type, qnty_ord=1):
    cursor = db_conn.cursor()
    sql_string = """
                    SELECT po.* 
                    FROM product_orders AS po
                    INNER JOIN products AS p
                    ON po.product_id = p.product_id
                    WHERE p.product_type = %s
                    AND po.quantity > %s;
                """
    cursor.execute(sql_string, [prod_type, qnty_ord])
    oven_order = cursor.fetchall()
    print(f"Total fetch request to the db server 1 and returned {len(oven_order)} records")
    return len(oven_order)
