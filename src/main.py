# Import all necessary files for functions below
from espn_api_client import ESPNApiClient
from json_exporter import JsonExporter
from chatgpt_client import generate_fantasy_recap, convert_fantasy_recap_to_html
from data_extractor import create_boxscore_weekly_summary, create_team_data_summary, pull_week_number
from email_client import send_email

def main():
    # # Initialize API client and JSON exporter
    api_client = ESPNApiClient()
    json_exporter = JsonExporter()

    # Fetch the league data to identify the current week number
    league_data = api_client.get_league_data()

    # Process the league data to identify the recap week number
    recap_week_number = pull_week_number(league_data)

    # Fetch boxscore data for the current week from the ESPN API 
    boxscore_data = api_client.get_boxscore_data(recap_week_number)

    # Process boxscore data and create weekly summary to provide to ChatGPT
    boxscore_weekly_summary = create_boxscore_weekly_summary(boxscore_data, recap_week_number)
    
    # Export boxscore weekly summary to JSON file for reference
    json_exporter.save_file('boxscore_weekly_summary.json', boxscore_weekly_summary)

    # Fetch team data from the ESPN API
    team_data = api_client.get_team_data()

    # Process team data and create summary to provide to ChatGPT
    team_data_summary = create_team_data_summary(team_data)

    # Export team data summary to JSON file for reference
    json_exporter.save_file('team_data_summary.json', team_data_summary)

    # Call ChatGPT to generate a recap of the latest week's fantasy football league results
    fantasy_recap = generate_fantasy_recap(team_data_summary, boxscore_weekly_summary)

    # Export the generated recap to a JSON file for reference
    json_exporter.save_file('fantasy_recap.json', fantasy_recap)

    # Convert to HTML for sending via email 
    fantasy_recap_html = convert_fantasy_recap_to_html(fantasy_recap)

    # Send the generated recap via email
    send_email("Next Year's 8 Man League - Week " + str(recap_week_number) + " Recap", fantasy_recap_html)

if __name__ == "__main__":
    main()