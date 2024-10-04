# Fantasy Football League Recap Generator

This project automates the process of generating and sending weekly recaps for a fantasy football league using data from the ESPN API and OpenAI's GPT model.

## Features

-   Fetches league data, boxscores, and team information from the ESPN API
-   Processes and summarizes the fetched data
-   Generates a detailed fantasy football recap using OpenAI's GPT model
-   Converts the generated recap to HTML format
-   Sends the recap via email to league participants

## Prerequisites

-   Python 3.7+
-   ESPN API access
-   OpenAI API key
-   SMTP server access for sending emails

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/pjtat/espn-ff-newsletter-bot.git
    ```

2. Install the required dependencies:
   [To update later]

3. Set up your environment variables:
    - `ESPN_S2`: Your ESPN S2 cookie
    - `SWID`: Your ESPN SWID cookie
    - `OPENAI_API_KEY`: Your OpenAI API key
    - `EMAIL_ADDRESS`: Your email address for sending recaps
    - `EMAIL_PASSWORD`: Your email password or app-specific password

## Usage

Run the main script to generate and send the weekly recap:

## Other ESPN API calls to Explore

-   mMatchupmNav
-   mRostermSettings
-   mTopPerformers
-   mMatchupScore
-   mTeam
-   mScoreboard
-   mStatus
-   mPositionalRatings
-   kona_player_info
