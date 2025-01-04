import requests
from datetime import datetime

# Bring in variables needed for API requests 
from config import LEAGUE_ID, ESPN_COOKIES, HEADERS, LEAGUE_YEAR

class ESPNApiClient:
    def __init__(self):
        # Figure out the current year in order to construct the base URL
        current_year = LEAGUE_YEAR

        # Construct the base URL for ESPN Fantasy Football API requests
        self.base_url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{current_year}/segments/0/leagues/{LEAGUE_ID}'

    def _make_request(self, params):
        try:
            # Send GET request to ESPN API with provided parameters
            response = requests.get(self.base_url, headers=HEADERS, cookies=ESPN_COOKIES, params=params)
            # Raise an exception for bad status codes
            response.raise_for_status()
            # Return the JSON response if successful
            return response.json()
        except requests.exceptions.RequestException as e:
            # Report error making request
            print(f"Error making request: {e}")
            return None
        except ValueError as e:
            # Report JSON parsing error
            print(f"Error parsing JSON response: {e}")
            return None

    def get_boxscore_data(self, season_week):
        # Fetch boxscore data for the provided week
        return self._make_request({"view": "mBoxscore", "scoringPeriodId": season_week})
    
    def get_team_data(self):
        # Fetch team data for the league
        return self._make_request({"view": "mTeam"})
    
    def get_league_data(self):
        # Fetch team data for the league
        return self._make_request({"view": "mNav"})
    
    def get_matchup_data(self, season_week):
        # Fetch matchup data for the provided week
        return self._make_request({"view": "mMatchupScore", "scoringPeriodId": season_week})
    
    def get_playoff_matchups(self):
        # Fetch playoff matchups for the league
        return self._make_request({"view": "mProjectedPlayoffMatchups", "matchupPeriodId": "1"})
    
    def get_league_settings(self):
        # Fetch league settings for the league
        return self._make_request({"view": "mSettings"})
    
    def get_team_standings(self):
        # Fetch team standings for the league
        return self._make_request({"view": "mStandings"})