using System.ComponentModel.DataAnnotations.Schema;

namespace CryptoWebApi.Models;

public class Prediction
{
    public int id { get; set; }
    [Column("close_time")]
    public DateTime CloseTime { get; set; }
    [Column("symbol")]
    public string Symbol { get; set; }
    [Column("prediction_value")]
    public double PredictionValue{ get; set; }
}