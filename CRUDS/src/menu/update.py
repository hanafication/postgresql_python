import psycopg2

def update(conn):
    '''' update an existing row of a table '''
    #set cursor
    cur = conn.cursor()

    #execute
    cur.execute(
        '''
        SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';
        ''')

    # fetch
    table_list = [name[0] for name in cur.fetchall()]

    print('List of available tables to choose :')
    table_dict = dict()
    for key, value in enumerate(table_list):
        print(key, value)
        table_dict[str(key)] = value

    # show data
    chosen_table = input('Choose Table: ')
    if chosen_table.isdigit() == True:
        if chosen_table in table_dict.keys():
            # show rows in chosen table
            sql = ''' SELECT * FROM {}; '''.format(table_dict[chosen_table])
            cur.execute(sql)
            column_list = [col for col in cur.fetchall()]
            print(column_list, '\n')

            # update data
            row = int(input('Choose row that want to be updated.'))
            if row in [i[0] for i in column_list]:
                print('Updating data ...\n')
                name = input('Change name :')
                desc = input('Change description :')

                cur.execute(
                    '''
                    UPDATE {} SET name = '{}', description = '{}' WHERE id = {}  
                    '''.format(table_dict[chosen_table], name, desc, row)
                )
                conn.commit()
                print('{} data successfully saved!'.format(cur.rowcount))
            else:
                raise Exception('Row ID not found!')
        else:
            raise Exception('Table not found!')
    else:
        if chosen_table in table_dict.values():
            # show column
            sql = ''' SELECT * FROM {} '''.format(chosen_table)
            cur.execute(sql)
            column_list = [col for col in cur.fetchall()]
            print(column_list)

            # update data
            row = int(input('Choose row that want to be updated.'))
            if row in column_list:
                print('Updating data ...\n')
                name = input('Change name :')
                desc = input('Change description :')

                cur.execute(
                    '''
                    UPDATE {} SET name = '{}', description = '{}' WHERE id = {}  
                    '''.format(chosen_table, name, desc, row)
                )
                conn.commit()
                print('{} data successfully saved!'.format(cur.rowcount))
            else:
                raise Exception('Row ID not found!')
        else:
            raise Exception('Table not found!')