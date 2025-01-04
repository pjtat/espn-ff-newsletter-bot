# Import all necessary files for functions below
from espn_api_client import ESPNApiClient
from file_exporter import FileExporter
from chatgpt_client import *
from data_extractor import *
from email_client import send_email
from config import LEAGUE_NAME, NEWSLETTER_PERSONALITY_NAME, production_recipient_emails, test_recipient_emails

def main(scenario):
    # # Initialize API client and JSON exporter
    api_client = ESPNApiClient()
    file_exporter = FileExporter()

    # Fetch general league data from ESPN API 
    league_data = api_client.get_league_data()
    team_data = api_client.get_team_data()
    
    # Determine the recap week number
    recap_week_number = determine_recap_week_number(league_data)

    # Fetch the matchup and boxscore data for the recap week from ESPN API
    matchup_data = api_client.get_matchup_data(recap_week_number)
    boxscore_data = api_client.get_boxscore_data(recap_week_number)

    # Export all responses to JSON files for testing
    file_exporter.save_json_file("mNav_API_response.json", league_data)
    file_exporter.save_json_file("mTeam_API_response.json", team_data)
    file_exporter.save_json_file("mMatchupScore_API_response.json", matchup_data)
    file_exporter.save_json_file("mBoxscore_API_response.json", boxscore_data)
    
    # Determine if regular season or playoffs
    is_regular_season = determine_if_regular_season(recap_week_number, matchup_data)

    # Process team and boxscore data to create summaries to provide to ChatGPT 
    team_data_summary = create_team_data_summary(team_data)
    boxscore_weekly_summary = create_boxscore_weekly_summary(boxscore_data, recap_week_number)

    # Conslidate summaries
    consolidated_weekly_summary = add_team_data_to_weekly_summary(boxscore_weekly_summary, team_data_summary)

    # Export the consolidated weekly summary to JSON for testing
    file_exporter.save_json_file("consolidated_weekly_summary.json", consolidated_weekly_summary)

    # Initialize newsletter text
    newsletter_text = ""

    # Call ChatGPT to generate the traits/bio of the newsletter personality
    newsletter_personality_traits = generate_newsletter_personality_traits(NEWSLETTER_PERSONALITY_NAME)

    # Determine if the season is over
    is_end_of_season = determine_if_end_of_season(league_data)

    # Call ChatGPT to generate recaps for each individual matchup
    for matchup in consolidated_weekly_summary['weekly_boxscores']:
        newsletter_text += generate_matchup_recap(matchup, newsletter_text, newsletter_personality_traits)
        newsletter_text += "\n\n"

    if is_end_of_season:
        intro_special_instructions = "This is the final week of the season."
    else:
        intro_special_instructions = ""

    # Call ChatGPT to generate an intro and closing for the newsletter
    newsletter_intro = generate_newsletter_intro(newsletter_text, newsletter_personality_traits, intro_special_instructions)
    newsletter_standings = create_standings_list(team_data_summary)
    newsletter_weekly_high_points = determine_weekly_high_points(consolidated_weekly_summary)

    if is_end_of_season:
        # medal_winners = get_medal_winners(team_data_summary)
        # newsletter_end_of_season_summary = generate_end_of_season_summary(medal_winners)
        closing_special_instructions = f"This is the end of the season. These are the final standings: {newsletter_standings}. Call out the first place winner, the runner up, the third place finisher, and the last place finisher. Provide a close to the season."
    else:
        closing_special_instructions = ""

    # Call ChatGPT to generate a closing for the newsletter
    newsletter_closing = generate_newsletter_closing(newsletter_text, newsletter_personality_traits, closing_special_instructions)

    # Assemble newsletter text
    newsletter_text = newsletter_intro + newsletter_text + newsletter_standings + newsletter_weekly_high_points + newsletter_closing

    # Convert to HTML for sending via email 
    fantasy_recap_html = convert_fantasy_recap_to_html(newsletter_text)

    # Determine if the test or production email should be sent
    if scenario == "test":
        send_email(f"TEST - {LEAGUE_NAME} - Week {recap_week_number} Recap Provided by {NEWSLETTER_PERSONALITY_NAME}", fantasy_recap_html, test_recipient_emails)
    else:
        send_email(f"{LEAGUE_NAME} - Week {recap_week_number} Recap Provided by {NEWSLETTER_PERSONALITY_NAME}", fantasy_recap_html, production_recipient_emails)

if __name__ == "__main__":
    while True:
        choice = input("Would you like to send a (T)est email or (P)roduction email? [T/P]: ").strip().upper()
        if choice == 'T':
            print("Sending test email...")
            scenario = "test"
            main(scenario)
            break
        elif choice == 'P':
            print("Sending production email...")
            scenario = "production"
            main(scenario)
            break
        print("Invalid input. Please enter 'T' for test or 'P' for production.")