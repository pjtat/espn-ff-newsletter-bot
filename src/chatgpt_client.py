import openai
import os
import json
from config import CHATGPT_API_KEY, NEWSLETTER_PERSONALITY, LEAGUE_NAME

# Set up your OpenAI API client
client = openai.OpenAI(api_key=CHATGPT_API_KEY)

def generate_fantasy_recap(boxscore_summary):
    """
    Generates a fantasy football recap in the style of the specified personality.
    
    Args:
        boxscore_summary: Dictionary containing matchup data
        personality_name: Name of the personality style to use (default: "jon taffer")
    
    Returns:
        str: Generated recap text
    
    Raises:
        ValueError: If personality_name is not recognized
    """

    # Define the prompt for the ChatGPT API call
    prompt = f"""
    Generate a {NEWSLETTER_PERSONALITY['name']}-style fantasy football recap!

    You are {NEWSLETTER_PERSONALITY['name']}, with the following bio, tone, and catchphrases:
    - BIO: {NEWSLETTER_PERSONALITY['bio']}
    - TONE: {NEWSLETTER_PERSONALITY['tone']}
    - CATCHPHRASES: {NEWSLETTER_PERSONALITY['catchphrases']}
    - FANTASY FOOTBALL ADAPTATIONS: {NEWSLETTER_PERSONALITY['fantasy_football_adaptations']}
    - FORMATTING PREFERENCES: {NEWSLETTER_PERSONALITY['formatting_preferences']}

    League Overview:
    - 10-team PPR league
    - League name: {LEAGUE_NAME}
    - Starting lineup: 1 QB, 2 RB, 2 WR, 1 TE, 2 FLEX, 1 K
    - Top 6 make playoffs
    - Winner gets trophy and bragging rights; last place gets punished

    Weekly Matchup Data:
    {json.dumps(boxscore_summary, indent=2)}

    Writing Guidelines:
    1. PERSONALITY REQUIREMENTS:
    - Introduce yourself at the beginning of the recap
    - Write in {NEWSLETTER_PERSONALITY['name']}'s tone
    - Use the provided characteristics and catchphrases
    - Stay consistent with the personality's style throughout
    - Sign the email as {NEWSLETTER_PERSONALITY['name']}

    2. MATCHUP RECAP REQUIREMENTS:
    - Each matchup recap MUST be at least 6 sentences long
    - Include the following in EACH matchup recap:
        * Opening narrative setting up the matchup
        * Analysis of at least two key player performances
        * Commentary on lineup decisions (good or bad)
        * Discussion of "what-if" scenarios with benched players
        * Specific callouts of impressive or disappointing performances
        * Closing thoughts with the exact final score

    3. STRUCTURAL REQUIREMENTS:
    - Cover each matchup in detail (8+ sentences each)
    - Include a standings section with:
        * Current ranks
        * Team records (W-L)
        * Total points
        * Owner names

    4. ACCURACY REQUIREMENTS:
    - Use only real matchup data from the provided boxscore
    - Reference actual player performances
    - Use correct team 
    - Refer to owners by first name only

    CREATE A {NEWSLETTER_PERSONALITY['name']}-STYLE RECAP THAT CAPTURES THEIR ESSENCE WHILE MEETING ALL LENGTH AND CONTENT REQUIREMENTS!
    """   
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are the stated personality writing a fantasy football recap newsletter."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=5000,
        n=1,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

def convert_fantasy_recap_to_html(fantasy_recap):
    # Convert the given fantasy football recap to HTML formatting.
    prompt = f"""
    Please formats the given fantasy football recap text with HTML tags for sending via Gmail.

    Do not include any code block formatting such as ```html.

    Do not use color text or bold. 

    {fantasy_recap}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a HTML formatting expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=5000,
        n=1,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

def convert_fantasy_recap_to_plain_text(fantasy_recap):
    # Remove the existing markdown/formatting from the provided fantasy football recap.
    prompt = f"""
    Please remove the existing markdown/formatting from the provided fantasy football recap.

    Please include the football recap in the plain text response and NOTHING else.

    {fantasy_recap}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a plain text formatting expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=5000,
        n=1,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()