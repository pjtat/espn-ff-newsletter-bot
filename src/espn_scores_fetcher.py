import requests
import json
import os

from leagueInformation import league_id, espn_cookies, headers

year = 2024

url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}'

boxscore_request = requests.get(url, headers=headers, cookies=espn_cookies, params={"view": "mMatchup"})
boxscore_request_json = boxscore_request.json()
boxscore_request_json = boxscore_request_json['schedule']

league_info_request = requests.get(url, headers=headers, cookies=espn_cookies, params={"view": "mNav"})
league_info_request_json = league_info_request.json()

top_performers_request = requests.get(url, headers=headers, cookies=espn_cookies, params={"view": "mScoreboard"})
top_performers_request_json = top_performers_request.json()

league_teams = league_info_request_json ['teams']
league_owners = league_info_request_json ['members']

league_info = {}

for team in league_teams:
    team_info = {
        'teamName': team['name'],
        'teamAbbrev': team['abbrev'],
        'ownerId': team['owners'][0],
        'wins': 0,
        'losses': 0,
        'ties': 0,
        'totalPointsFor': 0,
        'totalPointsAgainst': 0
    }
    league_info[team['id']] = team_info

for owner in league_owners:
    ownerInfo = {
        'ownerFirstName': owner['firstName'],
        'ownerLastName': owner['lastName'],
    }
    for team_id, team in league_info.items():
        if team['ownerId'] == owner['id']:
            league_info[team_id].update(ownerInfo)
            break

yearly_boxscores = []
last_week_results =  []

for matchup in boxscore_request_json:
    if(matchup['away']['totalPoints'] == 0 and matchup['home']['totalPoints'] == 0):
        break

    week_number = matchup['matchupPeriodId']
    matchup_number = matchup['id']
    away_team_id = matchup['away']['teamId']
    home_team_id = matchup['home']['teamId']
    
    if matchup['winner'] == 'AWAY':
        winner = away_team_id
        league_info[away_team_id]['wins'] += 1
        league_info[home_team_id]['losses'] += 1
    elif matchup['winner'] == 'HOME':
        winner = home_team_id
        league_info[home_team_id]['wins'] += 1
        league_info[away_team_id]['losses'] += 1
    else:
        winner = 'tie'
        league_info[away_team_id]['ties'] += 1
        league_info[home_team_id]['ties'] += 1

    away_team_score = matchup['away']['totalPoints']
    league_info[away_team_id]['totalPointsFor'] += away_team_score
    league_info[away_team_id]['totalPointsAgainst'] += home_team_score
    home_team_score = matchup['home']['totalPoints']
    league_info[home_team_id]['totalPointsFor'] += home_team_score
    league_info[home_team_id]['totalPointsAgainst'] += away_team_score

    matchup_info = {
        'weekNumber': week_number,
        'matchupNumber': matchup_number,
        'awayTeamId': away_team_id,
        'awayTeamScore': away_team_score,
        'homeTeamId': home_team_id,
        'homeTeamScore': home_team_score,
        'winner': winner,
    }

    yearly_boxscores.append(matchup_info)

    last_week_results.append(matchup_info)

week_number = last_week_results[0]['weekNumber']

weekly_summary = (f'In week {week_number} the results were:')

for result in last_week_results:
   matchup_number = result['matchupNumber']
   away_team_id = result['awayTeamId']
   home_team_id = result['homeTeamId']
   away_team_score = result['awayTeamScore']
   home_team_score = result['homeTeamScore']
   winner = result['winner']

   home_team_name = league_info[home_team_id]['teamName']
   home_team_owner = league_info[home_team_id]['ownerFirstName']
   away_team_name = league_info[away_team_id]['teamName']
   away_team_owner = league_info[away_team_id]['ownerFirstName']

   weekly_summary += (f'\nIn matchup {matchup_number}, {home_team_name} led by {home_team_owner} beat {away_team_name} led by {away_team_owner} with a score of {home_team_score} to {away_team_score}.')

print(weekly_summary)




# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path for the JSON file
json_file_path1 = os.path.join(script_dir, 'yearly_boxscores.json')
json_file_path2 = os.path.join(script_dir, 'leagueInfoVariable.json')
json_file_path3 = os.path.join(script_dir, 'mNav.json')
json_file_path4 = os.path.join(script_dir, 'mTopPerformers.json')

# Write formatted JSON data to a file in the same directory
with open(json_file_path1, 'w') as f:
    json.dump(yearly_boxscores, f, indent=4)

with open(json_file_path2, 'w') as f:
    json.dump(league_info, f, indent=4)

with open(json_file_path3, 'w') as f:
    json.dump(league_info_request_json , f, indent=4)

with open(json_file_path4, 'w') as f:
    json.dump(top_performers_request_json, f, indent=4)







### TEMP

# Get the directory of the current script
#script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path for the JSON file
#json_file_path = os.path.join(script_dir, 'boxscore_data.json')

# Write formatted JSON data to a file in the same directory
#with open(json_file_path, 'w') as f:
#    json.dump(boxscore_data, f, indent=4)