import psycopg2

def insert_data(conn):
    '''' Insert data into a table '''
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
            #show column
            sql = ''' SELECT column_name FROM information_schema.columns '''
            sql += '''WHERE table_name ='{}'; '''.format(table_dict[chosen_table])
            cur.execute(sql)
            column_list = [col[0] for col in cur.fetchall()]
            print(column_list)

            #insert data
            print('Inserting data ...\n')
            name = input('Insert name :')
            desc = input('Insert description :')

            cur.execute(
                '''
                INSERT INTO {} ({}, {}) VALUES ('{}', '{}')  
                '''.format(table_dict[chosen_table], column_list[1],
                           column_list[2], name, desc)
                )
            conn.commit()
            print('{} data successfully saved!'.format(cur.rowcount))
        else:
            raise Exception('Table not found!')
    else:
        if chosen_table in table_dict.values():
            # show column
            sql = ''' SELECT column_name FROM information_schema.columns '''
            sql += '''WHERE table_name ='{}'; '''.format(chosen_table)
            cur.execute(sql)
            column_list = [col[0] for col in cur.fetchall()]
            print(column_list)

            # insert data
            print('Inserting data ...\n')
            name = input('Insert name :')
            desc = input('Insert description :')

            cur.execute(
                '''
                INSERT INTO {} ({}, {}) VALUES ('{}', '{}')  
                '''.format(chosen_table, column_list[1],
                           column_list[2], name, desc)
            )
            conn.commit()
            print('{} data successfully saved!'.format(cur.rowcount))
        else:
            raise Exception('Table not found!')