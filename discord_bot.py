import datetime
import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import io
from model_loader import resnet_model, transform, LABELS  # Import model-related code
import torch
from PIL import Image
import pytz

DEVICE_NAME = "cpu"
device = torch.device(DEVICE_NAME)

# Load environment variables
load_dotenv()

# Discord bot code
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name='clear')
@app_commands.describe()
async def clear_messages(ctx):
    channel = ctx.channel
    messages = []
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    async for message in channel.history(limit=None):
        if (utc_now - message.created_at).days < 14:
            messages.append(message)
    print(f"Deleting {len(messages)} messages")
    while messages:
        batch = messages[:100]
        messages = messages[100:]
        await channel.delete_messages(batch)
    
@bot.tree.command(name="predict")
@app_commands.describe(image="Upload an image to predict")
async def predict(ctx, image: discord.Attachment):
    # Check if the attachment is an image
    if not image.content_type.startswith('image/'):
        await ctx.send("Please upload a valid image.")
        return

    try:
        img = transform(Image.open(io.BytesIO(await image.read())))

        img = img[None, ...]

        with torch.no_grad():
            y_hat = resnet_model.forward(img.to(device))

            predicted = torch.argmax(y_hat.data, dim=1)

            result = LABELS[predicted.data]
        
        await ctx.response.send_message(f"Type of Tumor is {result}")
    except Exception as e:
        await ctx.response.send_message(f"An error occurred: {str(e)}")


bot.run(TOKEN)
