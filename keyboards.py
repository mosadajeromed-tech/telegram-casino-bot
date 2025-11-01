"""
PickWin Casino Bot - Keyboard Layouts
With Bonus Flow
"""
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import URLS, SPORTS_URLS

# ============================================================================
# MAIN MENU
# ============================================================================
def get_main_menu():
    """Main menu with bonus button"""
    keyboard = [
        [InlineKeyboardButton("🎁 Claim Bonus", callback_data='bonus_start')],
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
# BONUS FLOW KEYBOARDS
# ============================================================================
def get_player_type_keyboard():
    """Player type selection"""
    keyboard = [
        [InlineKeyboardButton("🎯 Beginner Player (Low Deposit)", callback_data='player_beginner')],
        [InlineKeyboardButton("💎 High Roller (Large Deposit)", callback_data='player_highroller')],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_account_check_keyboard():
    """Account check"""
    keyboard = [
        [InlineKeyboardButton("✅ Yes, I have an account", callback_data='has_account_yes')],
        [InlineKeyboardButton("❌ No, I need to create one", callback_data='has_account_no')],
        [InlineKeyboardButton("⬅️ Back", callback_data='bonus_start')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_verification_keyboard():
    """Verification ready check"""
    keyboard = [
        [InlineKeyboardButton("✅ Yes, my account is ready!", callback_data='account_ready_yes')],
        [InlineKeyboardButton("🔄 Show tutorials again", callback_data='show_tutorials')],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_status_menu():
    """Status check menu for pending requests"""
    keyboard = [
        [InlineKeyboardButton("✅ Check Status", callback_data='check_status')],
        [InlineKeyboardButton("🔄 Start New Request", callback_data='restart_fresh')],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# CASINO MENU
# ============================================================================
def get_casino_menu():
    """Casino menu"""
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

# ============================================================================
# UTILITY KEYBOARDS
# ============================================================================
def get_back_button():
    """Simple back button"""
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]]
    return InlineKeyboardMarkup(keyboard)
