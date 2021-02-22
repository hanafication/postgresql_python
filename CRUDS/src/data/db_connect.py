import psycopg2
from config.config import config

def connect():
    ''' Make a connection to database '''
    conn = None
    try:
        #read connection parameters
        params = config()

        #connect to db server
        print('Establishing connection to database server ...')
        conn = psycopg2.connect(**params)

        #Create cursor
        curr = conn.cursor()

        #execute statement
        print('PostgreSQL database version')
        curr.execute('SELECT version()')

        #fetching execute
        db_ver = curr.fetchone()
        print(db_ver)

        #close communication
     #   curr.close()
    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
    #finally:
    #    if conn is not None:
    #       conn.close()
    #       print('Database connection terminated')

    return conn

if __name__ == ' __main__':
    connect()

