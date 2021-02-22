import psycopg2

def create_table(conn):
    '''' Creating table into chosen database with fixed columns'''
    #create cursor
    cur = conn.cursor()

    #execute
    table_name = input('Choose name of a table: ')
    cur.execute(
        '''
        SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{}' 
        '''.format(table_name))

    #check availability
    if cur.fetchone()[0] == 1:
        raise Exception('Table already exist!')
        pass
    else:
        #checking table if total table less than or equal 3
        if len(cur.fetchall()) < 4:
            cur.execute(
                '''
                CREATE TABLE {} (
                    id SERIAL PRIMARY KEY, 
                    name VARCHAR(30) NOT NULL,
                    description VARCHAR(255) NOT NULL ) 
                '''.format(table_name))
            conn.commit()
            print('Yoho! Table has been created!')
        else:
            raise Exception('Maximum table allowed = 3!')
            pass


