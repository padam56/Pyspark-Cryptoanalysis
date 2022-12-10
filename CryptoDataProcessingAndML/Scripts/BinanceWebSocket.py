import websocket
import json 
import logging
from datetime import datetime
import csv


class CryptoExtractSchedule:
    def __init__(self,streams,interval,output_path):
        self.streams=streams
        self.interval=interval
        self.output_path= output_path
        self.json_data_collection=[]
    
    def write_to_csv(self):
        print(f'Data collection Value = {self.json_data_collection}')###

        if((not self.json_data_collection) and len(self.json_data_collection)==0):
            return

        dt_string = datetime.now().strftime("%d-%m-%Y %H:%M:%S").replace(" ", "").replace(':','-')
        final_output_path= self.output_path+'cryptoData'+dt_string+'.csv'
        data_file = open(final_output_path, 'w', newline='')
        csv_writer = csv.writer(data_file)
        count = 0
        for data in self.json_data_collection:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values()) 
        data_file.close()
        #reset value
        self.json_data_collection=[]
    
    def on_open(self,ws):
        print("Binance connected ...")
        self.prev_date=datetime.now()
        try:
            subscribe = {"method":"SUBSCRIBE","params":self.streams,"id":1}
            ws.send(json.dumps(subscribe))
        except Exception as e:
            logging.ERROR(e)
            print(e)

    def on_message(self,ws, message):
        json_message = json.loads(message)
        is_candle_closed=False
        if(json_message and  'k' in json_message):
            candle = json_message['k']
            is_candle_closed= candle['x']
        if(is_candle_closed):
            print(f'inisde is candle closed with candle value = {candle}' )### inside isCandle closed
            self.json_data_collection.append(candle)
        
        #custom sceduling, inserting data to csv every 10 mins
        self.cur_date = datetime.now()
        if(((self.cur_date - self.prev_date).seconds)/60 >=10):
            self.write_to_csv()
            self.prev_date=self.cur_date

        # print(self.json_data_collection)
        #after every 10 minutes dump the data to a csv file
        #schedule.every(1).minutes.do(self.write_to_csv)
        

    def on_error(self,ws, error):
        ###logging.ERROR(error)
        print(error)

    def on_close(self,ws):
        print("Connection Closed!")

    # def get_socket(self):
    #     socket = 'wss://stream.binance.com:9443/ws'
    #     self.ws = websocket.WebSocketApp(socket,on_open= lambda ws,msg: self.on_open(ws),
    #                                      on_close= lambda ws: self.on_close(ws), 
    #                                      on_message = lambda ws,msg: self.on_message(ws,msg), 
    #                                      on_error= lambda ws,msg: self.on_error(ws,msg))
    #     return self.ws

    def run(self):
        socket = 'wss://data-stream.binance.com/ws'
        self.ws = websocket.WebSocketApp(socket,on_open= self.on_open,
                                         on_close= self.on_close, 
                                         on_message = self.on_message, 
                                         on_error= self.on_error)
        self.ws.run_forever()


interval = '1m'
streams = [f"ethusdt@kline_{interval}",f"btcusdt@kline_{interval}",f"xrpusdt@kline_{interval}",f"bnbusdt@kline_{interval}",f"dogeusdt@kline_{interval}",f"adausdt@kline_{interval}",f"maticusdt@kline_{interval}",
f"dotusdt@kline_{interval}",f"solusdt@kline_{interval}",f"usdcusdt@kline_{interval}"]

#TODO : FIX logging
logging.basicConfig(filename='GetCryptoData.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

file_path = '/Users/pratyushpradhan/Developer/Personal/Projects/Crypto/RealTimeData/'
obj = CryptoExtractSchedule(streams,interval,file_path)
temp = obj.run()