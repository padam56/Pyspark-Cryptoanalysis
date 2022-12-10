using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations.Schema;

namespace CryptoWebApi.Models.Crypto;

public class CryptoData
{
    public int id { get; set; }
    [Column("start_time")]
    public DateTime StartTime { get; set; }
    [Column("close_time")]
    public DateTime CloseTime { get; set; }
    [Column("symbol")]
    public string Symbol { get; set; }
    [Column("interval")]
    public string Interval { get; set; }
    [Column("open")]
    public double Open { get; set; }
    [Column("close")]
    public double  Close { get; set; }
    [Column("high")]
    public double High { get; set; }
    [Column("low")]
    public double Low { get; set; }
    [Column("base_volume")]
    public double BaseVolume { get; set; }
    [Column("num_trades")]
    public int NumTrades { get; set; }
    [Column("quote_volume")]
    public double QuoteVolume { get; set; }
    [Column("taker_buy_base_volume")]
    public double TakerBuyBaseVolume { get; set; }
    [Column("taker_buy_quote_volume")]
    public double TakerBuyQuoteVolume { get; set; }

    // public CryptoData(int id, DateTime startTime, DateTime closeTime, string symbol, string interval, double open, 
    //     double close, double high, double low, double baseVolume, int numTrades, double quoteVolume,
    //     double takerBuyBaseVolume, double takerBuyQuoteVolume)
    // {
    //     this.id = id;
    //     StartTime = startTime;
    //     CloseTime = closeTime;
    //     Symbol = symbol;
    //     Interval = interval;
    //     Open = open;
    //     Close = close;
    //     High = high;
    //     Low = low;
    //     BaseVolume = baseVolume;
    //     NumTrades = numTrades;
    //     QuoteVolume = quoteVolume;
    //     TakerBuyBaseVolume = takerBuyBaseVolume;
    //     TakerBuyQuoteVolume = takerBuyQuoteVolume;  
    // }

    public CryptoData()
    {
    }
}