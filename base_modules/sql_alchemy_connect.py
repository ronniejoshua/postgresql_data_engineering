import yaml
from sqlalchemy import create_engine
import logging

log = logging.getLogger(__name__)


def get_database():
    try:
        engine = get_connection_from_profile()
        log.info("Connected to PostgreSQL database!")
    except IOError:
        log.exception("Failed to get database connection!")
        return None, 'fail'

    return engine


def get_connection_from_profile(config_file_name="credentials.yaml"):
    """
    Sets up database connection from credentials.yaml file.
    Input:
    config_file_name: File containing host, user,
                      password, database, port, which are the
                      credentials for the PostgreSQL database
    """

    with open(config_file_name, 'r') as f:
        vals = yaml.full_load(f)

    if not ('host' in vals.keys() and
            'user' in vals.keys() and
            'password' in vals.keys() and
            'database' in vals.keys() and
            'port' in vals.keys()):
        raise Exception('Bad config file: ' + config_file_name)

    return get_engine(vals['database'], vals['user'],
                      vals['host'], vals['port'],
                      vals['password'])


def get_engine(db, user, host, port, passwd):
    """
    Get SQLalchemy engine using credentials.
    Input:
    db: database name
    user: Username
    host: Hostname of the database server
    port: Port number
    passwd: Password for the database
    """

    url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=user, passwd=passwd, host=host, port=port, db=db)
    engine = create_engine(url, pool_size=50)
    return engine


if __name__ == '__main__':
    get_database()
