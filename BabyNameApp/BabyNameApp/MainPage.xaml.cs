using BabyNameApp.Services;
using BabyNameApp.Model;

namespace BabyNameApp;

public partial class MainPage : ContentPage
{

	public MainPage()
	{
		InitializeComponent();
	}

	NameService nameService = new NameService();

	BabyName currentName = new BabyName();

	public async void GetNextName(object sender, EventArgs e)
	{
		currentName = await nameService.GetName();
        NextBtn.Text = currentName.Name;

		if (currentName.Gender.Equals("BOY"))
		{
			NextBtn.BackgroundColor = Colors.RoyalBlue;
		}
		else
		{
			NextBtn.BackgroundColor = Colors.Pink;
		}

		SemanticScreenReader.Announce(NextBtn.Text);
    }
}


