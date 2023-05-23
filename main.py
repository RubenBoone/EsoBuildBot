import os
from dotenv import load_dotenv
import discord


def main():
    load_dotenv()
    BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

    intents = discord.Intents.all()
    intents.message_content = True

    client = Client(intents=intents)
    client.run(BOT_TOKEN)


class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")


if __name__ == "__main__":
    main()
