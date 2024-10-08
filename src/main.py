# Import all necessary files for functions below
from espn_api_client import ESPNApiClient
from file_exporter import FileExporter
from chatgpt_client import *
from data_extractor import *
from email_client import send_email
from config import LEAGUE_NAME, NEWSLETTER_PERSONALITY

def main():
    # # Initialize API client and JSON exporter
    api_client = ESPNApiClient()
    file_exporter = FileExporter()

    # Fetch the league data to identify the current week number
    league_data = api_client.get_league_data()

    # Process the league data to identify the recap week number
    recap_week_number = determine_recap_week_number(league_data)

    # Fetch team data from the ESPN API
    team_data = api_client.get_team_data()

    # Process team data and create summary to provide to ChatGPT
    team_data_summary = create_team_data_summary(team_data)

    # Temp - Export for testing
    file_exporter.save_json_file("team_data_summary.json", team_data_summary)

    # Fetch boxscore data for the current week from the ESPN API 
    boxscore_data = api_client.get_boxscore_data(recap_week_number)

    # Process boxscore data and create weekly summary to provide to ChatGPT
    boxscore_weekly_summary = create_boxscore_weekly_summary(boxscore_data, recap_week_number)

    # Temp - Export for testing
    file_exporter.save_json_file("boxscore_weekly_summary.json", boxscore_weekly_summary)

    # Add team data to the weekly boxscore summary
    consolidated_weekly_summary = add_team_data_to_weekly_summary(boxscore_weekly_summary, team_data_summary)

    # Temp - Export for testing
    file_exporter.save_json_file("consolidated_weekly_summary.json", consolidated_weekly_summary)

    # Call ChatGPT to generate recaps for each individual matchup
    newsletter_text = ""

    for matchup in consolidated_weekly_summary['weekly_boxscores']:
        newsletter_text += generate_matchup_recap(matchup, newsletter_text)
        newsletter_text += "\n\n"

    # Temp - Export for testing
    file_exporter.save_txt_file("newsletter_text.txt", newsletter_text)

    # Call ChatGPT to generate an intro and closing for the newsletter
    newsletter_intro = generate_newsletter_intro(newsletter_text)
    newsletter_standings = create_standings_list(team_data_summary)
    newsletter_weekly_high_points = determine_weekly_high_points(consolidated_weekly_summary)
    newsletter_closing = generate_newsletter_closing(newsletter_text)

    # Combine the intro, recap, and closing into a single string
    newsletter_text = newsletter_intro + newsletter_text + newsletter_standings + newsletter_weekly_high_points + newsletter_closing

    # Convert to HTML for sending via email 
    fantasy_recap_html = convert_fantasy_recap_to_html(newsletter_text)

    # Send the generated recap via email
    send_email(f"{LEAGUE_NAME} - Week {recap_week_number} Recap by {NEWSLETTER_PERSONALITY['name']}", fantasy_recap_html)

if __name__ == "__main__":
    main()