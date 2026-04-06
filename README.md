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

1. Install dependencies: `pip install -r requirements.txt`
2. Configure API keys in `config.py`
3. Run the automation script: `python main.py`

## Disclaimer

This system is for educational and entertainment purposes only. Dark psychology concepts should be studied responsibly and never used to harm others.