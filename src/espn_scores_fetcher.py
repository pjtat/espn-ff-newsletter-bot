from espn_api_client import ESPNApiClient
#from data_processor import DataProcessor
#from report_generator import ReportGenerator
from json_exporter import JsonExporter

def main():
    api_client = ESPNApiClient()
    #data_processor = DataProcessor()
    #report_generator = ReportGenerator()
    json_exporter = JsonExporter()

    # Fetch data
    matchup_data = api_client.get_matchup_data()
    nav_data = api_client.get_nav_data()
    roster_data = api_client.get_roster_data()
    settings_data = api_client.get_settings_data()
    top_performers_data = api_client.get_top_performers_data()
    matchup_score_data = api_client.get_matchup_score_data()
    team_data = api_client.get_team_data()
    scoreboard_data = api_client.get_scoreboard_data()
    status_data = api_client.get_status_data()


    # Export incoming data
    json_exporter.save_files({
        'matchup_data.json': matchup_data,
        'nav_data.json': nav_data,
        'roster_data.json': roster_data,
        'settings_data.json': settings_data,
        'top_performers_data.json': top_performers_data,
        'matchup_score_data.json': matchup_score_data,
        'team_data.json': team_data,
        'scoreboard_data.json': scoreboard_data,
        'status_data.json': status_data
    })
    
    # Process data
    # league_info = data_processor.process_league_info(league_info_data)
    # yearly_boxscores, last_week_results = data_processor.process_boxscores(boxscore_data, league_info)

    # # Generate reports
    # weekly_summary = report_generator.generate_weekly_summary(last_week_results, league_info)
    # print(weekly_summary)

    # Export outgoing data
    # json_exporter.save_files({
    #     'yearly_boxscores.json': yearly_boxscores,
    #     'league_info.json': league_info,
    #     'league_info_data.json': league_info
    # })

if __name__ == "__main__":
    main()


# league_info = {}

# for team in league_teams:
#     team_info = {
#         'teamName': team['name'],
#         'teamAbbrev': team['abbrev'],
#         'ownerId': team['owners'][0],
#         'wins': 0,
#         'losses': 0,
#         'ties': 0,
#         'totalPointsFor': 0,
#         'totalPointsAgainst': 0
#     }
#     league_info[team['id']] = team_info

# for owner in league_owners:
#     ownerInfo = {
#         'ownerFirstName': owner['firstName'],
#         'ownerLastName': owner['lastName'],
#     }
#     for team_id, team in league_info.items():
#         if team['ownerId'] == owner['id']:
#             league_info[team_id].update(ownerInfo)
#             break

# yearly_boxscores = []
# last_week_results =  []

# for matchup in boxscore_request_json:
#     if(matchup['away']['totalPoints'] == 0 and matchup['home']['totalPoints'] == 0):
#         break

#     week_number = matchup['matchupPeriodId']
#     matchup_number = matchup['id']
    
#     away_team_id = matchup['away']['teamId']
#     away_team_score = matchup['away']['totalPoints']
#     home_team_id = matchup['home']['teamId']
#     home_team_score = matchup['home']['totalPoints']

#     if matchup['winner'] == 'AWAY':
#         winner = away_team_id
#         league_info[away_team_id]['wins'] += 1
#         league_info[home_team_id]['losses'] += 1
#     elif matchup['winner'] == 'HOME':
#         winner = home_team_id
#         league_info[home_team_id]['wins'] += 1
#         league_info[away_team_id]['losses'] += 1
#     else:
#         winner = 'tie'
#         league_info[away_team_id]['ties'] += 1
#         league_info[home_team_id]['ties'] += 1

#     league_info[away_team_id]['totalPointsFor'] += away_team_score
#     league_info[away_team_id]['totalPointsAgainst'] += home_team_score
#     league_info[home_team_id]['totalPointsFor'] += home_team_score
#     league_info[home_team_id]['totalPointsAgainst'] += away_team_score

#     matchup_info = {
#         'weekNumber': week_number,
#         'matchupNumber': matchup_number,
#         'awayTeamId': away_team_id,
#         'awayTeamScore': away_team_score,
#         'homeTeamId': home_team_id,
#         'homeTeamScore': home_team_score,
#         'winner': winner,
#     }

#     yearly_boxscores.append(matchup_info)

#     last_week_results.append(matchup_info)

# week_number = last_week_results[0]['weekNumber']

# weekly_summary = (f'In week {week_number} the results were:')

# for result in last_week_results:
#    matchup_number = result['matchupNumber']
#    away_team_id = result['awayTeamId']
#    home_team_id = result['homeTeamId']
#    away_team_score = result['awayTeamScore']
#    home_team_score = result['homeTeamScore']
#    winner = result['winner']

#    home_team_name = league_info[home_team_id]['teamName']
#    home_team_owner = league_info[home_team_id]['ownerFirstName']
#    away_team_name = league_info[away_team_id]['teamName']
#    away_team_owner = league_info[away_team_id]['ownerFirstName']

#    weekly_summary += (f'\nIn matchup {matchup_number}, {home_team_name} led by {home_team_owner} beat {away_team_name} led by {away_team_owner} with a score of {home_team_score} to {away_team_score}.')

# print(weekly_summary)




# # Get the directory of the current script
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Create a 'temp files' directory
# temp_files_dir = os.path.join(script_dir, 'temp files')
# os.makedirs(temp_files_dir, exist_ok=True)

# # Create the full path for the JSON files in the 'temp files' directory
# json_file_path1 = os.path.join(temp_files_dir, 'yearly_boxscores.json')
# json_file_path2 = os.path.join(temp_files_dir, 'leagueInfoVariable.json')
# json_file_path3 = os.path.join(temp_files_dir, 'mNav.json')
# json_file_path4 = os.path.join(temp_files_dir, 'mTopPerformers.json')

# # Write formatted JSON data to a file in the same directory
# with open(json_file_path1, 'w') as f:
#     json.dump(yearly_boxscores, f, indent=4)

# with open(json_file_path2, 'w') as f:
#     json.dump(league_info, f, indent=4)

# with open(json_file_path3, 'w') as f:
#     json.dump(league_info_request_json , f, indent=4)

# with open(json_file_path4, 'w') as f:
#     json.dump(top_performers_request_json, f, indent=4)







# ### TEMP

# # Get the directory of the current script
# #script_dir = os.path.dirname(os.path.abspath(__file__))

# # Create the full path for the JSON file
# #json_file_path = os.path.join(script_dir, 'boxscore_data.json')

# # Write formatted JSON data to a file in the same directory
# #with open(json_file_path, 'w') as f:
# #    json.dump(boxscore_data, f, indent=4)