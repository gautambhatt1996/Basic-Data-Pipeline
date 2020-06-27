import sys
from config import DB_DETAILS
from util import get_tables


def main():
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    # print(db_details)
    tables = get_tables('tables_list.txt')
    # for idx,table in tables.iterrows():
    #    print (table)
    for table in tables['table_name']:
        print(table)


if __name__ == '__main__':
    main()
