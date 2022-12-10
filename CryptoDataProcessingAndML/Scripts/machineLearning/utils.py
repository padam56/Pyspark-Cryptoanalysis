import os
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import LSTM, Dense
import requests



def change_timestamp (ts):
    digit_count = len(str(ts))
    if digit_count == 12:
        return (datetime.utcfromtimestamp(ts)).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return (datetime.utcfromtimestamp(ts/1000)).strftime('%Y-%m-%d %H:%M:%S')

def data_processing(path):
    
    df = pd.read_csv(path)
    
    df['dt_correct'] = df.Open_time.apply(lambda x: change_timestamp(x))
    df['Date'] = pd.to_datetime(df.dt_correct.values)
    df.drop(columns=['Close_time','Quote_asset_volume','Taker_buy_base_asset_volume','Taker_buy_quote_asset_volume','Ignore','dt_correct','Open_time','Volume','Number_of_trades'],inplace=True)
    df = df.set_index('Date')
    
    df = df[['Close']]
    
    return df

def scaling_dataPoints(data,scale_factor=(0,1)):
    
    df_values = data.values.reshape(-1,1)
    scaler = MinMaxScaler(feature_range= scale_factor)
    scaler = scaler.fit(df_values)
    df_values = scaler.transform(df_values)
    
    return scaler,df_values

def input_and_output_sequence(data,n_lookback,n_forecast):
    
    X = []
    Y = []

    for i in range(n_lookback, len(data) - n_forecast + 1):
        X.append(data[i - n_lookback: i])
        Y.append(data[i: i + n_forecast])
    
    return np.array(X), np.array(Y)
   

def train_keras_model(X_train, y_train, epochs, batch_size,forecast,lookback, shuffle=False):
  
# Initializing the Neural Network based on LSTM
  model = Sequential()  
  model.add(LSTM(units=50,return_sequences=True,input_shape=(lookback,1)))
  model.add(LSTM(units=50))
  model.add(Dense(forecast))
  model.compile(optimizer='adam',loss='mean_squared_error')

  model.fit(X_train, y_train, shuffle=shuffle, validation_split = 0.1, epochs=epochs, verbose=2, batch_size=batch_size)
  return model

def isotime(datestring):
    datestring = str(datestring)
    return datestring.replace("T"," ").split('.')[0]

def getHourlyData(symbol,closeDate,interval,count):
    base_url= "https://localhost:7089/MLData/GetMLData"
    #api_url = f"{base_url}?symbol=ethusdt&closeDate=2022-11-22 00:00:00&intervalInMin=60&count=24"
    api_url = f"{base_url}?symbol={symbol.upper()}&closeDate={closeDate}&intervalInMin={interval}&count={count}"
    response = requests.get(api_url, verify=False)
    print(response.json())
#close time, symbol, prediciton
def postPredictionData(symbol,closeTime,prediction):
    #TODO: add interval column in prediciton db
    api_url="https://localhost:7089/MLData/AddPrediction"
    myobj = { 'close_time':closeTime, 'symbol': symbol.upper(),'prediction':prediction }
    response = requests.post(api_url,json= myobj, verify=False)
    print(response.json())



data = {"data": [
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1256.51
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1259.1
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1253.67
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1264.73
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1259.65
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1262.31
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1296.01
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1266.59
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1285.11
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1285.83
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1297.08
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1259.74
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1295.79
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1297.31
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1290.85
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1288.75
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1294.3
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1301.64
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1295.13
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1292.15
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1290.7
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1290.31
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1300.64
    },
    {
      "id": 0,
      "closeTime": "2022-12-02T10:53:20",
      "symbol": "ETHUSDT",
      "intervalInMin": 1,
      "close": 1259.41
    }
  ]
}

