# Import all necessary files for functions below
from espn_api_client import ESPNApiClient
from json_exporter import JsonExporter
from chatgpt_client import *
from data_extractor import *
from email_client import send_email
from config import LEAGUE_NAME

def main():
    # # Initialize API client and JSON exporter
    api_client = ESPNApiClient()
    json_exporter = JsonExporter()

    # Fetch the league data to identify the current week number
    league_data = api_client.get_league_data()

    # Process the league data to identify the recap week number
    recap_week_number = determine_recap_week_number(league_data)

    # Fetch team data from the ESPN API
    team_data = api_client.get_team_data()

    # Process team data and create summary to provide to ChatGPT
    team_data_summary = create_team_data_summary(team_data)

    # Fetch boxscore data for the current week from the ESPN API 
    boxscore_data = api_client.get_boxscore_data(recap_week_number)

    # Process boxscore data and create weekly summary to provide to ChatGPT
    boxscore_weekly_summary = create_boxscore_weekly_summary(boxscore_data, recap_week_number)

    # Add team data to the weekly boxscore summary
    add_team_data_to_weekly_summary(boxscore_weekly_summary, team_data_summary)

    # Call ChatGPT to generate a recap of the latest week's fantasy football league results
    fantasy_recap = generate_fantasy_recap(boxscore_weekly_summary)

    # Convert to HTML for sending via email 
    fantasy_recap_html = convert_fantasy_recap_to_html(fantasy_recap)

    # Send the generated recap via email
    send_email(f"{LEAGUE_NAME} - Week {recap_week_number} Recap", fantasy_recap_html)

if __name__ == "__main__":
    main()