# Configuration file for Dark Psychology Automation
# This file loads settings from environment variables

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AI Service APIs
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
MIDJOURNEY_API_KEY = os.getenv('MIDJOURNEY_API_KEY')

# Social Media Posting API
AYRSHARE_API_KEY = os.getenv('AYRSHARE_API_KEY')

# Social Media Account Details
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
TIKTOK_USERNAME = os.getenv('TIKTOK_USERNAME')
YOUTUBE_CHANNEL_ID = os.getenv('YOUTUBE_CHANNEL_ID')

# Channel Settings
CHANNEL_NAME = os.getenv('CHANNEL_NAME', 'The Dark Codex')

# Voice Settings
VOICE_MODEL = "eleven_monolingual_v1"
VOICE_ID = os.getenv('VOICE_ID')  # Get from ElevenLabs dashboard

# Content Settings
VIDEO_LENGTH_SECONDS = int(os.getenv('VIDEO_LENGTH_SECONDS', 50))
HOOK_LENGTH_SECONDS = int(os.getenv('HOOK_LENGTH_SECONDS', 3))
SCRIPT_LENGTH_SECONDS = int(os.getenv('SCRIPT_LENGTH_SECONDS', 45))