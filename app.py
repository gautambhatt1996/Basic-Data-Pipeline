import sys
from config import DB_DETAILS
from util import get_tables,load_db_details
from read import read_table


def main():
    env = sys.argv[1]
    db_details = load_db_details(env)
    # print(db_details)
    tables = get_tables('tables_list.txt')
    # for idx,table in tables.iterrows():
    #    print (table)
    for table_name in tables['table_name']:
        print(f'reading data for {table_name}')
        data,column_names=read_table(db_details,table_name)
        print(f'loading data for {table_name}')





if __name__ == '__main__':
    main()
