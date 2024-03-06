import discord

from .logger_config import logger
from .settings import settings

bot_token: str = settings.bot_token.get_secret_value()
if not bot_token:
    raise ValueError("Discord token not found in settings.")

intents: discord.flags.Intents = discord.Intents.default()
intents.message_content = True

client: discord.Client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    """
    This function is called when the bot has successfully connected to the server.
    """
    logger.info(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message) -> None:
    """
    This function is triggered when a message is received by the bot.
    It checks if the message was sent by the bot itself, if so, it ignores the message.

    Args:
        message (discord.Message): The message that was received by the bot.
    """
    if message.author == client.user:
        return

    logger.info(f"Message from {message.author}: {message.content}")

    if message.content.startswith("https://"):
        logger.info("Message contains a link.")


client.run(bot_token)
