using CryptoWebApi.Models;
using CryptoWebApi.Services;
using Microsoft.AspNetCore.Mvc;
using CryptoWebApi.Models.Crypto;
using CryptoWebApi.Services.Wrapper;

namespace CryptoWebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class MLDataController : ControllerBase
{
    private readonly ILogger<CryptoDataController> _logger;
    private readonly IMLDataServiceAsync _mlDataServiceAsync;

    public MLDataController(ILogger<CryptoDataController> logger, IMLDataServiceAsync mlDataServiceAsync)
    {
        _mlDataServiceAsync = mlDataServiceAsync;
        _logger = logger;
    }
    [Route("GetMLData")]
    [HttpGet()]
    public async Task<IActionResult> GetMLData(string symbol, string closeDate, int intervalInMin, int count)
    {
        if ( string.IsNullOrWhiteSpace(symbol) || string.IsNullOrWhiteSpace(closeDate))
        {
            return NotFound();
        }

        dynamic result = await _mlDataServiceAsync.GetCloseDataBySymbolInterval(symbol,
            DateTime.Parse(closeDate), intervalInMin,  count);

        if (result.Data == null) 
            return NotFound(result);
        
        return Ok(result);
        
    }
    
    //[Route("GetMLData")]
    [HttpGet("GetPredictionData")]
    public async Task<IActionResult> GetPredictionData(string symbol, string closeDate)
    {
        if (string.IsNullOrWhiteSpace(symbol) || !DateTime.TryParse(closeDate, out DateTime date))
        {
            return NotFound();
        }
        ServiceResponse<Prediction> result = await _mlDataServiceAsync.GetPredictionData(symbol.ToUpper(),DateTime.Parse(closeDate));
        if (result.Data == null) 
            return NotFound(result);
        
        return Ok(result);
    }


    [HttpPost("AddPrediction")]
    public async Task<IActionResult> AddPrediction(PredictionWriteDto predictionWriteDto)
    {
        return Ok(await _mlDataServiceAsync.AddPredictionData(predictionWriteDto));
    }


}