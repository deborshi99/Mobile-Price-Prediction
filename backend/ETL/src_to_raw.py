import pandas as pd
import sqlite3
import sys, traceback
import glob
import time 
import numpy as np

from ETL.constants import *

class ETL:
    def __init__(self, db_path):
        try:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            print("successfully connected to database")
           
        except:
            print("Error in connecting database!")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

    def create_table(self, table_name):
        self.cursor.execute(CHECK_IF_TABLE_EXIST)
        tables = self.cursor.fetchall()
        refined_tables = [i[0] for i in tables]
        if table_name in refined_tables:
            return 1
        else:
            return 0


    def SourceToRaw(self, data_path):

        table_craeted = self.create_table("RAW")
        if table_craeted == 0:
            self.cursor.execute(RAW_CREATE_TABLE_QUERY)
            self.conn.commit()
            print("Table created successfully!!")
        else:
            print("Table already created!!")
        csv_files = glob.glob(data_path + "/*.csv")
        df_list = (pd.read_csv(file) for file in csv_files)
        big_df = pd.concat(df_list, ignore_index=True)
        big_df["unique_data"] = big_df["px_height"]/big_df["px_width"] + big_df["ram"]
        print(big_df.head())
        self.cursor.execute("select count(*) from RAW")
        get_raw_count = self.cursor.fetchall()
        raw_count = int(get_raw_count[0][0])
        print(raw_count)
        try:
            if raw_count != 0:
                big_df = big_df.iloc[raw_count+1:, :]
            elif raw_count == 0 or raw_count is None:
                pass
            big_df.to_sql("RAW", con=self.conn, if_exists="append", index=False)
        except:
            print("Error inserting data")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)


    def close_connection(self):
        self.conn.close()
        print("Database connection is closed")
        
        

        



        


