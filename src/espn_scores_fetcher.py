import requests
import json
import os

from myconstants import league_id, espn_cookies, headers

year = 2024

url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}'

boxscore_request = requests.get(url, headers=headers, cookies=espn_cookies, params={"view": "mMatchup"})
boxscore_request_json = boxscore_request.json()
boxscore_request_json = boxscore_request_json['schedule']

leagueInfoRequest = requests.get(url, headers=headers, cookies=espn_cookies, params={"view": "mNav"})
leagueInfoRequestJson = leagueInfoRequest.json()

topPerformersRequest = requests.get(url, headers=headers, cookies=espn_cookies, params={"view": "mScoreboard"})
topPerformersRequestJson = topPerformersRequest.json()

leagueTeams = leagueInfoRequestJson['teams']
leagueOwners = leagueInfoRequestJson['members']

leagueInfo = {}

for team in leagueTeams:
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
    leagueInfo[team['id']] = team_info

for owner in leagueOwners:
    ownerInfo = {
        'ownerFirstName': owner['firstName'],
        'ownerLastName': owner['lastName'],
    }
    for team_id, team in leagueInfo.items():
        if team['ownerId'] == owner['id']:
            leagueInfo[team_id].update(ownerInfo)
            break

yearly_boxscores = []
lastWeekResults =  []

for matchup in boxscore_request_json:
    if(matchup['away']['totalPoints'] == 0 and matchup['home']['totalPoints'] == 0):
        break

    weekNumber = matchup['matchupPeriodId']
    matchupNumber = matchup['id']
    awayTeamId = matchup['away']['teamId']
    homeTeamId = matchup['home']['teamId']
    
    if matchup['winner'] == 'AWAY':
        winner = awayTeamId
        leagueInfo[awayTeamId]['wins'] += 1
        leagueInfo[homeTeamId]['losses'] += 1
    elif matchup['winner'] == 'HOME':
        winner = homeTeamId
        leagueInfo[homeTeamId]['wins'] += 1
        leagueInfo[awayTeamId]['losses'] += 1
    else:
        winner = 'tie'
        leagueInfo[awayTeamId]['ties'] += 1
        leagueInfo[homeTeamId]['ties'] += 1

    awayTeamScore = matchup['away']['totalPoints']
    leagueInfo[awayTeamId]['totalPointsFor'] += awayTeamScore
    leagueInfo[awayTeamId]['totalPointsAgainst'] += matchup['home']['totalPoints']
    homeTeamScore = matchup['home']['totalPoints']
    leagueInfo[homeTeamId]['totalPointsFor'] += homeTeamScore
    leagueInfo[homeTeamId]['totalPointsAgainst'] += awayTeamScore

    matchup_info = {
        'weekNumber': weekNumber,
        'matchupNumber': matchupNumber,
        'awayTeamId': awayTeamId,
        'awayTeamScore': awayTeamScore,
        'homeTeamId': homeTeamId,
        'homeTeamScore': homeTeamScore,
        'winner': winner,
    }

    yearly_boxscores.append(matchup_info)

    lastWeekResults.append(matchup_info)

weekNumber = lastWeekResults[0]['weekNumber']

weeklySummary = (f'In week {weekNumber} the results were:')

for result in lastWeekResults:
   matchupNumber = result['matchupNumber']
   awayTeamId = result['awayTeamId']
   homeTeamId = result['homeTeamId']
   awayTeamScore = result['awayTeamScore']
   homeTeamScore = result['homeTeamScore']
   winner = result['winner']

   homeTeamName = leagueInfo[homeTeamId]['teamName']
   homeTeamOwner = leagueInfo[homeTeamId]['ownerFirstName']
   awayTeamName = leagueInfo[awayTeamId]['teamName']
   awayTeamOwner = leagueInfo[awayTeamId]['ownerFirstName']

   weeklySummary += (f'\nIn matchup {matchupNumber}, {homeTeamName} led by {homeTeamOwner} beat {awayTeamName} led by {awayTeamOwner} with a score of {homeTeamScore} to {awayTeamScore}.')

print(weeklySummary)







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
    json.dump(leagueInfo, f, indent=4)

with open(json_file_path3, 'w') as f:
    json.dump(leagueInfoRequestJson, f, indent=4)

with open(json_file_path4, 'w') as f:
    json.dump(topPerformersRequestJson, f, indent=4)







### TEMP

# Get the directory of the current script
#script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path for the JSON file
#json_file_path = os.path.join(script_dir, 'boxscore_data.json')

# Write formatted JSON data to a file in the same directory
#with open(json_file_path, 'w') as f:
#    json.dump(boxscore_data, f, indent=4)