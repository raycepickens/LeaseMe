using System.Diagnostics.Contracts;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text.Json.Serialization;
using System.Threading.RateLimiting;

namespace LeaseMe.Components.Data
{
    public class Lease
    {
        public string Poster { get; set; }         
        public string Contact { get; set; }        
        public string ImgId { get; set; }          
        public string PropertyInfo { get; set; }   
        public double Price { get; set; }          
        public string LeasePeriod { get; set; }
        public string PropertyName { get; set; }


        public override string ToString()
        {
            return $"{Poster} is posting a property at {PropertyName} for ${Price}" +
                $" from {LeasePeriod} \nadditional property info: {PropertyInfo}\nContact them at {Contact}";
        }
    }
}
