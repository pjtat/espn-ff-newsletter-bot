import openai
import os
import json
from config import CHATGPT_API_KEY, NEWSLETTER_PERSONALITY, LEAGUE_NAME

# Set up your OpenAI API client
client = openai.OpenAI(api_key=CHATGPT_API_KEY)

def generate_matchup_recap(individual_matchup_summary, newsletter_text):
    """
    Generates a fantasy football recap for an individual matchup.

    The recap generation was separated into multiple function calls to increase the quality of the responses. 
    
    Asking for all of the matchup summaries in a single response resulted in matchups that were too small. 
    """

    # Define the prompt for the ChatGPT API call
    prompt = f"""
    Generate a {NEWSLETTER_PERSONALITY['name']}-style fantasy football recap of the provided matchup!

    You are {NEWSLETTER_PERSONALITY['name']}, with the following bio, tone, and catchphrases:
    {NEWSLETTER_PERSONALITY}

    Matchup Data:
    {json.dumps(individual_matchup_summary, indent=2)}

    Writing Guidelines:
    1. PERSONALITY REQUIREMENTS:
    - Write in {NEWSLETTER_PERSONALITY['name']}'s tone
    - Stay consistent with the personality's style throughout
    - Make jokes, be sarcastic, be edgy, and insult the losing teams

    2. MATCHUP RECAP REQUIREMENTS:
    - Include the following in the recap:
        * Analysis of key player performances
        * Commentary on lineup decisions (good or bad)
        * Discussion of "what-if" scenarios with benched players
        * Specific callouts of impressive or disappointing performances
        * Closing thoughts with the final score

    3. STRUCTURAL REQUIREMENTS:
    - Title the section with [Team A] vs [Team B]
    - THE RECAP SHOULD BE BETWEEN 700 AND 800 CHARACTERS LONG
    - THE RECAP SHOULD BE ONE SINGLE PARAGRAPH

    4. ACCURACY REQUIREMENTS:
    - DO NOT REPEAT YOURSELF (INCLUDING INFORMATION FROM PREVIOUS RECAPS IN THE NEWSLETTER TEXT)
    - Use only real matchup data from the provided matchup summary
    - Reference actual player performances
    - Refer to owners by first name only

    CREATE A {NEWSLETTER_PERSONALITY['name']}-STYLE RECAP THAT CAPTURES THEIR ESSENCE WHILE MEETING ALL REQUIREMENTS!
    """   
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are the stated personality writing a fantasy football recap newsletter."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000,
        n=1,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

def generate_newsletter_intro(newsletter_text):
    """
    Generates an intro for the newsletter.
    """

    # Define the prompt for the ChatGPT API call
    prompt = f"""
    Generate a {NEWSLETTER_PERSONALITY['name']}-style fantasy football recap for the league. 

    You are {NEWSLETTER_PERSONALITY['name']}, with the following bio, tone, and catchphrases:
    {NEWSLETTER_PERSONALITY}

    Matchup Summaries:
    {newsletter_text}

    Writing Guidelines:
    1. PERSONALITY REQUIREMENTS:
    - Write in {NEWSLETTER_PERSONALITY['name']}'s tone
    - Use the provided characteristics and catchphrases
    - Stay consistent with the personality's style throughout

    2. INTRO REQUIREMENTS:
    - Write a short intro for the newsletter to introduce the provided recap and standings.
    - The intro should be 3-4 sentences.
    - The intro should align with the provided information and NOT repeat it.   
    - The intro should be engaging and capture the attention of the reader.
    - Always start the intro with "I'VE BEEN IN THIS BUSINESS FOR 30 YEARS"
    - DO NOT REPEAT YOURSELF

    CREATE A {NEWSLETTER_PERSONALITY['name']}-STYLE RECAP THAT CAPTURES THEIR ESSENCE WHILE MEETING ALL REQUIREMENTS!
    """   
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are the stated personality writing a fantasy football recap newsletter."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000,
        n=1,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

def generate_newsletter_closing(newsletter_text):
    """
    Generates an intro for the newsletter.
    """

    # Define the prompt for the ChatGPT API call
    prompt = f"""
    Generate a {NEWSLETTER_PERSONALITY['name']}-style fantasy football recap for the league. 

    You are {NEWSLETTER_PERSONALITY['name']}, with the following bio, tone, and catchphrases:
    {NEWSLETTER_PERSONALITY}

    Matchup Summaries:
    {newsletter_text}

    Writing Guidelines:
    1. PERSONALITY REQUIREMENTS:
    - Write in {NEWSLETTER_PERSONALITY['name']}'s tone
    - Use the provided characteristics and catchphrases
    - Stay consistent with the personality's style throughout

    2. CLOSING REQUIREMENTS:
    - Write a short closing for the newsletter to wrap up the recap.
    - The closing should be 3-4 sentences.
    - The closing should align with the provided information and NOT repeat it.   
    - The closing should be engaging and capture the attention of the reader.
    - DO NOT REPEAT YOURSELF

    CREATE A {NEWSLETTER_PERSONALITY['name']}-STYLE CLOSING THAT CAPTURES THEIR ESSENCE WHILE MEETING ALL REQUIREMENTS!
    """   
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are the stated personality writing a fantasy football recap newsletter."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000,
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
        max_tokens=8192,
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