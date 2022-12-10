using CryptoWebApi.Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;


namespace CryptoWebApi.Extra;


    public class DynamicModelCacheKeyFactory : IModelCacheKeyFactory
    {
        public object Create(DbContext context, bool designTime) => context is DataContext dynamicContext 
                ? (context.GetType(), dynamicContext.CreateSymbol,designTime) : (object)context.GetType();
    }
    
