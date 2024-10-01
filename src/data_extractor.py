from leagueInformation import LINEUP_SLOT_MAPPING 

def create_boxscore_weekly_summary(mBoxscore_json, current_week_number):

    boxscore_weekly_summary = {
        'week_number': current_week_number,
        'weekly_boxscores': []
        }

    ### Fn to grab matchups
    matchup_boxscores = mBoxscore_json['schedule']

    matchup_id = 1

    for matchup in matchup_boxscores:

        matchup_info = {}

        # Continue if week is right
        if matchup['matchupPeriodId'] == current_week_number:
            ### DO I NEED TO DECLARE IR, AND STARTERS?
            matchup_info = {
                'matchup_id': matchup_id,
                'away': {
                    'team_id': matchup['away']['teamId'],
                    'team_score': matchup['away']['totalPoints'],
                    'starters': [],
                    'ir': [],
                    'bench': []
                },
                'home': {
                    'team_id': matchup['home']['teamId'],
                    'team_score': matchup['home']['totalPoints'],
                    'starters': [],
                    'ir': [],
                    'bench': []
                }
            }

            for team_location in ['home','away']:
                team_players = matchup[team_location]['rosterForCurrentScoringPeriod']['entries']

                for player in team_players:

                    player_stats = player['playerPoolEntry']['player']['stats']

                    for player_stat_summary in player_stats:

                        # Check for the weekly score flag (not yearly)
                        if player_stat_summary['statSplitTypeId'] == 1:

                            # Check for the actual score flag
                            if player_stat_summary['statSourceId'] == 0:
                                player_weekly_score = player_stat_summary['appliedTotal']

                            # Check for the projection flag
                            elif player_stat_summary['statSourceId'] == 1:
                                player_weekly_projection = player_stat_summary['appliedTotal']

                            else:
                                print("There was an unexpected value for 'statSplitTypeId' when checking for player scores.")

                    # Determine player position (and if they're bench)
                    lineupSlotId = str(player['lineupSlotId'])

                    ### What happens if one fails and not the other? Do both fail?
                    try:
                        depth_chart_position, player_position = LINEUP_SLOT_MAPPING[lineupSlotId]
                    except KeyError:
                        print(f"Unexpected lineupSlotId: {lineupSlotId} for player: {player['playerPoolEntry']['player']['fullName']}")
                        depth_chart_position = 'unknown'
                        player_position = 'unknown'

                    player_info = {
                        'player_id': player['playerId'],
                        'player_position': player_position,
                        'player_full_name': player['playerPoolEntry']['player']['fullName'],
                        'player_pro_team_id': player['playerPoolEntry']['player']['proTeamId'],
                        'player_score_projection': player_weekly_score,
                        'player_score_actual': player_weekly_projection
                    }

                    matchup_info[team_location][depth_chart_position].append(player_info)
            
            boxscore_weekly_summary['weekly_boxscores'].append(matchup_info)
            matchup_id += 1

    return boxscore_weekly_summary

def create_team_data_summary(mTeam_json):
    team_weekly_summary = {'teams': []}

    ### Fn to grab matchups
    list_of_teams = mTeam_json['teams']
    list_of_owners = mTeam_json['members']

    for team in list_of_teams:
        list_of_team_owners = team['owners']
        
        for team_owner in list_of_team_owners:
            for owner in list_of_owners:
                if team_owner == owner['id']:
                    owner_name = f"{owner['firstName']} {owner['lastName']}"
        
        team_info = {
            'team_id': team['id'],
            'team_abbrev': team['abbrev'],
            'team_name': team['name'],
            'team_owner': owner_name,
            'team_record': {
                'wins': team['record']['overall']['wins'],
                'losses': team['record']['overall']['losses'],
                'ties': team['record']['overall']['ties'],
                'win_percentage': team['record']['overall']['percentage'],
                'points_for': team['record']['overall']['pointsFor'],
                'points_against': team['record']['overall']['pointsAgainst'],
                'streak_type': team['record']['overall']['streakType'],
                'streak_length': team['record']['overall']['streakLength'],
                'team_current_projection_rank': team['currentProjectedRank']
            }
        }

        team_weekly_summary['teams'].append(team_info)

    return team_weekly_summary