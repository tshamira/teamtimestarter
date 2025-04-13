import requests
import json

from datetime import datetime
from datetime import timedelta 
import pandas as pd

# Make a GET request to the API
response = requests.get("https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2024/league/00_full_schedule.json") 
# print(response)
# Check if the request was successful

warriors_games = []
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the data
#     print(data)
    
home_team_vs_away_teams, game_start_dates, game_start_times, game_end_dates, game_end_times, locations, game_ids  = [],[],[],[],[],[],[]

format = '%H:%M:%S'

for nba_game in data['lscd']:
    month_games = nba_game['mscd']
        
    for game in month_games['g']:
        
        if game['v']['tn'] == 'Warriors' or game['h']['tn'] == 'Warriors':
            # names of teams playing
            home_team = game['h']['tc'] + " " + game['h']['tn'] + " (" + game['h']['ta'] + ")"
            away_team = game['v']['tc'] + " " + game['v']['tn'] + " (" + game['v']['ta'] + ")"
            home_team_vs_away_team = away_team + " @ " + home_team
            home_team_vs_away_teams.append(home_team_vs_away_team)
            
            # game start dates + times
            game_start_date = game['gdte']
            game_start_dates.append(game_start_date)

            game_start_time_str = game['etm'][-8:-3]
            game_start_time_dt = datetime.strptime(game_start_time_str, format).time()
            #game_start_time = datetime.strptime(game_start_time_str, format).time()
            game_start_times.append(game_start_time_dt)
                
            # game end dates + times
            game_end_date = game['gdte']
            game_end_dates.append(game_end_date)
            # avg length of nba game is 2 hours 18 minutes -> 
            # datetime.strptime(game['etm'][-8:], '%H:%M:%S')
            game_end_time = (game_start_time + timedelta(minutes=138))
            game_end_times.append(game_end_time)
            
            # game location (city of home team)
            location = game['h']['tc']
            locations.append(location)
            
            # game id (will go in 'description' portion of google calendar)
            game_id = game['gid']
            game_ids.append(game_id)
            
        else:
            continue
            
    warriors_game_data = list(zip(home_team_vs_away_teams, game_start_dates, game_start_times, game_end_dates, game_end_times, locations, game_ids))
