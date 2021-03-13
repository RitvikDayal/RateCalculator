# Utility import to handle excel data
import pandas as pd

# MySQL Support imports
import mysql.connector as connector
from mysql.connector.errors import Error

def reader(file):
    '''
    Reads the excel file and returns the dictionary of tables corresponding to each table Id
    '''
    tables = { 1: 5, 2: 5, 3: 5, 4: 5, 5: 4, 6: 5, 7: 6, 8: 3, 9: 3, 10: 3 }

    df = pd.read_excel(file, engine='openpyxl', sheet_name='Data', header=None)
    df = df[[0,1,2,3,4,5,6]]

    for i in tables:
        temp_df = df.loc[df[0] == i]
        temp_df.drop([0], axis=1, inplace=True)
        temp_df = temp_df.reset_index(drop=True)
        tables[i] = temp_df[[index for index in range(1, tables[i]+1)]]
        tables[i].dropna(inplace=True)

    return tables

def upload2SQL(table, tablename):
    '''
    Accepts a table and table name and uploads it to the MySQL Database return True on successful update and false on failure.

    Parameters: Table - pandas dataframe.
                Tablename - name of the table in the database.
    '''
    try:
        # Establishing Connection to the databse.
        conn = connector.connect(
            host='localhost', # hostname
            user='root', # username
            password='', # password
            database='heroku_72b766963b50486',  #databse to use
            charset='utf8' # characterset of the database
        )

        # creating cursor to run query on database.
        cursor = conn.cursor()

        # Iterating through rows in the table.
        for(row, rs) in table.iterrows():
            '''
            Checking for any string data in the rows and enclosing the data in ' '.
            '''
            for i in range(len(rs)):
                if type(rs[i+1]) == type('s') and (' ' in rs[i+1] or rs[i+1].isalpha()):
                    rs[i+1] = '\''+rs[i+1]+'\''

            # Extracting column names for the table to pass in the query
            column_list = []
            cursor.execute('describe '+tablename)
            schemma = cursor.fetchall() # Extracting schemma of the table

            for i in range(len(schemma)):
                # Iterating through the schemma to extract column names.
                column_list.append(schemma[i][0])
            column_list = column_list[1:len(column_list)-1] # Removed First nad last column from the list ( Autogenrated columns )

            # print('List of Columns: ',column_list) # Debug statement to print column list
            
            # Query as string to run on the database.
            query = "insert into "+str(tablename)+" ("+", ".join(str(column) for column in column_list)+") values ( "+", ".join(str(ele) for ele in rs)+")"            
            print(query) #statement to print query to be run on the database

            cursor.execute(query) # Excuting Query

        # Commit the changes
        conn.commit()
        # Closing the connection to the database.
        conn.close()

        return True
    
    except Error as e:
        '''
        Excepts any error while running a query on the database and prints the error occurred
        '''
        print('Error in MySQL Database Conection: '+str(e))
    finally:
        # Finally closing the connection to the Database.
        conn.close()

    
