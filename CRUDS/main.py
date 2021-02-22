import psycopg2
import pandas as pd
from config.config import config
from src.data.db_connect import connect
from src.menu.create import create_table
from src.menu.insert import insert_data
from src.menu.show_data import show_data
from src.menu.update import update
from src.menu.delete import delete

#Connecting to database
print('Connecting to Database...')
conn = connect()
print('Connection established!\n')

#menu
def show_menu(conn):
    while(True):
        print('=== Welcome to CRUDS APP ===')
        print('===MENU===')
        print('1. Create New Table')
        print('2. Insert Data into a Table')
        print('3. Update Data from a Table')
        print('4. Delete Data from a Table')
        print('5. Show Data from a Table')
        print('6. Exit\n')

        print('Please Choose Your Action!')
        menu = int(input('Choosen Menu : '))

        if menu == 1:
            create_table(conn)
        elif menu == 2:
            insert_data(conn)
        elif menu == 3:
            update(conn)
        elif menu == 4:
            delete(conn)
        elif menu == 5:
            show_data(conn)
        elif menu == 6:
            print('Closing App...')
            conn.cursor().close()
            exit()
        else:
            print('Please Choose The Menu!')

if __name__ == '__main__':
    show_menu(conn)