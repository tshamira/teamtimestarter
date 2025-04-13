import requests
import json

from datetime import datetime
from datetime import timedelta 
import pandas as pd

# Make a GET request to the API
response = requests.get("https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2024/league/00_full_schedule.json") 
# print(response)
# Check if the request was successful

team_games = []
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the data
#     print(data)
    
home_team_vs_away_teams, game_start_dates, game_start_times, game_end_dates, game_end_times, locations, game_ids  = [],[],[],[],[],[],[]


#timezone = "PST"

def timezone_adjustment(timezone):
    # timezone is a string of three or four character denoting the timezone that the user is using the app in.
    # something tricky about timezones is that they can change depending on the time of year (due to daylight savings time).. will try to account for this
    format = '%H:%M:%S'
    game_start_time_ET = datetime.strptime(game['etm'][-8:], '%H:%M:%S')

    # USA
    if timezone == "EST":
        # UTC -05
        game_start_times.append(game_start_time)
    elif timezone == "CST":
        game_start_time = (game_start_time_ET - datetime.strptime("01:00:00", format))
        game_start_times.append(game_start_time)
    elif timezone == "MST":
        game_start_time = (game_start_time_ET - datetime.strptime("02:00:00", format))
        game_start_times.append(game_start_time)
    elif timezone == "PST":
        game_start_time = (game_start_time_ET - datetime.strptime("03:00:00", format))
        game_start_times.append(game_start_time)
    elif timezone == "AKST":
        game_start_time = (game_start_time_ET - datetime.strptime("04:00:00", format))
        game_start_times.append(game_start_time)
    elif timezone == "HST":
        game_start_time = (game_start_time_ET - datetime.strptime("05:00:00", format))
        game_start_times.append(game_start_time)
    else:
        print("Incorrect/missing timezone.")
        break
    


    
def team_time(team_name):
    format = '%H:%M'
    game_start_time_ET = datetime.strptime(game['etm'][-8:], '%H:%M:%S')
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
                start_datetime = datetime.strptime(game_start_time_str, "%H:%M")
                game_start_times.append(game_start_time_dt)
                    
                # game end dates + times
                game_end_date = game['gdte']
                game_end_dates.append(game_end_date)
                
                game_duration = timedelta(minutes=150)
                end_datetime = start_datetime + game_duration
                game_end_time = end_datetime.time()
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
