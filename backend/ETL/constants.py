TRAIN_DATA_PATH = "../dataset/train_data/"
TEST_DATA_PATH = "../dataset/test.csv"

DATABASE_PATH = "../database/data.db"

RAW_CREATE_TABLE_QUERY = """
    CREATE TABLE RAW(
        unique_data DECIMAL PRIMARY KEY,
        battery_power INTEGER,
        blue INTEGER,
        clock_speed DECIMAL,
        dual_sim INTEGER,
        fc INTEGER,
        four_g INTEGER,
        int_memory INTEGER,
        m_dep DECIMAL,
        mobile_wt INTEGER,
        n_cores INTEGER,
        pc INTEGER,
        px_height INTEGER,
        px_width INTEGER,
        ram INTEGER,
        sc_h INTEGER,
        sc_w INTEGER,
        talk_time INTEGER,
        three_g INTEGER,
        touch_screen INTEGER,
        wifi INTEGER,
        price_range INTEGER,
        RawTimeStamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
"""

CONSUMPTION_CREATE_TABLE_QUERY = """
    CREATE TABLE CONSUMPTION(
        unique_data DECIMAL PRIMARY KEY,
        battery_power INTEGER,
        blue INTEGER,
        clock_speed DECIMAL,
        dual_sim INTEGER,
        fc INTEGER,
        four_g INTEGER,
        int_memory INTEGER,
        m_dep DECIMAL,
        mobile_wt INTEGER,
        n_cores INTEGER,
        pc INTEGER,
        px_height INTEGER,
        px_width INTEGER,
        ram INTEGER,
        sc_h INTEGER,
        sc_w INTEGER,
        talk_time INTEGER,
        three_g INTEGER,
        touch_screen INTEGER,
        wifi INTEGER,
        price_range INTEGER,
        RawTimeStamp TIMESTAMP,
        ConsumptionTimeStamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    )
"""
CHECK_IF_TABLE_EXIST = 'SELECT name from sqlite_master where type= "table"'



