from utils import data_processing,scaling_dataPoints,input_and_output_sequence,train_keras_model,isotime,postPredictionData
import pandas as pd
import json
from tensorflow.keras.models import load_model
import requests

n_lookback = 24
n_forecast = 1

def model_training(path):

    df = data_processing(path)

    scaler, scaled_df = scaling_dataPoints(df)

    X, Y = input_and_output_sequence(scaled_df,n_lookback=n_lookback,n_forecast=n_forecast)

    model = train_keras_model(X, Y, epochs = 20, batch_size = 32, forecast = n_forecast, lookback = n_lookback, shuffle = False)
    model_name = path.split('/')[-1].split('-')[0]
    model.save(f'final_model_{model_name}.h5')

    return model, scaler
    

def model_selection_and_prediction(data_json,scaler):
    file = json.dumps(data_json['data'])
    df = pd.read_json(file)
    
    for index, row in df.iterrows():
        df['Date'] = isotime(row['CloseDate'])
        
    df = df.drop(columns=['CloseTime'],inplace=True)
    
    date_plus_one = pd.to_datetime(df['Date']).iloc[-1] + pd.Timedelta(hours=1)
    
    df_close = df[['Close']]
    
    sym = df['Symbol'].unique()[0]
    
    df_close = scaler.transform(df_close)
    X_ = df_close.reshape(1,n_lookback,1)
    
    if sym == 'ETHUSDT':
        model = load_model('./final_model_ETHUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(date_plus_one,Y_)
        
    elif sym == 'ADAUSDT':
        model = load_model('./final_model_ADAUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    elif sym == 'BNBUSDT':
        model = load_model('./final_model_BNBUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    elif sym == 'BTCUSDT':
        model = load_model('./final_model_BTCUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    elif sym == 'DOGEUSDT':
        model = load_model('./final_model_DOGEUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    elif sym == 'DOTUSDT':
        model = load_model('./final_model_DOTUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    elif sym == 'MATICUSDT':
        model = load_model('./final_model_MATICUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    elif sym == 'SOLUSDT':
        model = load_model('./final_model_SOLUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    elif sym == 'USDCUSDT':
        model = load_model('./final_model_USDCUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    elif sym == 'XRPUSDT':
        model = load_model('./final_model_XRPUSDT.h5')
    
        Y_ = model.predict(X_).reshape(-1,1)
        Y_ = scaler.inverse_transform(Y_)
        print(Y_)
        
    else:
        print('No Tickets exists! Try Again!')
    
    
    
    def getHourlyData():
        api_url = "https://jsonplaceholder.typicode.com/todos/1"
        response = requests.get(api_url)
        response.json()

    
     





