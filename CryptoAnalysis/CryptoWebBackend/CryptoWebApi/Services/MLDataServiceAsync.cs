using CryptoWebApi.Data;
using CryptoWebApi.Models;
using CryptoWebApi.Services.Wrapper;
using Microsoft.EntityFrameworkCore;

namespace CryptoWebApi.Services;

public class MLDataServiceAsync : IMLDataServiceAsync
{
    private DataContext _dbContext;

    public MLDataServiceAsync(DataContext dbContext)
    {
        _dbContext = dbContext;
        
    }

    // public async Task<ServiceResponse<List<MLData>>> GetCloseDataBySymbolInterval(string symbol,DateTime closeTime, int IntervalInMin,
    //      int count = 1)
    // {
    //     int loopCount = 1;
    //     ServiceResponse<List<MLData>> serviceResponse = new ServiceResponse<List<MLData>>();
    //     try
    //     {
    //
    //         var tempData = await _dbContext.CryptoData
    //             // .Where(x => x.Symbol == symbol && x.CloseTime <= closeTime)
    //             .Where(x => x.Symbol == symbol.ToUpper())
    //             .OrderBy(x => x.CloseTime)
    //             .Select(x => new MLData()
    //                 { Close = x.Close, Symbol = x.Symbol, CloseTime = x.CloseTime, IntervalInMin = IntervalInMin })
    //             //.Take(IntervalInMin * count)
    //             .ToListAsync();
    //
    //         if (tempData == null || tempData.Count() == 0)
    //         {
    //             return serviceResponse;
    //         }
    //
    //         List<MLData> result = new List<MLData>();
    //
    //         foreach (var data in tempData)
    //         {
    //             data.id = loopCount;
    //             if (loopCount % IntervalInMin == 0 || 
    //                 (loopCount == tempData.Count() && result.Count() == 0))
    //             {
    //                 result.Add(data);
    //             }
    //             loopCount++;
    //         }
    //         serviceResponse.Data = result;
    //     }
    //     catch (Exception e)
    //     {
    //         Console.WriteLine(e);
    //         throw;
    //     }
    //     return serviceResponse;
    // }
    
    public async Task<ServiceResponse<List<MLData>>> GetCloseDataBySymbolInterval(string symbol,DateTime closeTime, int IntervalInMin,
        int count = 1)
    {
        int loopCount = 1;
        ServiceResponse<List<MLData>> serviceResponse = new ServiceResponse<List<MLData>>();
        try
        {

            var tempData = await _dbContext.CryptoData
                // .Where(x => x.Symbol == symbol && x.CloseTime <= closeTime)
                .Where(x => x.Symbol == symbol.ToUpper() && x.CloseTime <= closeTime)
                .OrderByDescending(x => x.CloseTime)
                .Select(x => new MLData()
                    { Close = x.Close, Symbol = x.Symbol, CloseTime = x.CloseTime, IntervalInMin = IntervalInMin })
                .Take(IntervalInMin * count)
                .ToListAsync();

            if (tempData == null || tempData.Count() == 0)
            {
                return serviceResponse;
            }

            serviceResponse.Data = tempData;
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
            throw;
        }
        return serviceResponse;
    }


    public async Task<ServiceResponse<Prediction>> AddPredictionData(PredictionWriteDto predictionWriteDto)
    {
        ServiceResponse<Prediction> serviceResponse = new ServiceResponse<Prediction>();
        Prediction value = new Prediction()
        {
            Symbol = predictionWriteDto.Symbol, PredictionValue = double.Parse(predictionWriteDto.PredictionValue),
            CloseTime = DateTime.Parse(predictionWriteDto.CloseTime)
        };
        try
        {
            await _dbContext.AddAsync(value);
            _dbContext.SaveChanges();
            serviceResponse.Data = value;
        
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
            throw;
        }
        
        return serviceResponse;
    }

    public async Task<ServiceResponse<Prediction>> GetPredictionData(string symbol, DateTime date)
    {
        ServiceResponse<Prediction> value = new ServiceResponse<Prediction>();
        value.Data = await _dbContext.Prediction.Where(x => x.Symbol == symbol && x.CloseTime > date)
                            .OrderByDescending(x => x.CloseTime).FirstOrDefaultAsync();
        return value;
    }
}