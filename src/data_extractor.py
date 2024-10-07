# Import the lineup slot mapping to translate the player positions
from config import LINEUP_SLOT_MAPPING 

def create_boxscore_weekly_summary(mBoxscore_json, current_week_number):
    """
    Create a summary of weekly boxscores from the provided JSON data.

    Args:
    mBoxscore_json (dict): JSON data containing boxscore information
    current_week_number (int): The week number for which to create the summary

    Returns:
    dict: A summary of weekly boxscores
    """
    boxscore_weekly_summary = {
        'week_number': current_week_number,
        'weekly_boxscores': []
        }

    # Get matchups from the JSON data
    matchup_boxscores = mBoxscore_json['schedule']

    matchup_id = 1

    for matchup in matchup_boxscores:
        matchup_info = {}

        # Process only matchups for the current week
        if matchup['matchupPeriodId'] == current_week_number:
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
                    player_weekly_score = 0
                    player_weekly_projection = 0

                    for player_stat_summary in player_stats:
                        # Check for weekly score (not yearly)
                        if player_stat_summary['statSplitTypeId'] == 1:
                            # Check for actual score
                            if player_stat_summary['statSourceId'] == 0:
                                player_weekly_score = player_stat_summary['appliedTotal']
                            # Check for projected score
                            elif player_stat_summary['statSourceId'] == 1:
                                player_weekly_projection = player_stat_summary['appliedTotal']
                            else:
                                print("Unexpected value for 'statSplitTypeId' when checking player scores.")

                    # Determine player position and depth chart position
                    lineupSlotId = str(player['lineupSlotId'])

                    try:
                        # Attempt to map the lineupSlotId to depth chart position and player position
                        depth_chart_position, player_position = LINEUP_SLOT_MAPPING[lineupSlotId]
                    except KeyError:
                        # If the lineupSlotId is not found in the mapping, log the error and set default values
                        print(f"Unexpected lineupSlotId: {lineupSlotId} for player: {player['playerPoolEntry']['player']['fullName']}")
                        depth_chart_position = 'unknown'
                        player_position = 'unknown'

                    player_info = {
                        'player_id': player['playerId'],
                        'player_position': player_position,
                        'player_full_name': player['playerPoolEntry']['player']['fullName'],
                        'player_pro_team_id': player['playerPoolEntry']['player']['proTeamId'],
                        'player_score_projection': round(player_weekly_projection, 1),
                        'player_score_actual': round(player_weekly_score, 1)
                    }

                    # Add the info for this player to the team summary
                    matchup_info[team_location][depth_chart_position].append(player_info)
            
            # Add the info for this week of boxscores to the overall summary
            boxscore_weekly_summary['weekly_boxscores'].append(matchup_info)

            matchup_id += 1

    return boxscore_weekly_summary

def create_team_data_summary(mTeam_json):
    """
    Create a summary of team data from the provided JSON data.

    Args:
    mTeam_json (dict): JSON data containing team information

    Returns:
    dict: A summary of team data
    """
    team_weekly_summary = {'teams': []}

    # Get list of teams and owners from the JSON data
    list_of_teams = mTeam_json['teams']
    list_of_owners = mTeam_json['members']

    for team in list_of_teams:
        list_of_team_owners = team['owners']
        
        # Find the owner name for the current team
        for team_owner in list_of_team_owners:
            for owner in list_of_owners:
                if team_owner == owner['id']:
                    owner_name = f"{owner['firstName']} {owner['lastName']}"
        
        team_info = {
            'team_id': team['id'],
            'team_abbrev': team['abbrev'],
            'team_name': team['name'],
            'team_owner': owner_name,
            'team_rank': team['playoffSeed'],
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

        # Add the info for this team to the overall summary
        team_weekly_summary['teams'].append(team_info)

    return team_weekly_summary

def determine_recap_week_number(league_data):
    # Pull the current week number from the league data
    current_week_number = league_data['status']['currentMatchupPeriod']
    
    # Subtract 1 from the current week number to get the previous week's recap
    previous_week_number = current_week_number - 1

    return previous_week_number

def add_team_data_to_weekly_summary(boxscore_weekly_summary, team_weekly_summary):
    """
    Add team data to the weekly boxscore summary.

    Args:
    boxscore_weekly_summary (dict): The weekly boxscore summary to add to
    team_weekly_summary (dict): The team data to add
    """
    for matchup in boxscore_weekly_summary['weekly_boxscores']:
        for team_location in ['home', 'away']:
            team_id = matchup[team_location]['team_id']
            for team in team_weekly_summary['teams']:
                if team['team_id'] == team_id:
                    matchup[team_location]['team_info'] = team