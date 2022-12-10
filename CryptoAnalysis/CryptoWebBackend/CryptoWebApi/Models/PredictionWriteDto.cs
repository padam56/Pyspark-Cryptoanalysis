namespace CryptoWebApi.Models;

public class PredictionWriteDto
{
    public string CloseTime { get; set; }
    public string Symbol { get; set; }
    public string PredictionValue { get; set; }

    public PredictionWriteDto()
    {
    }
}