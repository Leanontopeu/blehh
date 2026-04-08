import discord
from discord import app_commands
from discord.ext import commands
import sqlite3
import os
import random
from datetime import datetime, timedelta, timezone

DB_PATH = "data/economy.db"

def get_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS economy (
            user_id TEXT PRIMARY KEY,
            balance INTEGER DEFAULT 0,
            last_daily TEXT,
            last_work TEXT
        )
    """)
    conn.commit()
    return conn

def ensure_user(conn, user_id: str):
    conn.execute("INSERT OR IGNORE INTO economy (user_id, balance) VALUES (?, 0)", (user_id,))
    conn.commit()

def get_balance(conn, user_id: str) -> int:
    ensure_user(conn, user_id)
    row = conn.execute("SELECT balance FROM economy WHERE user_id = ?", (user_id,)).fetchone()
    return row["balance"]

def add_balance(conn, user_id: str, amount: int):
    ensure_user(conn, user_id)
    conn.execute("UPDATE economy SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()

CURRENCY = "🪙"

WORK_JOBS = [
    ("mowed lawns",      50, 150),
    ("delivered pizzas", 80, 200),
    ("debugged code",    100, 300),
    ("walked dogs",      40, 120),
    ("streamed on Twitch", 10, 500),
    ("sold lemonade",    20, 80),
    ("wrote a blog post",60, 180),
    ("fixed a printer",  90, 250),
    ("found a $20 bill", 20, 20),
    ("won a bet",        50, 400),
]


class Economy(commands.Cog):
    """💰 Economy commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ── /balance ──────────────────────────────────────────────────────────────
    @app_commands.command(name="balance", description="Check your (or another user's) balance")
    @app_commands.describe(user="User to check (default: yourself)")
    async def balance(self, interaction: discord.Interaction, user: discord.User = None):
        target = user or interaction.user
        with get_db() as conn:
            bal = get_balance(conn, str(target.id))
        embed = discord.Embed(
            title=f"💰 {target.display_name}'s Balance",
            description=f"{CURRENCY} **{bal:,}** coins",
            color=0xF1C40F
        )
        embed.set_thumbnail(url=target.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    # ── /daily ────────────────────────────────────────────────────────────────
    @app_commands.command(name="daily", description="Claim your daily coins")
    async def daily(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        now = datetime.now(timezone.utc)
        with get_db() as conn:
            ensure_user(conn, user_id)
            row = conn.execute("SELECT last_daily, balance FROM economy WHERE user_id = ?", (user_id,)).fetchone()
            last = row["last_daily"]
            if last:
                last_dt = datetime.fromisoformat(last)
                if last_dt.tzinfo is None:
                    last_dt = last_dt.replace(tzinfo=timezone.utc)
                next_claim = last_dt + timedelta(hours=24)
                if now < next_claim:
                    remaining = next_claim - now
                    h, m = divmod(int(remaining.total_seconds()), 3600)
                    m //= 60
                    await interaction.response.send_message(
                        f"⏰ Daily already claimed! Come back in **{h}h {m}m**.", ephemeral=True
                    )
                    return
            amount = random.randint(100, 500)
            conn.execute("UPDATE economy SET balance = balance + ?, last_daily = ? WHERE user_id = ?",
                         (amount, now.isoformat(), user_id))
            conn.commit()
            new_bal = get_balance(conn, user_id)
        embed = discord.Embed(
            title="📅 Daily Claimed!",
            description=f"You received {CURRENCY} **{amount:,}** coins!\nBalance: {CURRENCY} **{new_bal:,}**",
            color=0x2ECC71
        )
        await interaction.response.send_message(embed=embed)

    # ── /work ─────────────────────────────────────────────────────────────────
    @app_commands.command(name="work", description="Work to earn coins (1h cooldown)")
    async def work(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        now = datetime.now(timezone.utc)
        with get_db() as conn:
            ensure_user(conn, user_id)
            row = conn.execute("SELECT last_work FROM economy WHERE user_id = ?", (user_id,)).fetchone()
            last = row["last_work"]
            if last:
                last_dt = datetime.fromisoformat(last)
                if last_dt.tzinfo is None:
                    last_dt = last_dt.replace(tzinfo=timezone.utc)
                next_work = last_dt + timedelta(hours=1)
                if now < next_work:
                    remaining = next_work - now
                    m = int(remaining.total_seconds()) // 60
                    await interaction.response.send_message(
                        f"⏰ You're tired! Work again in **{m}m**.", ephemeral=True
                    )
                    return
            job, min_earn, max_earn = random.choice(WORK_JOBS)
            earned = random.randint(min_earn, max_earn)
            conn.execute("UPDATE economy SET balance = balance + ?, last_work = ? WHERE user_id = ?",
                         (earned, now.isoformat(), user_id))
            conn.commit()
            new_bal = get_balance(conn, user_id)
        embed = discord.Embed(
            title="💼 Work Complete",
            description=f"You **{job}** and earned {CURRENCY} **{earned:,}**!\nBalance: {CURRENCY} **{new_bal:,}**",
            color=0x3498DB
        )
        await interaction.response.send_message(embed=embed)

    # ── /pay ──────────────────────────────────────────────────────────────────
    @app_commands.command(name="pay", description="Pay coins to another user")
    @app_commands.describe(user="Who to pay", amount="Amount to pay")
    async def pay(self, interaction: discord.Interaction, user: discord.User, amount: int):
        if user.id == interaction.user.id:
            await interaction.response.send_message("❌ You can't pay yourself.", ephemeral=True)
            return
        if amount <= 0:
            await interaction.response.send_message("❌ Amount must be positive.", ephemeral=True)
            return
        sender_id = str(interaction.user.id)
        receiver_id = str(user.id)
        with get_db() as conn:
            sender_bal = get_balance(conn, sender_id)
            if sender_bal < amount:
                await interaction.response.send_message(
                    f"❌ Insufficient funds. You have {CURRENCY} **{sender_bal:,}**.", ephemeral=True
                )
                return
            conn.execute("UPDATE economy SET balance = balance - ? WHERE user_id = ?", (amount, sender_id))
            add_balance(conn, receiver_id, amount)
            new_sender = get_balance(conn, sender_id)
        embed = discord.Embed(
            title="💸 Payment Sent",
            description=f"Sent {CURRENCY} **{amount:,}** to **{user.display_name}**!\nYour balance: {CURRENCY} **{new_sender:,}**",
            color=0x2ECC71
        )
        await interaction.response.send_message(embed=embed)

    # ── /leaderboard ──────────────────────────────────────────────────────────
    @app_commands.command(name="leaderboard", description="Top 10 richest users")
    async def leaderboard(self, interaction: discord.Interaction):
        await interaction.response.defer()
        with get_db() as conn:
            rows = conn.execute(
                "SELECT user_id, balance FROM economy ORDER BY balance DESC LIMIT 10"
            ).fetchall()
        if not rows:
            await interaction.followup.send("No economy data yet. Use `/daily` or `/work` to start!")
            return
        embed = discord.Embed(title="🏆 Economy Leaderboard", color=0xF1C40F)
        medals = ["🥇", "🥈", "🥉"] + ["🏅"] * 7
        lines = []
        for i, row in enumerate(rows):
            try:
                user = await self.bot.fetch_user(int(row["user_id"]))
                name = user.display_name
            except Exception:
                name = f"User {row['user_id']}"
            lines.append(f"{medals[i]} **{name}** — {CURRENCY} {row['balance']:,}")
        embed.description = "\n".join(lines)
        await interaction.followup.send(embed=embed)

    # ── /gamble ───────────────────────────────────────────────────────────────
    @app_commands.command(name="gamble", description="Gamble your coins (50/50 chance)")
    @app_commands.describe(amount="Amount to gamble")
    async def gamble(self, interaction: discord.Interaction, amount: int):
        if amount <= 0:
            await interaction.response.send_message("❌ Amount must be positive.", ephemeral=True)
            return
        user_id = str(interaction.user.id)
        with get_db() as conn:
            bal = get_balance(conn, user_id)
            if bal < amount:
                await interaction.response.send_message(
                    f"❌ Not enough coins. Balance: {CURRENCY} **{bal:,}**", ephemeral=True
                )
                return
            win = random.random() < 0.5
            delta = amount if win else -amount
            add_balance(conn, user_id, delta)
            new_bal = get_balance(conn, user_id)
        color = 0x2ECC71 if win else 0xE74C3C
        result = f"🎉 You **won** {CURRENCY} **{amount:,}**!" if win else f"💀 You **lost** {CURRENCY} **{amount:,}**."
        embed = discord.Embed(
            title="🎰 Gamble Result",
            description=f"{result}\nBalance: {CURRENCY} **{new_bal:,}**",
            color=color
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Economy(bot))
