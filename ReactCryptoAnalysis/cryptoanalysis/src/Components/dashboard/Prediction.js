import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import Title from './Title';
import { useState,useEffect } from 'react';
import {getCurrentDateTime} from '../../Utils/Utils';


export default function Prediction({symbol}) {

  const [predValue, setPredValue] = useState({});



  const endPoint = "https://localhost:7089/MLData/GetPredictionData";
  const requestBuilder = (symbol,date) => `${endPoint}?symbol=${symbol}&closeDate=${date}`

  useEffect(()=>
  {
    getAndSetPredictionData(symbol)
    console.log(`prediction value = ${predValue.predictionValue}`)
  },[symbol])




  const getAndSetPredictionData = (symbol ) => {
    if(symbol)
    {
      let date = getCurrentDateTime()
      console.log(`prediction date here! ${date} `);
      // fetch(requestBuilder(symbol,date))
      //     .then((res) => {
      //     if (res.ok) {
      //       console.log("Success");
      //     } else {
      //       console.log("Connection Failed");
      //     }
      //     return res.json()
            
      //   }).then((val) => {
      //     console.log(val.data)
      //     setPredValue(val.data)
      //     console.log(predValue)})

          fetch(requestBuilder(symbol,date))
          .then((response) => response.json())
          .then((val) => setPredValue(val.data));
    }
  };


  return (
    <>
      <Title>Prediction</Title>
      <Typography>{symbol?.toUpperCase()}</Typography>
      <Typography component="p" variant="h4">
        {predValue?.predictionValue}
      </Typography>
      <Typography color="text.secondary" sx={{ flex: 1 }}>
        {/* for 15 March, 2022 */}
        {predValue?.closeTime}
      </Typography>
      <div>
        <Link color="primary" href="#" >
          View Prediction Chart
        </Link>
      </div>
    </>
  );
}
