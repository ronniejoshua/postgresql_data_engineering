from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlappdev.config import params


def get_database(parms):
    try:
        engine = get_connection_from_profile(parms)
        print("Connected to PostgreSQL database!")
    except IOError:
        print("Failed to get database connection!")
        return None, 'fail'

    return engine


def get_connection_from_profile(params):
    if not ('host' in params.keys() and
            'user' in params.keys() and
            'password' in params.keys() and
            'database' in params.keys() and
            'port' in params.keys()):
        raise Exception("Bad Configuration Provided - Please check again")

    return get_engine(params['database'], params['user'],
                      params['host'], params['port'],
                      params['password'])


def get_engine(db, user, host, port, password):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(url, pool_size=50)
    return engine


if __name__ == "__main__":
    engine = get_database(params)

    Session = sessionmaker(engine)
    session = Session()

    base = declarative_base()

    class Product(base):
        __tablename__ = 'products'
        product_id = Column(Integer, primary_key=True)
        product_name = Column(String)
        product_type = Column(String)

    class Supplier(base):
        __tablename__ = 'suppliers'
        supplier_id = Column(Integer, primary_key=True)
        supplier_name = Column(String)
        supplier_region = Column(String)
        supplier_level = Column(Integer)

    # products = session.query(Product)
    # for product in products:
    #     print(product.product_name)

    products = session.query(Product).filter(Product.product_type == 'fryer')
    for product in products:
        print(product.product_name)
