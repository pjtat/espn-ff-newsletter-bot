import requests
import json
import os

from myconstants import league_id, espn_cookies, headers, listOfOwners

year = 2024

url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}'

boxscore_request = requests.get(url, headers=headers, cookies=espn_cookies, params={"view": "mMatchup"})
boxscore_request_json = boxscore_request.json()
boxscore_request_json = boxscore_request_json['schedule']

max_team_id = max(max(listOfOwners), max(m['away']['teamId'] for m in boxscore_request_json), max(m['home']['teamId'] for m in boxscore_request_json))

yearly_boxscores = []
teamRecords = [{
    'wins': 0,
    'losses': 0,
    'ties': 0,
    'totalPoints': 0
} for _ in range(max_team_id + 1)]

for matchup in boxscore_request_json:
    weekNumber = matchup['matchupPeriodId']
    matchupNumber = matchup['id']
    awayTeamId = matchup['away']['teamId']
    homeTeamId = matchup['home']['teamId']
    
    if matchup['winner'] == 'AWAY':
        winner = awayTeamId
        teamRecords[awayTeamId]['wins'] += 1
        teamRecords[homeTeamId]['losses'] += 1
    elif matchup['winner'] == 'HOME':
        winner = homeTeamId
        teamRecords[homeTeamId]['wins'] += 1
        teamRecords[awayTeamId]['losses'] += 1
    else:
        winner = 'tie'
        teamRecords[awayTeamId]['ties'] += 1
        teamRecords[homeTeamId]['ties'] += 1

    awayTeamScore = matchup['away']['totalPoints']
    teamRecords[awayTeamId]['totalPoints'] += awayTeamScore
    homeTeamScore = matchup['home']['totalPoints']
    teamRecords[homeTeamId]['totalPoints'] += homeTeamScore

    matchup = {
        'weekNumber': weekNumber,
        'matchupNumber': matchupNumber,
        'awayTeamId': awayTeamId,
        'awayTeamScore': awayTeamScore,
        'homeTeamId': homeTeamId,
        'homeTeamScore': homeTeamScore,
        'winner': winner,
    }

    yearly_boxscores.append(matchup)

    

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path for the JSON file
json_file_path1 = os.path.join(script_dir, 'yearly_boxscores.json')
json_file_path2 = os.path.join(script_dir, 'team_records.json')

# Write formatted JSON data to a file in the same directory
with open(json_file_path1, 'w') as f:
    json.dump(yearly_boxscores, f, indent=4)

with open(json_file_path2, 'w') as f:
    json.dump(teamRecords, f, indent=4)





### TEMP

# Get the directory of the current script
#script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path for the JSON file
#json_file_path = os.path.join(script_dir, 'boxscore_data.json')

# Write formatted JSON data to a file in the same directory
#with open(json_file_path, 'w') as f:
#    json.dump(boxscore_data, f, indent=4)