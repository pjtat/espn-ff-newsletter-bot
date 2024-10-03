# Import all necessary files for functions below
from espn_api_client import ESPNApiClient
from json_exporter import JsonExporter
from chatgpt_client import generate_fantasy_recap
from data_extractor import create_boxscore_weekly_summary, create_team_data_summary

# Temporary - Need to find a way to automate
# Provide the week number value to determine which week to pull data for
current_week_number = 4

def main():
    # Initialize API client and JSON exporter
    api_client = ESPNApiClient()
    json_exporter = JsonExporter()

    # Fetch boxscore data for the current week from the ESPN API 
    boxscore_data = api_client.get_boxscore_data(current_week_number)

    # Process boxscore data and create weekly summary to provide to ChatGPT
    boxscore_weekly_summary = create_boxscore_weekly_summary(boxscore_data, current_week_number)

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

    # Print the generated recap
    print(fantasy_recap)

if __name__ == "__main__":
    main()