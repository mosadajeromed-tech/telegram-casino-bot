"""
PickWin Casino Bot - Keyboard Layouts
Simple menus
"""
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import URLS, SPORTS_URLS

# ============================================================================
# MAIN MENU
# ============================================================================
def get_main_menu():
    """Simple main menu"""
    keyboard = [
        [
            InlineKeyboardButton("🎰 Casino", callback_data='casino_menu'),
            InlineKeyboardButton("⚽ Sports", callback_data='sports_menu')
        ],
        [
            InlineKeyboardButton("🔐 Login", web_app=WebAppInfo(url=URLS['login'])),
            InlineKeyboardButton("✨ Register", web_app=WebAppInfo(url=URLS['register']))
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# CASINO MENU
# ============================================================================
def get_casino_menu():
    """Casino menu - only Casino and Live Casino"""
    keyboard = [
        [InlineKeyboardButton("🎰 Casino", web_app=WebAppInfo(url=URLS['casino']))],
        [InlineKeyboardButton("🎲 Live Casino", web_app=WebAppInfo(url=URLS['live_casino']))],
        [InlineKeyboardButton("⬅️ Back", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# SPORTS MENU
# ============================================================================
def get_sports_menu():
    """Sports betting menu"""
    keyboard = [
        [
            InlineKeyboardButton("🏀 Basketball", web_app=WebAppInfo(url=SPORTS_URLS['basketball'])),
            InlineKeyboardButton("⚽ Soccer", web_app=WebAppInfo(url=SPORTS_URLS['soccer']))
        ],
        [
            InlineKeyboardButton("🎾 Tennis", web_app=WebAppInfo(url=SPORTS_URLS['tennis'])),
            InlineKeyboardButton("🏒 Ice Hockey", web_app=WebAppInfo(url=SPORTS_URLS['ice_hockey']))
        ],
        [
            InlineKeyboardButton("🎮 Dota 2", web_app=WebAppInfo(url=SPORTS_URLS['dota2'])),
            InlineKeyboardButton("🎮 Counter Strike", web_app=WebAppInfo(url=SPORTS_URLS['counter_strike']))
        ],
        [
            InlineKeyboardButton("🏐 Volleyball", web_app=WebAppInfo(url=SPORTS_URLS['volleyball'])),
            InlineKeyboardButton("⚾ Baseball", web_app=WebAppInfo(url=SPORTS_URLS['baseball']))
        ],
        [InlineKeyboardButton("🥊 Boxing", web_app=WebAppInfo(url=SPORTS_URLS['boxing']))],
        [InlineKeyboardButton("⬅️ Back", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)
