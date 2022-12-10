using CryptoWebApi.Models.Crypto;

namespace CryptoWebApi.Models;

public class OHLCV
{
    public DateTime? x { get; set; }
    public List<Double>? y { get; set; }

    public Double? volume { get; set; }

    public static List<OHLCV> covertDataToOHLCV(List<CryptoData> data)
    {
        if (data == null)
        {
            return null;
        }

        var newData = data.AsEnumerable()
                                    .Select(val=> new OHLCV(){x=val.CloseTime, y = new List<double>(){val.Open, val.High, val.Low, val.Close},volume = val.BaseVolume})
                                    .ToList();
        return newData;
    }

}
