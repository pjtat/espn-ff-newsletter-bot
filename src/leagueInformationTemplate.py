
# ESPN League Information
# Reference README for more information on how to gather this information
LEAGUE_ID = "######"

# Additional ESPN League Information required for private leagues
# Reference README for more information on how to gather this information
ESPN_COOKIES = {"swid": "{########-####-####-####-############}",
    "espn_s2": "############################################################################################################################################################################################################################################################################################"}

# The year in which you want to pull data for
YEAR = ####

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