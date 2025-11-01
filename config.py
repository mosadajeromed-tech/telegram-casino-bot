"""
PickWin Casino Bot - Configuration
All URLs, images, and constants in one place
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================================
# BOT TOKEN
# ============================================================================
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# ============================================================================
# BASE URLS
# ============================================================================
PICKWIN_BASE = "https://pickwin.fun"

# ============================================================================
# CASINO URLS
# ============================================================================
CASINO_URLS = {
    'main': f"{PICKWIN_BASE}/casino",
    'slots': f"{PICKWIN_BASE}/casino/spins/",
    'live': f"{PICKWIN_BASE}/casino/live/",
    'tv': f"{PICKWIN_BASE}/casino/tv/",
    'table': f"{PICKWIN_BASE}/casino/table/",
    'virtual': f"{PICKWIN_BASE}/casino/virtuals/"
}

# ============================================================================
# SPORTS URLS
# ============================================================================
SPORTS_URLS = {
    'main': f"{PICKWIN_BASE}/sportbook/",
    'basketball': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/basketball-2",
    'soccer': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/soccer-1",
    'tennis': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/tennis-5",
    'dota2': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/dota-2-111",
    'ice_hockey': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/ice-hockey-4",
    'counter_strike': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/counter-strike-109",
    'volleyball': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/volleyball-23",
    'baseball': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/baseball-3",
    'boxing': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/boxing-10"
}

# ============================================================================
# OTHER URLS
# ============================================================================
OTHER_URLS = {
    'home': PICKWIN_BASE,
    'promotions': f"{PICKWIN_BASE}/promotions",
    'vip': f"{PICKWIN_BASE}/vip",
    'support': f"{PICKWIN_BASE}/support",
    'account': f"{PICKWIN_BASE}/account",
    'cashier': f"{PICKWIN_BASE}/cashier",
    'help': f"{PICKWIN_BASE}/help"
}

# ============================================================================
# BANNER IMAGES (Rotating per menu)
# ============================================================================
IMAGES = {
    'main': [
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/jCQOouWLM5tOPrkBDuhyZxzuQ7Ch3USKFus0NiiV.png',
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/Fb8yQDCEiX87mCpqLFZE6hNx109Bj9u6ANcHZIo8.jpg',
    ],
    'casino': [
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/w3PBLuQACmZJqWfuT8iiYUzF4BGyvidSC259wWII.png',
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/xVwXPszBgs60AUx56DGQFkbfl5dI75R3bERs5PZ6.jpg',
    ],
    'sports': [
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/9G2TIbOCvBZIKQ6eol1IWdmKxxzDC7JNy22teKDU.jpg',
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/p9UGxjdPeDQ18GjblWLKxVuEr8ZySJcvZpGJ00xW.jpg',
    ],
    'promotions': [
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/G4B2CzcJ6t6Rmklku4FTK5diYfeJkdj7zjLXmwkt.jpg',
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/Un8S6qTB53SOeescreTEFypeOea4oevf7cdV8EXh.jpg',
    ],
    'account': [
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/gCnJfPbNJlyV95n7n1rGcLxbtmdDXzS2eVH7QrPc.jpg',
        'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/TerxFTiYeLlSZNFisNIdhPeqweYUMGn4jELpfJ6R.jpg',
    ]
}

# ============================================================================
# TEXT CONTENT
# ============================================================================
WELCOME_TEXT = """🎰 **Welcome to PickWin Casino!** 🎰

{name}, ready to win big? 🚀

🎁 **NEW PLAYER BONUS**
💰 Get up to $500 + Free Spins!

✨ **What We Offer:**
• 🎰 Thousands of Casino Games
• 🎲 Live Dealer Tables
• ⚽ Sports Betting
• 💸 Instant Crypto Withdrawals
• 🏆 VIP Rewards Program

Choose an option below:"""

CASINO_TEXT = """🎰 **CASINO GAMES** 🎰

