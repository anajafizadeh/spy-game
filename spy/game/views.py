from django.shortcuts import render, redirect
from .forms import GameSetUpForm, PlayerNamesForm
import random

LOCATIONS = [
    "Airport", "Restaurant", "Hospital", "Movie Theater", "Train Station", "Beach", "School"
]

def setup_view(request):
    request.session.flush()
    if request.method == "POST":
        form = GameSetUpForm(request.POST)
        if form.is_valid():
            num_players = form.cleaned_data['num_players']
            num_spies = form.cleaned_data['num_spies']
            request.session['num_players'] = num_players
            request.session['num_spies'] = num_spies
            request.session['game_duration'] = form.cleaned_data['game_duration']
            return redirect('game:names')
    else:
        form = GameSetUpForm()
    args = {"form": form}
    return render(request, 'game/setup.html', args)

def names_view(request):
    num_players = request.session.get('num_players')
    if not num_players:
        return redirect('game:setup')
    if request.method == "POST":
        form = PlayerNamesForm(num_players, request.POST)
        if form.is_valid():
            player_names = []
            for i in range(1, num_players + 1):
                player_names = [form.cleaned_data[f'player_{i}'] for i in range(1, num_players + 1)]
                request.session['player_names'] = player_names
                request.session['num_players'] = num_players
                request.session['num_spies'] = request.session.get('num_spies')
                request.session['location'] = random.choice(LOCATIONS)
                return redirect('game:role_reveal')
    else:
        form = PlayerNamesForm(num_players)
    args = {'form':form}
    return render(request, 'game/enter_names.html', args)
    

def role_reveal_view(request):
    player_names = request.session.get('player_names')
    num_players = request.session.get('num_players')
    num_spies = request.session.get('num_spies')
    location = request.session.get('location')
    roles = request.session.get('roles')
    current_index = request.session.get('current_index', 0)
    role_revealed = request.session.get('role_revealed', False)
    
    if not roles:
        spy_indices = random.sample(range(num_players), num_spies)
        roles = []
        print(player_names)
        for i, name in enumerate(player_names):
            # print(name)
            if i in spy_indices:
                roles.append({'name': name, 'role': 'spy'})
            else:
                roles.append({'name': name, 'role': location})
        request.session['roles'] = roles
    
    if current_index >= num_players:
        request.session['current_index'] = 0
        return redirect('game:timer')
    
    # Handle POST
    if request.method == 'POST':
        if 'reveal' in request.POST:
            request.session['role_revealed'] = True
        elif 'next' in request.POST:
            request.session['current_index'] = current_index + 1
            request.session['role_revealed'] = False
            return redirect('game:role_reveal')  # Reload for next player

    # Get current player data
    player = roles[current_index]
    show_role = request.session.get('role_revealed', False)

    return render(request, 'game/role_reveal.html', {
        'player': player,
        'show_role': show_role,
    })

def timer_view(request):
    duration = request.session.get('game_duration')
    request.session['current_index'] = 0
    if not duration:
        return redirect('game:setup')
    args = {'duration': duration}
    return render(request, 'game/timer.html', args)

def game_over_view(request):
    roles = request.session.get('roles', [])
    spies = [player['name'] for player in roles if player['role'] == 'spy']

    request.session.flush()
    return render(request, 'game/game_over.html', {'spies': spies})

def restart_game_view(request):
    request.session.flush()
    return redirect('game:setup')

