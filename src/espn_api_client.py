import requests

from leagueInformation import league_id, espn_cookies, headers, year

class ESPNApiClient:
    def __init__(self):
        self.base_url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}'

    def _make_request(self, params):
        return requests.get(self.base_url, headers=headers, cookies=espn_cookies, params=params).json()

    # def get_boxscore_data(self):
    #     return self._make_request({"view": "mMatchup"})['schedule']

    def get_matchup_data(self):
        return self._make_request({"view": "mMatchup"})

    def get_nav_data(self):
        return self._make_request({"view": "mNav"})
    
    def get_roster_data(self):
        return self._make_request({"view": "mRoster"})
    
    def get_settings_data(self):
        return self._make_request({"view": "mSettings"})
    
    def get_top_performers_data(self):
        return self._make_request({"view": "mTopPerformers"})
    
    def get_matchup_score_data(self):
        return self._make_request({"view": "mMatchupScore"})
    
    def get_team_data(self):
        return self._make_request({"view": "mTeam"})
    
    def get_scoreboard_data(self):
        return self._make_request({"view": "mScoreboard"})
    
    def get_status_data(self):
        return self._make_request({"view": "mStatus"})
    