import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_nfl_team_schedule(teamid: str=None, season: str='2022', teamabv: str='CHI', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This call returns the schedule of any team, using the teamID that can be found in "getNFLTeams" call.
		
		Call needs to look like this:
		/getNFLTeamSchedule?teamID=1
		You can also use the team Abbreviation:
		/getNFLTeamSchedule?teamAbv=CHI   
		
		That will return a list of the team's games in the body. 
		
		To get a list of appropriate team abbreviations, use the getNFLTeams call.
		
		You can also add the "season" parameter if you want to specify season.  Good for seasons 2022 and 2023."
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"
    querystring = {}
    if teamid:
        querystring['teamID'] = teamid
    if season:
        querystring['season'] = season
    if teamabv:
        querystring['teamAbv'] = teamabv
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_nfl_games_and_stats_for_a_single_player(playerid: str='4362887', gameid: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This call will grab a map of all of the games a player has played this season.   
		playerID is a required parameter.
		You can also use gameID if you want to only pull back a specific game. 
		
		Example:
		Correct way to get the stats for Justin Fields for his game against Detroit on 11/13/2022 would be this:
		/getNFLGamesForPlayer?playerID=4362887&gameID=20221113_DET@CHI
		
		But if you wanted to get all of his games this season, you'd make this call
		/getNFLGamesForPlayer?playerID=4362887
		
		This call will not work without playerID.  If you want stats for all players during a game, then use the getNFLBoxScore call with that specific gameID.
		
		You can choose which season you pull games from with parameter: season .   
		NFL Season that runs from 2022-2023 is season 2022.  And so on.
		If you call without season parameter then it will pull back current season's games.
		
		You can limit the amount of games returned with parameter: numberOfGames.   For example: &numberOfGames=5 will return the last 5 games this player has an entry for."
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLGamesForPlayer"
    querystring = {}
    if playerid:
        querystring['playerID'] = playerid
    if gameid:
        querystring['gameID'] = gameid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_nfl_team_roster(archivedate: str=None, teamabv: str='CHI', teamid: str='6', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This call returns the current or historical* roster of any team, using the teamID that can be found in "getNFLTeams" call.
		
		Rosters are updated a few times throughout the day.  Usually every hour.  
		 
		Historical rosters are saved on a daily basis as of 20230505 and moving forward. 
		
		Call needs to look like this:
		/getNFLTeamRoster?teamID=6
		or
		/getNFLTeamRoster?teamAbv=CHI
		
		That will return a list of the team's current roster players in the body.
		
		Add parameter archiveDate to the call to get a list of roster players (playerID's only) for that specific date.  Historical roster dates only are kept as far back as 20230505."
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamRoster"
    querystring = {}
    if archivedate:
        querystring['archiveDate'] = archivedate
    if teamabv:
        querystring['teamAbv'] = teamabv
    if teamid:
        querystring['teamID'] = teamid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_nfl_teams(schedules: str='true', rosters: str='true', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This call will retrieve the list of NFL teams. Included is their name, city, abbreviation, and teamID which can be used in other calls.  Their current record and current W/L streak is included as well. Optional data that can be included are the team rosters and their schedules.      
		
		Included in team rosters is all players injuries. 
		/getNFLTeams
		
		Optional parameters are ?schedules=true    or    ?rosters=true"
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeams"
    querystring = {}
    if schedules:
        querystring['schedules'] = schedules
    if rosters:
        querystring['rosters'] = rosters
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_nfl_betting_odds(gamedate: str='20230101', gameid: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This grabs NFL betting/gambling lines and odds from some of the most popular online sportsbooks (fanduel, betrivers, betmgm, caesars, pointsbet, etc). 
		
		You can call this for specific game or a specific date.  Check out the example responses here for the type of data you can expect back.   Some of the sportsbooks do not offer live betting, so data from those sportsbooks will not be returned after the game starts.  
		
		Either gameDate or gameID is required.
		Examples of what the calls can look like:
		/getNFLBettingOdds?gameDate=20230101
		/getNFLBettingOdds?gameID=20230101_CHI@DET"
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLBettingOdds"
    querystring = {}
    if gamedate:
        querystring['gameDate'] = gamedate
    if gameid:
        querystring['gameID'] = gameid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_player_information(playerid: str=None, playername: str='justin_fi', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Call this to get general information on each player (name, team, experience, birthday, college, etc).
		
		You can call with their playerID, if you know it.  playerID calls will always be quicker as it acts on the key of the table.  
		
		You can also call with playerName.  This call will return a list of players who have that name.  If you want to include spaces in the search name, then use underscore.  So if you want to find Justin Fields, you can use "Justin_fields" and it will bring him back.  Or try with playerName=justin and it will return a list of guys with justin in their name.
		
		/getNFLPlayerInfo?playerID=4374033
		
		/getNFLPlayerInfo?playerName=justin_fields
		
		etc"
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLPlayerInfo"
    querystring = {}
    if playerid:
        querystring['playerID'] = playerid
    if playername:
        querystring['playerName'] = playername
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_player_list(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Grabs all of this season's players and their IDs.  
		
		ONE CALL is all you need to retrieve every player.  No need to call multiple times to get the full list.
		
		Rosters are updated multiple times per day during the season.
		
		You mainly will use this to match a player with his playerID.
		
		There are no parameters, just a simple call..
		
		/getNFLPlayerList"
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLPlayerList"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_daily_nfl_schedule(gamedate: str='20221211', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get basic information on which games are being played during a day.  
		call is like this:
		/getNFLGamesForDate?gameDate=20221211
		The above call will return all of the games from December 11th, 2022.  Date must be in that format.  
		They come back in a list format within the body of the response."
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLGamesForDate"
    querystring = {}
    if gamedate:
        querystring['gameDate'] = gamedate
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_general_game_information(gameid: str='20221212_NE@ARI', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This call pulls back the most general information for a game: away team, home team, game date, and game start time.  All times are in Eastern (ET) time zone.  
		gameID is needed.  You can retrieve gameID from a few different calls.  The "getNFLGamesForDate" call or the "getNFLTeamSchedule" call will be the best ways to get the gameID's.   
		
		Call should look like this: 
		/getNFLGameInfo?gameID=20221212_NE@ARI"
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLGameInfo"
    querystring = {}
    if gameid:
        querystring['gameID'] = gameid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_nfl_game_box_score_live_real_time(gameid: str='20221212_NE@ARI', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves the entire box score for a game either in progress or already completed for the current season.  The stats retrieved here are what are normally shown in box scores or used in fantasy games.  If there are any stats here that you'd like to see, please message me.  
		
		The call looks like this /getNFLBoxScore?gameID=20221212_NE@ARI
		
		The call needs to be exactly in the same format as above.  8 digit date, underscore, then the away team abbreviation, @, then home team abbreviation.  Complete list of team abbreviations can be retrieved with the getNFLTeams call or various other calls.  
		
		But, the best way to find specific game ID's are either from the "getNFLGamesForDate" call, or the "getNFLTeamSchedule" call."
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLBoxScore"
    querystring = {}
    if gameid:
        querystring['gameID'] = gameid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_daily_scoreboard_live_real_time(gameid: str=None, gamedate: str='20221211', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This call will pull game scores and no other stats.  
		/getNFLScoresOnly
		Call it with no parameters, it will return the current date's game list with their scores.  
		
		You can use both gameID and gameDate for parameters.  gameID will give you only the scores for one specific game.  gameDate will give you the scores for every game on that date.  
		
		Example, to get all games for December 11, 2022
		/getNFLScoresOnly?gameDate=20221211
		or you can use this call to get just one specific game 
		/getNFLScoresOnly?gameID=20221211_NYJ@BUF
		or call with no parameters for the games for 'current processing day'."
    
    """
    url = f"https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLScoresOnly"
    querystring = {}
    if gameid:
        querystring['gameID'] = gameid
    if gamedate:
        querystring['gameDate'] = gamedate
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

