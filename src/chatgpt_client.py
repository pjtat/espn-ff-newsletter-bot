import openai
import os
import json
from config import CHATGPT_API_KEY, NEWSLETTER_PERSONALITY_NAME, NEWSLETTER_PERSONALITY_TRAITS_TEMPLATE

# Set up your OpenAI API client
client = openai.OpenAI(api_key=CHATGPT_API_KEY)

def generate_matchup_recap(individual_matchup_summary, newsletter_text, personality_bio):
    """
    Generates a fantasy football recap for an individual matchup.

    The recap generation was separated into multiple function calls to increase the quality of the responses. 
    
    Asking for all of the matchup summaries in a single response resulted in matchups that were too small. 
    """

    # Define the prompt for the ChatGPT API call
    prompt = f"""
    Generate a {NEWSLETTER_PERSONALITY_NAME}-style fantasy football recap that perfectly matches their unique personality.

    Matchup Data:
    {json.dumps(individual_matchup_summary, indent=2)}

    Personality Profile:
    {json.dumps(personality_bio, indent=2)}

    Writing Guidelines:
    1. PERSONALITY & TONE:
    - Embody an extreme, over-the-top version of the personality bio
    - Include signature catchphrases and mannerisms in an amplified way
    - Make bold, outrageous statements while staying true to the core personality
    - Don't hold back - be edgy, controversial and entertaining

    2. MATCHUP RECAP REQUIREMENTS:
    - Cover key points:
        * Winners and losers
        * Notable lineup decisions
        * Benched player analysis
        * Final score reveal
    - Stay true to their analysis style from the bio
    - Make fun of the losing teams and roast the losing team owners  

    3. STRUCTURAL REQUIREMENTS:
    - Start with team names: "[Team A] vs. [Team B]"
    - Write the analysis as a single, focused paragraph without line breaks or section headers
    - Keep length to 700-800 characters
    - Use emphasis patterns specified in bio

    4. ACCURACY REQUIREMENTS:
    - Use accurate stats and data
    - Frame analysis in personality's perspective

    Create a recap that embodies this personality while delivering insightful fantasy analysis!
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

def generate_newsletter_intro(newsletter_text, personality_bio, special_instructions=""):
    """
    Generates an intro for the newsletter.
    """

    # Define the prompt for the ChatGPT API call
    prompt = f"""
    Generate a {NEWSLETTER_PERSONALITY_NAME}-style fantasy football recap for the league.

    Matchup Summaries:
    {newsletter_text}

    Personality Profile:
    {json.dumps(personality_bio, indent=2)}

    Special Instructions:
    {special_instructions}

    Writing Guidelines:
    1. PERSONALITY & TONE:
    - Match the provided personality bio 

    2. INTRO REQUIREMENTS:
    - Write a short intro for the newsletter to introduce the provided recap and standings.
    - The intro should be 3-4 sentences.
    - The intro should align with the provided information and NOT repeat it.   
    - The intro should be engaging and capture the attention of the reader.

    Create an intro that embodies this personality while setting up the newsletter!
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

def generate_newsletter_closing(newsletter_text, personality_bio, special_instructions=""):
    """
    Generates a closing for the newsletter.
    """

    # Define the prompt for the ChatGPT API call
    prompt = f"""
    Generate a {NEWSLETTER_PERSONALITY_NAME}-style fantasy football recap for the league.

    Matchup Summaries:
    {newsletter_text}

    Personality Profile:
    {json.dumps(personality_bio, indent=2)}

    Special Instructions:
    {special_instructions}

    Writing Guidelines:
    1. PERSONALITY & TONE:
    - Match the provided personality bio

    2. CLOSING REQUIREMENTS:
    - Write a short closing for the newsletter to wrap up the recap.
    - The closing should be 3-4 sentences.
    - The closing should align with the provided information and NOT repeat it.   
    - The closing should be engaging and capture the attention of the reader.

    Create a closing that embodies this personality while wrapping up the newsletter!
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

def generate_end_of_season_summary(medal_winners):
    # Define the prompt for the ChatGPT API call
    prompt = f"""
    Generate a {NEWSLETTER_PERSONALITY_NAME}-style fantasy football recap for the league.

    Medal Winners:
    {json.dumps(medal_winners, indent=2)}

    Writing Guidelines:
    1. PERSONALITY & TONE:
    - Match the provided personality bio

    2. CLOSING REQUIREMENTS:
    - This was the final week of the season. Generate a summary of the end of the season and the medal winners (gold, silver, bronze).
    - The summary should be 2-3 sentences.
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

def generate_newsletter_personality_traits(personality_name):
    # Generate peronsality traits and bio based on the name
    prompt = f"""
    Create a detailed personality profile for {NEWSLETTER_PERSONALITY_NAME} with the following structure:

    {NEWSLETTER_PERSONALITY_TRAITS_TEMPLATE}

    Requirements:
    1. Fill in all sections of the provided structure
    2. Maintain consistency with the character's known traits
    3. Include specific mannerisms and catchphrases
    4. Add distinctive writing patterns and speech habits
    5. Ensure all traits align with the personality's public persona
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