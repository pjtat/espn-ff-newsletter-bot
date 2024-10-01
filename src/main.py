from espn_api_client import ESPNApiClient
from json_exporter import JsonExporter
from data_extractor import create_boxscore_weekly_summary, create_team_data_summary

## TEMP 
current_week_number = 2

def main():
    api_client = ESPNApiClient()
    json_exporter = JsonExporter()

    # Fetch data
    boxscore_data = api_client.get_boxscore_data(current_week_number)

    # Create Boxscore JSON
    boxscore_weekly_summary = create_boxscore_weekly_summary(boxscore_data, current_week_number)

    # Export outgoing data 
    json_exporter.save_file('boxscore_weekly_summary.json', boxscore_weekly_summary)

    # Get team data
    team_data = api_client.get_team_data()

    # Create Team Data JSON
    team_data_summary = create_team_data_summary(team_data)

    # Export outgoing data
    json_exporter.save_file('team_data_summary.json', team_data_summary)

if __name__ == "__main__":
    main()