import os
import discord
import CONFIG

BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]


def main():
    intents = discord.Intents.default()
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
