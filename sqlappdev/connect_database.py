import psycopg2
from sqlappdev.config import params
import sqlappdev.parameterized_query as pq

if __name__ == "__main__":
    try:
        conn = psycopg2.connect(**params)
    except psycopg2.OperationalError as err:
        print(err)
        conn = None

    cursor = conn.cursor()

    all_ovens = pq.get_products_by_type(conn, 'oven')
    print(len(all_ovens))

    pq.avoid_n_plus_one(conn, all_ovens)
    pq.get_product_orders_by_type(conn, 'oven')
    pq.get_product_orders_by_type_quantity(conn, 'oven', 2)
