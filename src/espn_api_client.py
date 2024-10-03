import requests

# Bring in variables needed for API requests 
from espn_league_input import LEAGUE_ID, ESPN_COOKIES, HEADERS, YEAR

class ESPNApiClient:
    def __init__(self):
        # Construct the base URL for ESPN Fantasy Football API requests
        self.base_url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{YEAR}/segments/0/leagues/{LEAGUE_ID}'

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