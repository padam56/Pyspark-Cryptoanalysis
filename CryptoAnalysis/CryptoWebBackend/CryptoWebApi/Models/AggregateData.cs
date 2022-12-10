
namespace CryptoWebApi.Models;
using System.ComponentModel.DataAnnotations.Schema;

public class AggregateData
{
        public AggregateData()
        {
        }

        public int id { get; set; }
        [Column("symbol")]
        public string Symbol { get; set; }        
        [Column("close_date")] 
        public DateTime CloseDate { get; set; }
        [Column("total_num_trades")]
        public double TotalNumTrades { get; set; }
        [Column("total_base_volume")] 
        public double TotalBaseVolume { get; set; }
        [Column("total_quote_volume")] 
        public double TotalQuoteVolume { get; set; }
    
}