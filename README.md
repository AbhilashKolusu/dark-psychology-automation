# Dark Psychology Content Automation

This repository contains an automated system for generating viral Dark Psychology content for YouTube Shorts, TikTok, and Instagram. The goal is to create a "set it and forget it" workflow that produces monetizable content.

## Channel Identity

Choose one of these authoritative, mysterious names for consistency across platforms:
- The Dark Codex (Recommended)
- Shadow Intelligence
- Mind Control Lab
- The Puppet Master
- Subconscious Secrets

## Master Automation Prompt

Use this system instruction with an LLM to generate JSON-formatted video packages:

```
Act as a Viral Dark Psychology Content Architect. Your goal is to generate a full video package for a 50-second Short.

Output requirements (JSON format):
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
```

## Tech Stack

- **Trigger**: Scheduled timer or Google Sheet
- **Brain**: GPT-4/Gemini API
- **Voice**: ElevenLabs API
- **Visuals**: Midjourney/Leonardo.ai API
- **Assembly**: InVideo AI/CapCut API
- **Posting**: Ayrshare/Buffer API

## Monetization Strategies

1. **Creator Funds**: Monetize once hitting follower milestones
2. **Affiliate Marketing**: Promote related products (journals, courses, VPNs)
3. **Digital Products**: Sell e-books like "10 Dark Psychology Tricks"
4. **Sponsorships**: Partner with mental health/security brands

## Important Notes

- Always include educational disclaimers to avoid platform flags
- Focus on curiosity and social power rather than harmful manipulation
- Content should be informative and cautionary

## Setup

1. **Clone and navigate to the project**:
   ```bash
   cd /Users/_ak/Workspace_Personal/dark-psychology-automation
   ```

2. **Install dependencies** (creates virtual environment automatically):
   ```bash
   make install
   ```

3. **Configure API keys and social media accounts**:
   ```bash
   make setup
   # Then edit .env file with your actual API keys and account details
   ```

   **Required API Keys:**
   - `OPENAI_API_KEY`: Get from https://platform.openai.com/api-keys
   - `ELEVENLABS_API_KEY`: Get from https://elevenlabs.io/app/profile
   - `MIDJOURNEY_API_KEY`: Get from Midjourney API (if using API access)
   - `AYRSHARE_API_KEY`: Get from https://ayrshare.com (for social media posting)

   **Social Media Account Details:**
   - `INSTAGRAM_USERNAME`: Your Instagram handle (without @)
   - `TIKTOK_USERNAME`: Your TikTok handle (without @)
   - `YOUTUBE_CHANNEL_ID`: Your YouTube channel ID
   - `CHANNEL_NAME`: Your brand name (default: "The Dark Codex")

4. **Validate your configuration**:
   ```bash
   make validate
   # This will check if all required settings are configured
   ```

5. **Activate the virtual environment** (for manual commands):
   ```bash
   source venv/bin/activate
   ```

6. **Run the automation**:
   ```bash
   make run
   ```

## Manual Commands

If you prefer to run commands manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py
```

## How Social Media Accounts Are Used

The automation system uses your configured social media accounts in the following way:

1. **Instagram & TikTok**: The `INSTAGRAM_USERNAME` and `TIKTOK_USERNAME` are used by Ayrshare API to post content to your specific accounts
2. **YouTube**: The `YOUTUBE_CHANNEL_ID` identifies which channel to upload videos to
3. **Channel Name**: Used in content generation and branding consistency across platforms

**Important**: Make sure these accounts are connected to your Ayrshare account before running the full automation. You can connect social media accounts in your Ayrshare dashboard at https://app.ayrshare.com/