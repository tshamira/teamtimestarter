# teamtimestarter
starter code for team time (name of site/app still undecided)

okay so basically, i got tired of having to check when the (NBA) warriors games are, so i wanted to find a way to automatically upload those games to my google calendar

things i was able to do in jupyter notebook:
- call the nba api to get a list of all games in the 2024-25 season (including preseason, not including postseason because those matchups are not determined yet)
- parse through the .json file from the api call and filter for warriors games (home and away)
- retrieve all relevant data for warriors games - i.e. game date, game start time, opponent, location
- turn this data (which was in a list) into a pandas dataframe, and then into a .csv file

from here, i opened the .csv file of the warriors' schedule using google sheets. in google sheets, i reformatted the header row to fit the parameters of google calendar and was then able to download the google sheet as a .ics file, which i imported to my google calendar. 

--

i was able to do this on a small scale (i.e. import events to my own calendar), but i want to make it so that other people can upload their events to their own calendars. that is, i want other people to be able to select their own team(s) whose schedules they care about and have those specific games uploaded to their personal calendars (google calendar, apple calendar, outlook, notion are the main ones I can think of rn).

what will this look like? a website? an app? i honestly need to explore some options first, but updates to come..
