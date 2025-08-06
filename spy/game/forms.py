from django import forms 

class GameSetUpForm(forms.Form):
    num_players = forms.IntegerField(min_value=3, max_value=10, label="Number of Players")
    num_spies = forms.IntegerField(min_value=1, label="Number of Spies")
    game_duration = forms.IntegerField(min_value=1, label="Game Duration (minutes)")
class PlayerNamesForm(forms.Form):
    def __init__(self, num_players, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(1, num_players + 1):
            self.fields[f'player_{i}'] = forms.CharField(initial=f'Player {i}', label=f'Player {i} Name')