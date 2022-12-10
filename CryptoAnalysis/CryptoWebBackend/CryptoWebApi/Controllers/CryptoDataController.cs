using CryptoWebApi.Models;
using CryptoWebApi.Models.Crypto;
using CryptoWebApi.Services;
using CryptoWebApi.Services.Wrapper;
using Microsoft.AspNetCore.Mvc;
using CryptoWebApi.Models.Crypto;

namespace CryptoWebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class CryptoDataController : ControllerBase
{
    
    private readonly ILogger<CryptoDataController> _logger;
    private readonly ICryptoDataServiceAsync _cryptoDataServiceAsync;

    public CryptoDataController(ILogger<CryptoDataController> logger, ICryptoDataServiceAsync cryptoDataServiceAsync  )
    {
        _cryptoDataServiceAsync = cryptoDataServiceAsync;
        _logger = logger;
    }
    [Route("GetCryptoData")]
    [HttpGet()]
    public async Task<IActionResult> GetCryptoData(string symbol, string startDate, string closeDate,string dataType = "")
    {
        dynamic result;
        if ( !string.IsNullOrWhiteSpace(dataType) && dataType.ToLower().Equals("ohlcv"))
        {
            result = await _cryptoDataServiceAsync.GetOHLCVBySymbol(symbol,
                DateTime.Parse(startDate), DateTime.Parse(closeDate));
        }
        else
        {
            result = await _cryptoDataServiceAsync.GetCryptoBySymbol(symbol,
                DateTime.Parse(startDate), DateTime.Parse(closeDate));
        }
        
        if (result.Data == null) 
            return NotFound(result);
        return Ok(result);
    }
    [Route("GetAllAggregateData")]
    [HttpGet()]
    public async Task<IActionResult> GetAggregateData(string closeDate)
    {
        ServiceResponse<List<AggregateData>> result =  await _cryptoDataServiceAsync.GetAllAggregateData(DateTime.Parse(closeDate));
        if (result.Data == null) 
            return NotFound(result);
        return Ok(result);
    }

    
}
