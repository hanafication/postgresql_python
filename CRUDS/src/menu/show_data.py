import psycopg2

def show_data(conn):
    '''' Show data from certain table '''
    #set cursor
    cur = conn.cursor()

    #execute
    cur.execute(
        '''
        SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';
        ''')

    #fetch
    table_list = [name[0] for name in cur.fetchall()]

    print('List of available tables to choose :')
    table_dict = dict()
    for key, value in enumerate(table_list):
        print(key, value)
        table_dict[str(key)] = value

    #show data
    chosen_table = input('Choose Table: ')
    if chosen_table.isdigit() == True:
        if chosen_table in table_dict.keys():
            cur.execute(
                '''
                SELECT * FROM {} ORDER BY id;
                '''.format(table_dict[chosen_table]))

            print(cur.fetchall())
        else:
            raise Exception('Table not found!')
    else:
        if chosen_table in table_dict.values():
            cur.execute(
                '''
                SELECT * FROM {} ORDER BY id;
                '''.format(chosen_table))

            print(cur.fetchall())
        else:
            raise Exception('Table not found!')


