import { useEffect, useState } from "react";
import ReactApexChart from "react-apexcharts";
import dayjs from "dayjs";

export const CandleStickChart = ({ symbol, startDate, endDate }) => {
  const [ohclvData, setOhclvData] = useState([{}]);
  const [options, setOptions] = useState({});
  //https://localhost:7089/CryptoData?symbol=ethusdt&startDate=2022-11-21%2020%3A15%3A00&closeDate=2022-11-21%2020%3A44%3A59.999&dataType=ohlcv
  const endPoint = "https://localhost:7089/CryptoData/GetCryptoData";

  useEffect(() => {
    setOptions({
      chart: {
        type: "candlestick",
        height: 350,
      },
      title: {
        text: "CandleStick Chart",
        align: "left",
      },
      xaxis: {
        type: "datetime",
        labels: {
          formatter: function (val) {
            return dayjs(val).format("MMM DD HH:mm");
          },
        },
      },
      yaxis: {
        tooltip: {
          enabled: true,
        },
      },
    });
  }, []);
  useEffect(() => {
    getAndsetCryptoData(symbol, "1m", startDate, endDate);
    //getAndsetCryptoData(symbol,'1m','2022-11-21 20:15:00','2022-11-21 20:44:59.999')
  }, [symbol, startDate, endDate]);

  const requestBuilder = (
    symbol,
    interval = "1m",
    startDate,
    closeDate,
    dataType = ""
  ) =>
    `${endPoint}?symbol=${symbol}&startDate=${startDate}&closeDate=${closeDate}&dataType=${dataType}`;

  const getAndsetCryptoData = (symbol, interval, startDate, closeDate) => {
    if(symbol && startDate &&  closeDate)
    {
      console.log("in here!");
      fetch(requestBuilder(symbol, interval, startDate, closeDate, "ohlcv")).then(
        (res) => {
          if (res.ok) {
            console.log("Success");
          } else {
            console.log("Connection Failed");
          }
          return res
            .json()
            .then((val) => setOhclvData([{ name: "candle", data: val.data }]));
        }
      );
    }
  };

  return (
    <div>
      {console.log(ohclvData)}
      <ReactApexChart
        options={options}
        series={ohclvData}
        type="candlestick"
        height={350}
      />
    </div>
  );
};
