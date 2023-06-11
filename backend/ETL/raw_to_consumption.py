import pandas as pd
import sqlite3
import sys, traceback
import glob
import time 
import numpy as np

from ETL.constants import *
from ETL.src_to_raw import ETL

class RawToConsumptionETL(ETL):
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


    def get_missing_values_column(self, df):
        cols = [x for x in df.columns]
        null_values = df.isnull().sum().to_list()

        columns_having_null_value = [cols[i] for i in range(len(cols)) if null_values[i] > 0]
        result_dict = {}
        for col in columns_having_null_value:
            result_dict[col] = df[col].dtype.name

        return result_dict
    
    def fill_nan_value(self, df, fill_value, drop=False):
        cols_dtype_dict = self.get_missing_values_column(df)
        if drop == False:
            for cols in cols_dtype_dict.keys():
                if fill_value == "mean":
                    mean = df[cols].mean()
                    df[cols].fillna(mean, inplace = True)
                elif fill_value == "median":
                    median = df[cols].median()
                    df[cols].fillna(median, inplace = True)
                elif fill_value == "mode":
                    median = df[cols].mode()[0]   
                    df[cols].fillna(median, inplace = True)
        else:
            df.dropna(inplace=True)
        return df
    
    def RawToConsumption(self, fill_value, drop, src_table):
        table_created = self.create_table("CONSUMPTION")
        if table_created == 0:
            self.cursor.execute(CONSUMPTION_CREATE_TABLE_QUERY)
            self.conn.commit()
            print("Table created successfully!!")
        else:
            print("Table already created!!")
        src_table_if_created = self.create_table("RAW")
        if src_table_if_created == 0:
            print("{} table is not present in the database".format(src_table))
        elif src_table_if_created == 1:
            df = pd.read_sql('SELECT * FROM {}'.format(src_table), self.conn)
            updated_df = self.fill_nan_value(df=df, fill_value=fill_value, drop=drop)
            self.cursor.execute("select count(*) from CONSUMPTION")
            get_consumption_count = self.cursor.fetchall()
            consumption_count = int(get_consumption_count[0][0])
            print(consumption_count)
            try:
                if consumption_count != 0:
                    updated_df = updated_df.iloc[consumption_count+1:, :]
                elif consumption_count == 0 or consumption_count is None:
                    pass
                updated_df.to_sql("CONSUMPTION", con=self.conn, if_exists="append", index=False)
            except:
                print("Error inserting data")
                print("-"*60)
                traceback.print_exc(file=sys.stdout)
                print("-"*60)

    
    def close_connection(self):
        self.conn.close()
        print("Database connection is closed")