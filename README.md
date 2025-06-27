
# Botsy

## Overview
The **Botsy** repository contains a Python-based bot framework designed to automate posting, messaging, and interacting across multiple social media platforms such as Twitter, Facebook, Instagram, Telegram, and Discord.

---

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/Ito-Clash/Botsy.git
cd botsy
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure the Environment

Rename `template.env` to `.env` and populate it with your actual credentials:

```bash
cp template.env .env
nano .env
```

Fill out your tokens:

```env
OPENAI_API_KEY=<Your OpenAI API Key>

# Twitter API Credentials
Account_TWITTER_CONSUMER_KEY=<Your Twitter Consumer Key>
Account_TWITTER_CONSUMER_SECRET=<Your Twitter Consumer Secret>

#Review Template.env for working examples
# Facebook, Instagram, Telegram, Discord, and other keys follow the same pattern
```

---

## Running the Bot

Execute the main script to start bots:

```bash
python src/main.py
```

Optionally, for the GUI:

```bash
python src/gui.py
```

---
## Master Console Commands
- `list` – List available bots and their statuses.
- `start all` – Start all bots.
- `start {bot name}` – Start the specified bot.
- `stop all` – Stop all bots.
- `stop {bot name}` – Stop the specified bot.
- `{bot name}` – Enter control mode for the specified bot.
- `show log all` – Show scheduled log info for all bots with status.
- `help` or `?` – Show help message.
- `exit` – Exit the master console.

## Individual Bot Commands
- `start` – Start the bot.
- `stop` – Stop the bot.
- `new auth` – Force reauthentication by deleting the current token.
- `auth age` – Display the remaining token validity period.
- `run post` – Immediately post content on all platforms.
- `run comment` – Immediately comment on all platforms.
- `run reply` – Immediately reply on all platforms.
- `set post count <num>` – Set how many posts to run in batch operations.
- `set comment count <num>` – Set how many comments to run in batch operations.
- `set reply count <num>` – Set how many replies to run in batch operations.
- `list context` – List contexts defined in configuration.
- `run context {name}` – Execute a specific context.
- `new random all` – Randomize scheduled times for posts, comments, and replies.
- `new random post` – Randomize scheduled post times.
- `new random comment` – Randomize scheduled comment times.
- `new random reply` – Randomize scheduled reply times.
- `stop post` – Disable automatic posting.
- `start post` – Enable automatic posting.
- `stop comment` – Disable automatic commenting.
- `start comment` – Enable automatic commenting.
- `stop reply` – Disable automatic replies.
- `start reply` – Enable automatic replies.
- `start cross` – Enable cross-platform engagement.
- `stop cross` – Disable cross-platform engagement.
- `start trending` – Enable trending topic engagement.
- `stop trending` – Disable trending topic engagement.
- `start dm` – Enable auto DM checking.
- `stop dm` – Disable auto DM checking.
- `run dm {username}` – Send a direct message to a specific user.
- `start story` – Enable automatic collaborative storytelling.
- `stop story` – Disable automatic collaborative storytelling.
- `run story` – Immediately execute collaborative storytelling.
- `run image tweet` – Post immediately with generated images.
- `run adaptive tune` – Adjust parameters based on engagement metrics.
- `show metrics` – Show recent engagement metrics.
- `set mood {mood}` – Manually set the bot's mood (e.g., happy, neutral, serious).
- `show dashboard` – Display a summary dashboard of the bot's status.
- `show settings` – Show current bot settings.
- `show listener` – Display the next scheduled job times.
- `show log` – Show scheduled logs.
- `help` or `?` – Show this help message.
- `back` – Return to the master console.---


## Directory Structure

```
ito-clash-botsy/
├── bots/               # Bot-specific data and caches
├── configs/            # YAML configuration files for each bot
├── src/                # Source code for the bot framework
│   ├── platforms/      # Platform-specific adapters
│   ├── bot.py          # Core bot logic
│   ├── console.py      # CLI interactions
│   ├── gui.py          # GUI interactions
│   └── main.py         # Entry point
├── requirements.txt    # Python dependencies
└── template.env        # Template for environment variables
```

---

## Core Functionality

- **Automated Posting:** Schedule posts across Twitter, Facebook, Instagram, Telegram, and Discord.
- **Adaptive Responses:** Bots dynamically adapt to social interactions based on character profiles.
- **Character Management:** Detailed YAML configurations control character personality, mood, and speech patterns.
- **Cross-Platform Interaction:** Bots coordinate activities across multiple platforms seamlessly.
- **Sentiment Analysis:** Utilizes TextBlob and OpenAI APIs to gauge and respond to user sentiment effectively.
- **Real-Time Interaction:** Responds to monitored users and specific hashtags dynamically.

---

## Commands and Usage

- **Run Bots:**
  ```bash
  python src/main.py
  ```
- **Launch GUI:**
  ```bash
  python src/gui.py
  ```
- **Console Commands:**
  ```bash
  python src/console.py
  ```

---

## Unfinished Features

- **Advanced GUI Dashboard:** Detailed visualization of bot interactions and real-time analytics.
- **Reinforcement Learning Integration:** Adaptive parameter tuning based on engagement feedback.
- **Social Graph Analysis:** Comprehensive identification and interaction with key community influencers.
- **Extended Multimedia Integration:** Automatic generation of images and audio based on engagement metrics.
- **Adaptive Retargeting:** Enhanced cross-platform sharing and narrative coordination.

---

## Licensing

This project is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE) for details.

---

## Contact

For support or questions, please reach out via email or create an issue in the GitHub repository.

---
