namespace CryptoWebApi.Models;

public class MLData
{
    public int id { get; set; }
    public DateTime CloseTime { get; set; }
    public string Symbol { get; set; }
    public int IntervalInMin { get; set; }
    public double Close { get; set; }

    public MLData()
    {
    }
}