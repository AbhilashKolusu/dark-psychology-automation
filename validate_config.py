#!/usr/bin/env python3
"""
Configuration Validator for Dark Psychology Automation

This script checks if all required API keys and social media accounts are configured.
"""

import os
from dotenv import load_dotenv

def validate_configuration():
    """Validate that all required environment variables are set."""

    # Load environment variables
    load_dotenv()

    required_vars = {
        'OPENAI_API_KEY': 'OpenAI API Key (for content generation)',
        'ELEVENLABS_API_KEY': 'ElevenLabs API Key (for voice generation)',
        'AYRSHARE_API_KEY': 'Ayrshare API Key (for social media posting)',
        'INSTAGRAM_USERNAME': 'Instagram username (without @)',
        'TIKTOK_USERNAME': 'TikTok username (without @)',
        'YOUTUBE_CHANNEL_ID': 'YouTube Channel ID'
    }

    optional_vars = {
        'MIDJOURNEY_API_KEY': 'Midjourney API Key (optional, for image generation)',
        'CHANNEL_NAME': 'Channel/Brand Name (defaults to "The Dark Codex")',
        'VOICE_ID': 'ElevenLabs Voice ID (optional)'
    }

    print("🔍 Checking Dark Psychology Automation Configuration\n")

    all_good = True

    print("📋 Required Settings:")
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value and value != f'your-{var.lower()}-here':
            print(f"✅ {var}: Configured")
        else:
            print(f"❌ {var}: NOT SET - {description}")
            all_good = False

    print("\n📋 Optional Settings:")
    for var, description in optional_vars.items():
        value = os.getenv(var)
        if value and value != f'your-{var.lower()}-here':
            print(f"✅ {var}: Configured")
        else:
            print(f"⚠️  {var}: Not set - {description}")

    print("\n" + "="*50)

    if all_good:
        print("🎉 All required configurations are set! Ready to generate content.")
        print("\n💡 Next steps:")
        print("1. Run: make run")
        print("2. Check generated content_*.json files")
        print("3. Set up Make.com automation with the JSON output")
    else:
        print("⚠️  Some required configurations are missing.")
        print("Please edit your .env file with the missing values.")

    return all_good

if __name__ == "__main__":
    validate_configuration()