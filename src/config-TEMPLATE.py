# OpenAI API key for ChatGPT
CHATGPT_API_KEY = "###################################################################################################################################################################################################################################"

# Email configuration for sending recaps
sender_email = "#################@gmail.com"
sender_password = "################"

# List of recipient email addresses
recipient_emails = ["########@gmail.com", "########@gmail.com"]

# League Name - Will be used in the subject line of the email
LEAGUE_NAME = ""

# ESPN League Information
# Reference README for more information on how to gather this information
LEAGUE_ID = "######"

# Additional ESPN League Information required for private leagues
# Reference README for more information on how to gather this information
ESPN_COOKIES = {"swid": "#{######################################}",
    "espn_s2": "############################################################################################################################################################################################################################################################################################################################################################"}

# Header information for API requests - no need to update per league 
HEADERS = {
 'Connection': 'keep-alive',
 'Accept': 'application/json, text/plain, */*',
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

# Mapping for 'LineupSlotId' variable listed in player information from ESPN API
# Format: 'slot_id': ('category', 'position')
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

# Define the newsletter personality 
NEWSLETTER_PERSONALITY_NAME = "######"

# Provide the structure of personality traits to provide ChatGPT
NEWSLETTER_PERSONALITY_TRAITS_TEMPLATE = {
    "bio": "",
    "tone_characteristics": [
        ""
    ],
    "fantasy_football_adaptations": [

    ],
    "formatting_preferences": {
        "capitalization": "",
        "punctuation": ""
    }
}