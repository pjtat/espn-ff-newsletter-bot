
# ESPN League Information
# Reference README for more information on how to gather this information
LEAGUE_ID = "963482"

# Additional ESPN League Information required for private leagues
# Reference README for more information on how to gather this information
ESPN_COOKIES = {"swid": "{B6CAEBA9-F067-42E3-BA15-D9CEB1886017}",
    "espn_s2": "AEA21%2B7maZIuM%2FJfdzcExMyfjSxWkFF8uZSUAe679FOHdNgp16AuNBIc%2BKXd8xaTi8%2By4TQHG9c%2BIawbxUEArMO7mrBW%2FiBlZ%2Bf1m0AvYZbeaDAcDcOerC3awkhakRsOgkx95q2OehFE3Mhgj5E0nlMBqTqoyR%2BlwJVz40vt%2B1yb7SKHLiTPt1y%2FcPzMVtZo4Jqq24EBfFO6YWz5R3DRzerQ%2BxOOk76v72xcDzSvb9PXL4Rd4lXl6lgSoa84ENh8iG0jML1vgjr9oxK6rYb38ICH"}

# The year in which you want to pull data for
YEAR = 2024

# Header information for API requests - no need to update per league 
HEADERS = {
 'Connection': 'keep-alive',
 'Accept': 'application/json, text/plain, */*',
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

# Mapping for 'LineupSlotId' variable listed in player information from ESPN API
LINEUP_SLOT_MAPPING = {
    '20': ('bench', None),
    '21': ('ir', None),
    '0': ('starters', 'QB'),
    '2': ('starters', 'RB'),
    '4': ('starters', 'WR'),
    '6': ('starters', 'TE'),
    '23': ('starters', 'FLEX'),
    '17': ('starters', 'K'),
}