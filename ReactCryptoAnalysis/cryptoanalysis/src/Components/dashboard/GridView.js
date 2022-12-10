import { useEffect, useState } from "react";
import { DataGrid } from '@mui/x-data-grid';
import {getCurrentDate} from '../../Utils/Utils';

export const GridView =() =>
{
    const [aggData, setAggData]= useState([])
    
    const endPoint = "https://localhost:7089/CryptoData/GetAllAggregateData";

    // const requestBuilder = ( ) => `${endPoint}?closeDate=${getCurrentDate()}` '2022-11-21'
    const requestBuilder = ( ) => `${endPoint}?closeDate=${getCurrentDate()}`

  
    
    const  getAndSetAggData =  () =>
    {
        console.log('Aggregate Data')
        fetch(requestBuilder())
        .then((res)=> res.json())
        .then((val)=> setAggData(val.data) )
    }
    
    const columns = [
        // { field: 'id', headerName: 'Id', width: 150 },
        { field: 'symbol', headerName: 'Symbol', width: 150 },
        { field: 'closeDate', headerName: 'Date', width: 200 },
        { field: 'totalNumTrades', headerName: 'Total Number of Trades', width: 200 },
        { field: 'totalBaseVolume', headerName: 'Total Base Volume', width: 200 },
        { field: 'totalQuoteVolume', headerName: 'Total Quote Volume', width: 200 },
      ];

      useEffect(()=>
      {
          //first call 
          getAndSetAggData()
      },[])

    useEffect(()=>
    {
        // call every 5 minutes
        const interval = setInterval(()=>getAndSetAggData(), 50000) 
        return () => { clearInterval(interval)}

    },[])
    //getRowId={(row)=>row.id}

    return(
        <div style={{ height: 400, width: '100%' }}>
        <DataGrid 
        rows={aggData} 
        columns={columns} 
        pageSize={10}

        // getRowId={(row) => row.id}
        />
      </div>)
}