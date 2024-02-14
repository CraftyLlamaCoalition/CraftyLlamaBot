# This example requires the 'message_content' intent.
import discord

from .passmanager import PassManager

pm: PassManager = PassManager()
client_key: str = pm.get_password("discord/key")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    """
    This function is called when the bot has successfully connected to the server.
    """
    print(f"We have logged in as {client.user}")


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

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


client.run(client_key)
