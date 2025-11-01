"""
PickWin Casino Bot - Keyboard Layouts
All menus and button configurations
"""

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import CASINO_URLS, SPORTS_URLS, OTHER_URLS

# ============================================================================
# MAIN MENU
# ============================================================================

def get_main_menu():
    """Main menu with primary options"""
    keyboard = [
        [
            InlineKeyboardButton("🎰 Casino", callback_data='casino_menu'),
            InlineKeyboardButton("⚽ Sports", callback_data='sports_menu')
        ],
        [
            InlineKeyboardButton("🎁 Promotions", callback_data='promotions_menu'),
            InlineKeyboardButton("👤 My Account", callback_data='account_menu')
        ],
        [
            InlineKeyboardButton("💬 Support", callback_data='support_menu'),
            InlineKeyboardButton("❓ Help", callback_data='help_menu')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# CASINO MENUS
# ============================================================================

def get_casino_menu():
    """Casino games menu - all open in mini app"""
    keyboard = [
        [InlineKeyboardButton("🎰 Slots", web_app=WebAppInfo(url=CASINO_URLS['slots']))],
        [InlineKeyboardButton("🎲 Live Casino", web_app=WebAppInfo(url=CASINO_URLS['live']))],
        [
            InlineKeyboardButton("📺 TV Games", web_app=WebAppInfo(url=CASINO_URLS['tv'])),
            InlineKeyboardButton("🃏 Table Games", web_app=WebAppInfo(url=CASINO_URLS['table']))
        ],
        [InlineKeyboardButton("🎮 Virtual Games", web_app=WebAppInfo(url=CASINO_URLS['virtual']))],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# SPORTS MENUS
# ============================================================================

def get_sports_menu():
    """Sports betting menu - all open in mini app"""
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
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# PROMOTIONS MENU
# ============================================================================

def get_promotions_menu():
    """Promotions menu"""
    keyboard = [
        [InlineKeyboardButton("🎁 Welcome Bonus - $500", callback_data='promo_welcome')],
        [
            InlineKeyboardButton("🔄 Reload Bonus", callback_data='promo_reload'),
            InlineKeyboardButton("🎰 Free Spins", callback_data='promo_freespins')
        ],
        [
            InlineKeyboardButton("💸 Cashback", callback_data='promo_cashback'),
            InlineKeyboardButton("🏆 VIP Rewards", callback_data='promo_vip')
        ],
        [InlineKeyboardButton("📋 View All Promotions", web_app=WebAppInfo(url=OTHER_URLS['promotions']))],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# ACCOUNT MENU
# ============================================================================

def get_account_menu():
    """Account management menu - all open in mini app"""
    keyboard = [
        [InlineKeyboardButton("💰 Cashier (Deposit/Withdraw)", web_app=WebAppInfo(url=OTHER_URLS['cashier']))],
        [
            InlineKeyboardButton("🎁 My Bonuses", web_app=WebAppInfo(url=f"{OTHER_URLS['account']}/bonuses")),
            InlineKeyboardButton("📊 History", web_app=WebAppInfo(url=f"{OTHER_URLS['account']}/history"))
        ],
        [
            InlineKeyboardButton("⚙️ Settings", web_app=WebAppInfo(url=f"{OTHER_URLS['account']}/settings")),
            InlineKeyboardButton("🏆 VIP Status", callback_data='vip_info')
        ],
        [InlineKeyboardButton("👤 View Full Account", web_app=WebAppInfo(url=OTHER_URLS['account']))],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# SUPPORT MENU
# ============================================================================

def get_support_menu():
    """Support options menu"""
    keyboard = [
        [InlineKeyboardButton("💬 Live Chat 24/7", web_app=WebAppInfo(url=f"{OTHER_URLS['support']}/chat"))],
        [
            InlineKeyboardButton("📧 Email Support", callback_data='support_email'),
            InlineKeyboardButton("❓ FAQ", web_app=WebAppInfo(url=f"{OTHER_URLS['help']}/faq"))
        ],
        [InlineKeyboardButton("🛡️ Responsible Gaming", callback_data='responsible_gaming')],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# HELP MENU
# ============================================================================

def get_help_menu():
    """Help and information menu"""
    keyboard = [
        [InlineKeyboardButton("📖 Help Center", web_app=WebAppInfo(url=OTHER_URLS['help']))],
        [
            InlineKeyboardButton("💰 Payment Methods", callback_data='help_payments'),
            InlineKeyboardButton("🎁 Bonus Guide", callback_data='help_bonuses')
        ],
        [
            InlineKeyboardButton("🔐 KYC Verification", callback_data='help_kyc'),
            InlineKeyboardButton("💸 Withdrawals", callback_data='help_withdrawals')
        ],
        [InlineKeyboardButton("💬 Contact Support", callback_data='support_menu')],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# DETAILED INFO MENUS
# ============================================================================

def get_welcome_bonus_keyboard():
    """Welcome bonus detailed view"""
    keyboard = [
        [InlineKeyboardButton("🎁 Claim Bonus Now", web_app=WebAppInfo(url=f"{OTHER_URLS['promotions']}/welcome"))],
        [InlineKeyboardButton("📋 Full Terms & Conditions", web_app=WebAppInfo(url=f"{OTHER_URLS['promotions']}/terms"))],
        [InlineKeyboardButton("⬅️ Back to Promotions", callback_data='promotions_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_payment_info_keyboard():
    """Payment methods information"""
    keyboard = [
        [InlineKeyboardButton("💰 Deposit Now", web_app=WebAppInfo(url=OTHER_URLS['cashier']))],
        [
            InlineKeyboardButton("🟠 Crypto Guide", callback_data='payment_crypto'),
            InlineKeyboardButton("💳 Card Payments", callback_data='payment_cards')
        ],
        [InlineKeyboardButton("⬅️ Back to Help", callback_data='help_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_responsible_gaming_keyboard():
    """Responsible gaming tools"""
    keyboard = [
        [InlineKeyboardButton("⏰ Set Deposit Limits", web_app=WebAppInfo(url=f"{OTHER_URLS['account']}/limits"))],
        [
            InlineKeyboardButton("🛑 Self-Exclusion", web_app=WebAppInfo(url=f"{OTHER_URLS['account']}/exclusion")),
            InlineKeyboardButton("📊 Activity History", web_app=WebAppInfo(url=f"{OTHER_URLS['account']}/history"))
        ],
        [InlineKeyboardButton("📞 Get Help Resources", callback_data='help_resources')],
        [InlineKeyboardButton("⬅️ Back to Support", callback_data='support_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================================
# QUICK ACTION KEYBOARDS
# ============================================================================

def get_back_to_main_button():
    """Simple back to main menu button"""
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]]
    return InlineKeyboardMarkup(keyboard)

def get_quick_play_keyboard():
    """Quick play options"""
    keyboard = [
        [
            InlineKeyboardButton("🎰 Play Slots", web_app=WebAppInfo(url=CASINO_URLS['slots'])),
            InlineKeyboardButton("🎲 Live Casino", web_app=WebAppInfo(url=CASINO_URLS['live']))
        ],
        [
            InlineKeyboardButton("⚽ Sports Betting", web_app=WebAppInfo(url=SPORTS_URLS['main'])),
            InlineKeyboardButton("💰 Deposit", web_app=WebAppInfo(url=OTHER_URLS['cashier']))
        ],
        [InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_promo_action_keyboard(promo_type):
    """Action buttons for specific promotion"""
    keyboard = [
        [InlineKeyboardButton("🎁 Claim This Bonus", web_app=WebAppInfo(url=f"{OTHER_URLS['promotions']}/{promo_type}"))],
        [InlineKeyboardButton("📋 Read Terms", web_app=WebAppInfo(url=f"{OTHER_URLS['promotions']}/terms"))],
        [InlineKeyboardButton("⬅️ Back to Promotions", callback_data='promotions_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)
