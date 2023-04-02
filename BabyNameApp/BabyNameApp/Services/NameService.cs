using System.Net.Http.Json;
using BabyNameApp.Model;

namespace BabyNameApp.Services
{
	public class NameService
	{
        HttpClient httpClient;

        public NameService()
		{
			httpClient = new HttpClient();
		}

        BabyName babyName = new ();

		public async Task<BabyName> GetName()
		{
			var url = "http://127.0.0.1:5000/random";

			var response = await httpClient.GetAsync(url);

			if(response.IsSuccessStatusCode)
			{
				babyName = await response.Content.ReadFromJsonAsync<BabyName>();
			}

			return babyName;
        }
	}
}

