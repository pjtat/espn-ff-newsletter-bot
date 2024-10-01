import requests

from leagueInformation import LEAGUE_ID, ESPN_COOKIES, HEADERS, YEAR

class ESPNApiClient:
    def __init__(self):
        self.base_url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{YEAR}/segments/0/leagues/{LEAGUE_ID}'

    def _make_request(self, params):
        try:
            response = requests.get(self.base_url, headers=HEADERS, cookies=ESPN_COOKIES, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None
        except ValueError as e:
            print(f"Error parsing JSON response: {e}")
            return None

    def get_boxscore_data(self, season_week):
        return self._make_request({"view": "mBoxscore", "scoringPeriodId": season_week})
    
    def get_team_data(self):
        return self._make_request({"view": "mTeam"})