import pandas as pd
import mysql.connector as connector
from mysql.connector.errors import Error

def reader(file):
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
    try:
        conn = connector.connect(
            host='localhost',
            user='root', 
            password='', 
            database='heroku_72b766963b50486',  
            charset='utf8'
        )
        cursor = conn.cursor()

        for(row, rs) in table.iterrows():

            for i in range(len(rs)):
                if type(rs[i+1]) == type('s') and (' ' in rs[i+1] or rs[i+1].isalpha()):
                    rs[i+1] = '\''+rs[i+1]+'\''

            column_list = []
            cursor.execute('describe '+tablename)
            schemma = cursor.fetchall()

            for i in range(len(schemma)):
                column_list.append(schemma[i][0])
            column_list = column_list[1:len(column_list)-1]

            print('List of Columns: ',column_list)
            
            query = "insert into "+str(tablename)+" ("+", ".join(str(column) for column in column_list)+") values ( "+", ".join(str(ele) for ele in rs)+")"            
            print(query)
            cursor.execute(query)
    
        conn.commit()
        conn.close()

        return True
    
    except Error as e:
        print('Error in MySQL Database Conection: '+str(e))
    finally:
        conn.close()

    
