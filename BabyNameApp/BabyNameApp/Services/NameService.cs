using System.Net.Http.Json;

namespace BabyNameApp.Services
{
	public class NameService
	{
        HttpClient httpClient;

        public NameService()
		{
			httpClient = new HttpClient();
		}
	}
}

