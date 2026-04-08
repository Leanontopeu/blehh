import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
from datetime import datetime

load_dotenv()

APPLICATION_ID = 1480003267877535745
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
INVITE_URL = (
    f"https://discord.com/oauth2/authorize"
    f"?client_id={APPLICATION_ID}"
    f"&permissions=8"
    f"&scope=bot%20applications.commands"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("bot.log", encoding="utf-8"),
    ],
)
log = logging.getLogger("blehh")

COGS = [
    "cogs.fun",
    "cogs.utility",
    "cogs.information",
    "cogs.moderation",
    "cogs.social",
    "cogs.economy",
    "cogs.games",
]


class Blehh(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            application_id=APPLICATION_ID,
            intents=intents,
            help_command=None,
        )
        self.start_time = datetime.utcnow()

    async def setup_hook(self):
        for cog in COGS:
            try:
                await self.load_extension(cog)
                log.info(f"Loaded cog: {cog}")
            except Exception as e:
                log.error(f"Failed to load cog {cog}: {e}")
        await self.tree.sync()
        log.info("Slash commands synced globally.")

    async def on_ready(self):
        log.info(f"Logged in as {self.user} (ID: {self.user.id})")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="/help | blehh"
            )
        )

    async def on_command_error(self, ctx, error):
        log.error(f"Command error: {error}")


bot = Blehh()


@bot.tree.command(name="help", description="Show all available commands")
async def help_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔥 blehh — Commands",
        description="Slash commands work in servers, DMs, and group chats!",
        color=0xFF6B35,
    )
    embed.add_field(
        name="🎉 Fun",
        value="`/8ball` `/coinflip` `/roll` `/ship` `/rate` `/joke` `/meme` `/advice` `/fact` `/rizz` `/yomama` `/decide` `/nitro`",
        inline=False,
    )
    embed.add_field(
        name="🔧 Utility",
        value="`/ping` `/uptime` `/remind` `/poll` `/timestamp` `/base64` `/hash` `/math` `/encode`",
        inline=False,
    )
    embed.add_field(
        name="ℹ️ Information",
        value="`/avatar` `/banner` `/userinfo` `/serverinfo` `/about` `/color` `/discordstatus` `/firstmessage`",
        inline=False,
    )
    embed.add_field(
        name="🛡️ Moderation",
        value="`/kick` `/ban` `/mute` `/warn` `/purge` `/slowmode` `/warnings`",
        inline=False,
    )
    embed.add_field(
        name="💞 Social",
        value="`/hug` `/pat` `/slap` `/kiss` `/wave` `/poke`",
        inline=False,
    )
    embed.add_field(
        name="💰 Economy",
        value="`/balance` `/daily` `/work` `/pay` `/leaderboard`",
        inline=False,
    )
    embed.add_field(
        name="🎮 Games",
        value="`/rps` `/trivia` `/hangman` `/slots` `/tictactoe`",
        inline=False,
    )
    embed.set_footer(text="blehh • Built with discord.py")
    await interaction.response.send_message(embed=embed)


if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        log.critical("DISCORD_TOKEN not set in .env — aborting.")
        exit(1)
    bot.run(token, log_handler=None)
  
