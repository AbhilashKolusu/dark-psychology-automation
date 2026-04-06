#!/usr/bin/env python3
"""
Dark Psychology Content Automation Script

This script generates viral content packages for Dark Psychology videos
using AI APIs. It creates JSON output that can be parsed by automation tools.
"""

import os
import json
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

SYSTEM_PROMPT = """Act as a Viral Dark Psychology Content Architect. Your goal is to generate a full video package for a 50-second Short.

Output requirements (JSON format only):
{
  "Title": "Viral-optimized title",
  "Hook": "A 3-second psychological 'trap' to stop scrolling",
  "Script": "45 seconds of high-retention narration focusing on a specific dark psychology trick (e.g., The Ben Franklin Effect, Love Bombing, Gaslighting signs)",
  "Image_Prompts": ["5 detailed prompts for an AI image generator (like Midjourney) that match the mood (cinematic, dark, moody lighting, noir style)"],
  "Voice_Setting": "The specific tone (e.g., 'Whispered, deep, male, authoritative')",
  "Captions": "Key words to highlight in bold on screen",
  "Tags": ["10 trending tags for TikTok, YouTube Shorts, and Instagram"],
  "Topic": "[INSERT TOPIC HERE]"
}

IMPORTANT: Output ONLY valid JSON. No additional text or explanations."""

def generate_content_package(topic):
    """Generate a complete content package for the given topic."""

    user_prompt = f"Topic: {topic}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        content = response.choices[0].message.content.strip()

        # Parse the JSON response
        package = json.loads(content)

        return package

    except Exception as e:
        print(f"Error generating content: {e}")
        return None

def save_package(package, filename="content_package.json"):
    """Save the content package to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(package, f, indent=2)
    print(f"Content package saved to {filename}")

def main():
    """Main function to run the content generation."""

    # Example topics - you can modify or make this configurable
    topics = [
        "The Ben Franklin Effect",
        "Love Bombing Tactics",
        "Gaslighting Warning Signs",
        "Mirroring in Social Manipulation",
        "Foot-in-the-Door Technique"
    ]

    for topic in topics:
        print(f"Generating content for: {topic}")
        package = generate_content_package(topic)

        if package:
            filename = f"content_{topic.lower().replace(' ', '_')}.json"
            save_package(package, filename)
        else:
            print(f"Failed to generate content for {topic}")

if __name__ == "__main__":
    main()