Explore our massive casino collection:

🎰 **Slots** - Thousands of games
🎲 **Live Casino** - Real dealers
📺 **TV Games** - Game shows
🃏 **Table Games** - Classic casino
🎮 **Virtual Games** - Instant action

Select a category to play:"""

SPORTS_TEXT = """⚽ **SPORTS BETTING** ⚽

Bet on your favorite sports:

🏀 **Basketball** - NBA, EuroLeague
⚽ **Soccer** - All major leagues
🎾 **Tennis** - Grand Slams
🎮 **Esports** - Dota 2, CS:GO
🏒 **Ice Hockey** - NHL, KHL
🏐 **Volleyball** - World Championships
⚾ **Baseball** - MLB
🥊 **Boxing** - Championship fights

Pick your sport:"""

PROMOTIONS_TEXT = """🎁 **PROMOTIONS & BONUSES** 🎁

Amazing offers waiting for you!

💰 **Welcome Bonus**
Get 100% up to $500 + Free Spins

🔄 **Reload Bonuses**
Up to 50% on every deposit

🎰 **Free Spins**
Daily and weekly offers

💸 **Cashback**
Get 10-20% back on losses

🏆 **VIP Program**
Exclusive rewards and benefits

Explore promotions:"""

ACCOUNT_TEXT = """👤 **MY ACCOUNT** 👤

Manage your PickWin account:

💰 **Cashier**
Deposits & Withdrawals

🎁 **My Bonuses**
Active & Available Bonuses

📊 **History**
Transaction & Game History

⚙️ **Settings**
Account Preferences

🏆 **VIP Status**
Check Your VIP Level

Select an option:"""

SUPPORT_TEXT = """💬 **CUSTOMER SUPPORT** 💬

We're here to help 24/7!

**Contact Options:**

💬 **Live Chat**
Instant help (avg. response: 2 min)

📧 **Email Support**
support@pickwin.fun

❓ **FAQ**
Instant answers to common questions

🛡️ **Responsible Gaming**
Tools and resources

Choose how to reach us:"""

# ============================================================================
# BONUS DETAILS
# ============================================================================
WELCOME_BONUS = {
    'title': '🎁 Welcome Bonus',
    'amount': '$500',
    'percentage': '100%',
    'wagering': '35x',
    'min_deposit': '$20',
    'validity': '30 days'
}

VIP_TIERS = {
    'bronze': {'name': '🥉 Bronze', 'requirement': '$1,000', 'cashback': '10%'},
    'silver': {'name': '🥈 Silver', 'requirement': '$10,000', 'cashback': '12%'},
    'gold': {'name': '🥇 Gold', 'requirement': '$50,000', 'cashback': '15%'},
    'platinum': {'name': '💎 Platinum', 'requirement': '$250,000', 'cashback': '20%'}
}

# ============================================================================
# PAYMENT METHODS
# ============================================================================
CRYPTO_CURRENCIES = ['Bitcoin', 'Ethereum', 'Tether', 'Litecoin', 'Bitcoin Cash']
EWALLET_METHODS = ['PayPal', 'Skrill', 'Neteller']

# ============================================================================
# SUPPORT CONTACTS
# ============================================================================
SUPPORT_EMAIL = "support@pickwin.fun"
SUPPORT_CHAT_URL = f"{PICKWIN_BASE}/support/chat"

# ============================================================================
# RESPONSIBLE GAMBLING RESOURCES
# ============================================================================
HELP_RESOURCES = {
    'international': {
        'GamCare': 'www.gamcare.org.uk',
        'Gambling Therapy': 'www.gamblingtherapy.org'
    },
    'usa': {
        'name': 'National Council on Problem Gambling',
        'phone': '1-800-522-4700'
    },
    'uk': {
        'name': 'BeGambleAware',
        'phone': '0808 8020 133'
    },
    'canada': {
        'name': 'Responsible Gambling Council',
        'phone': '1-888-391-1111'
    }
}
