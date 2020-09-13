from base_modules.sql_alchemy_connect import get_database

# Make PostgreSQL Connection
engine = get_database()
print(engine)

with engine.connect() as con:
    print(con)
    rs = con.execute('SELECT customer_id FROM public.customer limit 2;')
    for r in rs:
        print(r)


