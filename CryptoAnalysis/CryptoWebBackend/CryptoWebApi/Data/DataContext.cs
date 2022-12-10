using CryptoWebApi.Extra;
using CryptoWebApi.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using CryptoWebApi.Models.Crypto;
namespace CryptoWebApi.Data;

public class DataContext : DbContext
{
    public string CreateSymbol { get; set; }

    private readonly IHttpContextAccessor _httpContextAccessor;
    
    //Dynamically change table according to the http request
    public DataContext(DbContextOptions<DataContext> options, IHttpContextAccessor httpContextAccessor) : base (options)
    {
        _httpContextAccessor = httpContextAccessor;
        CreateSymbol=_httpContextAccessor?.HttpContext?.Request?.Query["symbol"]??"ETHUSDT";
    }
    
    public DbSet<CryptoData> CryptoData { get; set;}

    public DbSet<AggregateData> AggregateData { get; set;}
    public DbSet<Prediction> Prediction { get; set;}



    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<CryptoData>(b =>
        {
            //b.ToTable(CreateSymbol.ToLower());
            b.ToTable(CreateSymbol??"ETHUSDT");
            b.HasKey(p => p.id);
        });
        
        modelBuilder.Entity<AggregateData>(b =>
        {
            //b.ToTable(CreateSymbol.ToLower());
            b.ToTable("aggregate_trade");
            b.HasKey(p => p.id);
        });
        
        modelBuilder.Entity<Prediction>(b =>
        {
            //b.ToTable(CreateSymbol.ToLower());
            b.ToTable("prediction");
            b.HasKey(p => p.id);
        });
        //modelBuilder.Entity<CryptoData>().ToTable(symbol);
    }
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)=> optionsBuilder.ReplaceService<IModelCacheKeyFactory, DynamicModelCacheKeyFactory>();
    
}