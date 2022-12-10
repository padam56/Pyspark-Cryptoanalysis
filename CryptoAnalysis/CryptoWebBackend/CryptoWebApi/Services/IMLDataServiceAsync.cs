using CryptoWebApi.Models;
using CryptoWebApi.Services.Wrapper;

namespace CryptoWebApi.Services;

public interface IMLDataServiceAsync
{
    public Task<ServiceResponse<List<MLData>>> GetCloseDataBySymbolInterval (string symbol,DateTime closeTime,int IntervalInMin, int count);
    //NO
    public Task<ServiceResponse<Prediction>> AddPredictionData (PredictionWriteDto predictionWriteDto);
    public Task<ServiceResponse<Prediction>> GetPredictionData (string symbol,DateTime date);

}