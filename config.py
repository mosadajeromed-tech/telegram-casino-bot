"""
PickWin Casino Bot - Configuration
Simple and clean
"""
import os
import random
from dotenv import load_dotenv

load_dotenv()

# ============================================================================
# BOT TOKEN
# ============================================================================
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# ============================================================================
# BASE URL
# ============================================================================
PICKWIN_BASE = "https://pickwin.fun"

# ============================================================================
# MAIN URLS
# ============================================================================
URLS = {
    'login': f"{PICKWIN_BASE}/promotions/?modal=login",
    'register': f"{PICKWIN_BASE}/promotions/?modal=registration",
    'sports': f"{PICKWIN_BASE}/sportbook/",
    'casino': f"{PICKWIN_BASE}/casino/",
    'live_casino': f"{PICKWIN_BASE}/casino/live/",
    'vpn_tutorial': "https://www.vpnmentor.com/blog/ultimate-guide-to-vpn/",  # Change this to your VPN tutorial
}

# ============================================================================
# SPORTS URLS
# ============================================================================
SPORTS_URLS = {
    'basketball': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/basketball-2",
    'soccer': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/soccer-1",
    'tennis': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/tennis-5",
    'dota2': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/dota-2-111",
    'ice_hockey': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/ice-hockey-4",
    'counter_strike': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/counter-strike-109",
    'volleyball': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/volleyball-23",
    'baseball': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/baseball-3",
    'boxing': f"{PICKWIN_BASE}/sportbook/?bt-path=/?top=/boxing-10",
}

# ============================================================================
# ALL BANNER IMAGES (Random Selection)
# ============================================================================
ALL_IMAGES = [
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/Fb8yQDCEiX87mCpqLFZE6hNx109Bj9u6ANcHZIo8.jpg',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/w3PBLuQACmZJqWfuT8iiYUzF4BGyvidSC259wWII.png',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/xVwXPszBgs60AUx56DGQFkbfl5dI75R3bERs5PZ6.jpg',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/9G2TIbOCvBZIKQ6eol1IWdmKxxzDC7JNy22teKDU.jpg',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/p9UGxjdPeDQ18GjblWLKxVuEr8ZySJcvZpGJ00xW.jpg',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/G4B2CzcJ6t6Rmklku4FTK5diYfeJkdj7zjLXmwkt.jpg',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/Un8S6qTB53SOeescreTEFypeOea4oevf7cdV8EXh.jpg',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/gCnJfPbNJlyV95n7n1rGcLxbtmdDXzS2eVH7QrPc.jpg',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/jCQOouWLM5tOPrkBDuhyZxzuQ7Ch3USKFus0NiiV.png',
    'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/TerxFTiYeLlSZNFisNIdhPeqweYUMGn4jELpfJ6R.jpg',
]

def get_random_image():
    """Get a random banner image"""
    return random.choice(ALL_IMAGES)

# ============================================================================
# TEXT MESSAGES
# ============================================================================
WELCOME_TEXT = """🎰 **Welcome to PickWin!** 🎰

Ready to play? Choose an option:"""

CASINO_TEXT = """🎰 **CASINO** 🎰

Choose your game type:"""

SPORTS_TEXT = """⚽ **SPORTS BETTING** ⚽

Pick your sport:"""
