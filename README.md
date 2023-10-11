
# Discord TumorBot

Discord TumorBot is a Python-based Discord bot that uses a pre-trained ResNet-50 model to classify brain tumor types from uploaded images. It allows users to interact with the bot using slash commands and predict the type of tumor in medical images.

## Features

- Slash commands for interacting with the bot.
- Predict the type of brain tumor from uploaded medical images.
- Greet users and respond to simple commands.

## Prerequisites

Before running the bot, make sure you have the following dependencies installed:

- Python 3.8
- Discord.py library
- PyTorch and torchvision (CPU-compatible versions)
- Pillow (PIL)
- Other necessary libraries (check requirements.txt)

You can install the required packages using the provided `requirements.txt` file.

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/devchaitanya/discord-tumorbot.git
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Invite the Bot:

   Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications) and invite it to your server.

5. Create a `.env` file in the root directory of the project and add your Discord bot token:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   ```

6. Load the model:

   Download the trained model from here [MODEL](https://drive.google.com/file/d/1EfJ4nyGLvznEvtKSHuc2zr90NzDU2VtR/view?usp=drive_link)
   
   Make sure you have the ResNet-50 model weights saved in the correct location (`DiscordBot/models/bt_resnet50_model.pt`) or modify the path accordingly.

8. Run the bot:

   ```bash
   python discord_bot.py
   ```

## Usage

- Use the `/predict` command in your Discord server to upload a medical image and receive the predicted brain tumor type.

