from ETL.constants import *
from ETL.src_to_raw import ETL
from ETL.raw_to_consumption import RawToConsumptionETL

a = RawToConsumptionETL("./database/data.db")
a.RawToConsumption(fill_value="mean", drop=False, src_table="RAW")
a.close_connection()

