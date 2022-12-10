import pyspark
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType, FloatType
from pyspark.sql import functions as f
from pyspark.sql import types as t
from pyspark.sql import functions as f
from pyspark.sql import types as t
import psycopg2
from sqlalchemy import create_engine
from pathlib import Path
import datetime as dt


spark = SparkSession.builder.appName('final').getOrCreate()

#The columns are in capital and small so we have to make it case, sensetive. By default its off.
spark.conf.set('spark.sql.caseSensitive', True)

file_path = '/Users/pratyushpradhan/Developer/Personal/Projects/Crypto/RealTimeData'
df = spark.read.option('header','true').csv(file_path, inferSchema=True)


#TODO:  6 perform analytics task thorugh filter and search group by columns

#TRANSFORMATION

#drop columns
df= df.drop('B','x','f','L')

#rename
col_list=['start_time','close_time','symbol','interval','open','close','high','low','base_volume','num_trades'
,'quote_volume','taker_buy_base_volume','taker_buy_quote_volume']
df = df.toDF(*col_list)

#drop column if value null
df= df.na.drop(how='any', subset=['symbol','start_time','close_time','open','close','high','low','base_volume'])
#update date values from unix epoch timestamp to timestamp
#NOTE Unix epoch time is utc by default
df = df.withColumn('start_time', f.to_timestamp(df.start_time/1000)).withColumn('close_time', f.to_timestamp(df.close_time/1000))
#get distinct symbols from all columns
dist_symbols = df.select('symbol').distinct().rdd.flatMap(lambda x:x).collect()
#Convert spark dataframe to pandas
##df.show()
df = df.toPandas()
#create aggregate Datatable
df['close_date'] = (df['close_time']).dt.date
agg_df=df.groupby(['symbol','close_date']).sum().reset_index().copy()
agg_df=agg_df.rename(columns={'num_trades':'total_num_trades','base_volume': 'total_base_volume', 'quote_volume': 'total_quote_volume'})
agg_df=agg_df.loc[:,['symbol','close_date','total_num_trades','total_base_volume','total_quote_volume']]

#take only certain columns and rename them
#droping the temp column
df = df.drop('close_date', axis=1)
def createConnection(database,user,password,host,port):
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}?client_encoding=utf8")

#load data to database
#TODO: CREATE CONFIG fiLE
database=''
user=''
password= ''
host='127.0.0.1'
port= '5432'

#TODO: implement try catch  and logging
engine = createConnection(database,user,password,host,port)
#Code to insert to database

for value in dist_symbols:
    #note that the data table name is same as symbol name
    # TODO: if time add a query so that if new symbol comes and its corresponding datatable does not exist, create new table with a predefined schema
    #NOTE: always  " " inside filter at start function no ''
    #NOTE: for postgres take db in lowercase, we need to add  quotes (" ") always if taken to uppercase
    temp_df = df.query(f"symbol == '{value}' ").to_sql(value.lower(), engine, index=False, if_exists= 'append')
#insert aggregate database to postgres
table_name= 'aggregate_trade'
display(agg_df)
temp = agg_df.to_sql(table_name, engine, index=False, if_exists= 'append') 