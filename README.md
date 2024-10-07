# Fantasy Football League Recap Generator

This project automates the process of generating and sending weekly recaps for an ESPN fantasy football league using OpenAI's GPT model.

## Features

- Fetches league data, boxscores, and team information from the ESPN API
- Processes and summarizes the fetched data
- Generates a detailed fantasy football recap using OpenAI's GPT model
- Converts the generated recap to HTML format
- Sends the recap via email to league participants

## Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
- ESPN API access
- OpenAI API key
- SMTP server access for sending emails

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/pjtat/espn-ff-newsletter-bot.git
   ```

2. Install the required dependencies:
    1. `poetry install`
    2. `poetry shell` to enter a shell with the virtual environment activated with your installed dependencies


3. Set up your environment variables:
   - `ESPN_S2`: Your ESPN S2 cookie
   - `SWID`: Your ESPN SWID cookie
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `EMAIL_ADDRESS`: Your email address for sending recaps
   - `EMAIL_PASSWORD`: Your email password or app-specific password


4. Run the main script to generate and send the weekly recap. Adjust as needed for your league.

## More on the ESPN API

ESPN does not support a public API for accessing fantasy football data. In the past few years, they have updated their API a few times. If this happens again, it's likely that it will break the existing setup and will require updating the code.

### How to get your ESPN League ID & Cookies

The League ID is *always* required for all leagues (public or private).

*League ID:* You can find your league ID in the URL when you are on the "Home" page of your league. It's the 8-digit number that comes after `leagueId=` in the URL. For example, in the URL `https://fantasy.espn.com/ffl/league?leagueId=86462812&seasonId=2024`, the league ID is `86462812`.

The `espn_s2` and `SWID` cookies are required for *private* leagues. If you have a public league, you do not need to include these in the requests.

*Cookies:* Navigate to your league home page. Open the develops tools and navigate to the "Network" tab. In the API requests, you should be able to find the `SWID` and `espn_s2` in the cookies section.

### ESPN API Calls Used In This Project
- *mBoxscore:* Used to get the boxscore data for the week.
- *mTeam:* Used to get the team data for the league.
- *mNav:* Used to get the league data.

### Additional ESPN API Calls to Explore
- *mMatchup:* Used to get detailed matchup information for a specific week.
- *mMatchupScore:* Used to get the scores for all matchups in a specific week.
- *mScoreboard:* Used to get the scoreboard data for the league.
- *mRoster:* Used to get detailed roster information for each team.
- *mSettings:* Used to get the league settings and configuration.
- *mTopPerformers:* Used to get data on the top-performing players for a specific period.
- *mStatus:* Used to get the current status of the league and its teams.
- *mPositionalRatings:* Used to get ratings for players by position.
- *kona_player_info:* Used to get detailed information about specific players.

## More on the OpenAI API

You will need to sign up for a paid plan to use the OpenAI API. At the time of writing, the API calls in this project cost less than $0.01 each. 

## More on the Email API

I created a GMail account to send all emails via SMTP. You can use any email provider that supports SMTP. 

If you do use GMail, you will need to create an app-specific password to use the SMTP server. You can do this by navigating to your Google Account, clicking on "Security," and then on "App passwords." Enter your password and select "Mail" as the app. You will then be able to use the password to authenticate your email. In order to do this, you will need to enable two-factor authentication.
