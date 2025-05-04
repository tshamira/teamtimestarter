import requests
import json

from datetime import datetime
from datetime import timedelta 
import pandas as pd

# team_name is the noun part of the NBA team's name; for example, if you want to find the schedule for the 
# Golden State Warriors, team_name = 'Warriors'
def team_time(team_name):
    
    # Make a GET request to the API
    response = requests.get("https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2024/league/00_full_schedule.json") 
    team_games = []
    if response.status_code == 200:
    # Parse the JSON response
        data = response.json()
    
    home_team_vs_away_teams, game_start_dates, game_start_times, game_end_dates, game_end_times, locations, game_ids  = [],[],[],[],[],[],[]
    format = '%H:%M'
    
    for nba_game in data['lscd']:
        month_games = nba_game['mscd']
            
        for game in month_games['g']:
            
            if game['v']['tn'] == team_name or game['h']['tn'] == team_name:
                # names of teams playing
                home_team = game['h']['tc'] + " " + game['h']['tn'] + " (" + game['h']['ta'] + ")"
                away_team = game['v']['tc'] + " " + game['v']['tn'] + " (" + game['v']['ta'] + ")"
                home_team_vs_away_team = away_team + " @ " + home_team
                home_team_vs_away_teams.append(home_team_vs_away_team)
                
                # game start dates + times
                game_start_date = game['gdte']
                game_start_dates.append(game_start_date)

                game_start_time_str = game['etm'][-8:-3]
                game_start_datetime = datetime.strptime(game_start_time_str, "%H:%M")
                game_start_times.append(game_start_datetime.time())
                #the .time() has to be added to the appended value bEcause the game_start_datetime variable is used
                #to calculate the game_end_datetime variable in the next chunk of code; this game_end_datetime variable requires
                #us to add timedelta (stored in game_duration variable), a process which does not work between 
                #time and timedelta objects. (datetime + timedelta OK apparently)
                
                # game end dates + times
                game_end_date = game['gdte']
                game_end_dates.append(game_end_date)
          
                game_duration = timedelta(minutes=150)
                game_end_datetime = game_start_datetime + game_duration
                game_end_time = game_end_datetime.time()
                game_end_times.append(game_end_time)
                
                # game location (city of home team)
                location = game['h']['tc']
                locations.append(location)
                
                # game id (will go in 'description' portion of google calendar)
                game_id = game['gid']
                game_ids.append(game_id)
                
            else:
                continue
            
    team_game_data = list(zip(home_team_vs_away_teams, game_start_dates, game_start_times, game_end_dates, game_end_times, locations, game_ids))
    team_sched_df = pd.DataFrame(team_game_data, columns =['away team @ home team',
                                                              'game start date',
                                                              'start time (PT)',
                                                              'game end date',
                                                              'game end time (PT)',
                                                              'location',
                                                              'game id'])
    return team_sched_df.head(10)
