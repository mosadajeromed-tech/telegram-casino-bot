import logging
import os
from datetime import datetime
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from telegram.error import BadRequest, TimedOut, NetworkError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Basic Setup ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

API_TOKEN = os.environ.get('BOT_TOKEN')
if not API_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# PickWin Website URLs
PICKWIN_BASE = "https://pickwin.fun"
PICKWIN_LOGIN = f"{PICKWIN_BASE}/login"
PICKWIN_REGISTER = f"{PICKWIN_BASE}/register"
PICKWIN_GAMES = f"{PICKWIN_BASE}/games"
PICKWIN_SLOTS = f"{PICKWIN_BASE}/games/slots"
PICKWIN_LIVE_CASINO = f"{PICKWIN_BASE}/games/live-casino"
PICKWIN_SPORTS = f"{PICKWIN_BASE}/sports"
PICKWIN_PROMOTIONS = f"{PICKWIN_BASE}/promotions"
PICKWIN_CASHIER = f"{PICKWIN_BASE}/cashier"
PICKWIN_SUPPORT = f"{PICKWIN_BASE}/support"
PICKWIN_VIP = f"{PICKWIN_BASE}/vip"

# Banner Image URL
BANNER_IMAGE = 'https://fungamess.games/cdn-cgi/image/w=1500,f=avif,q=80/https://pickwin.fun/external_storage/banners/jCQOouWLM5tOPrkBDuhyZxzuQ7Ch3USKFus0NiiV.png'

# --- Keyboard Layouts ---

def get_main_menu():
    """Main menu with all primary options"""
    keyboard = [
        [
            InlineKeyboardButton("🎮 Play Now", web_app=WebAppInfo(url=PICKWIN_BASE)),
            InlineKeyboardButton("🔐 Login", url=PICKWIN_LOGIN)
        ],
        [
            InlineKeyboardButton("✨ Register & Get $500 Bonus", url=PICKWIN_REGISTER)
        ],
        [
            InlineKeyboardButton("🎰 Games", callback_data='games_menu'),
            InlineKeyboardButton("🎁 Promotions", callback_data='promotions')
        ],
        [
            InlineKeyboardButton("💰 Deposit", url=PICKWIN_CASHIER),
            InlineKeyboardButton("🏆 VIP Club", callback_data='vip_info')
        ],
        [
            InlineKeyboardButton("💬 Support 24/7", callback_data='support'),
            InlineKeyboardButton("❓ Help", callback_data='help')
        ],
        [
            InlineKeyboardButton("🛡️ Play Responsibly", callback_data='responsible_gambling')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_games_menu():
    """Games category menu"""
    keyboard = [
        [
            InlineKeyboardButton("🎰 Slots (4,000+ Games)", url=PICKWIN_SLOTS)
        ],
        [
            InlineKeyboardButton("🎲 Live Casino", url=PICKWIN_LIVE_CASINO),
            InlineKeyboardButton("⚽ Sports Betting", url=PICKWIN_SPORTS)
        ],
        [
            InlineKeyboardButton("🔥 Popular Games", callback_data='popular_games'),
            InlineKeyboardButton("🆕 New Releases", callback_data='new_games')
        ],
        [
            InlineKeyboardButton("🎯 Providers", callback_data='game_providers')
        ],
        [
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_promotions_menu():
    """Promotions and bonuses menu"""
    keyboard = [
        [
            InlineKeyboardButton("🎁 Welcome Bonus - $500", callback_data='welcome_bonus')
        ],
        [
            InlineKeyboardButton("💎 VIP Rewards", callback_data='vip_rewards'),
            InlineKeyboardButton("🔄 Reload Bonus", callback_data='reload_bonus')
        ],
        [
            InlineKeyboardButton("🎰 Free Spins", callback_data='free_spins'),
            InlineKeyboardButton("💸 Cashback", callback_data='cashback')
        ],
        [
            InlineKeyboardButton("🏆 Tournaments", callback_data='tournaments')
        ],
        [
            InlineKeyboardButton("📋 View All Promos", url=PICKWIN_PROMOTIONS)
        ],
        [
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_payment_menu():
    """Payment methods menu"""
    keyboard = [
        [
            InlineKeyboardButton("💳 Deposit Now", url=PICKWIN_CASHIER)
        ],
        [
            InlineKeyboardButton("🟠 Crypto (Bitcoin, ETH, USDT)", callback_data='crypto_info'),
        ],
        [
            InlineKeyboardButton("💳 Credit/Debit Cards", callback_data='card_info'),
            InlineKeyboardButton("💵 E-Wallets", callback_data='ewallet_info')
        ],
        [
            InlineKeyboardButton("💰 Withdrawal Info", callback_data='withdrawal_info')
        ],
        [
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_support_menu():
    """Support options menu"""
    keyboard = [
        [
            InlineKeyboardButton("💬 Live Chat 24/7", url=f"{PICKWIN_SUPPORT}/chat")
        ],
        [
            InlineKeyboardButton("📧 Email Support", callback_data='email_support'),
            InlineKeyboardButton("❓ FAQ", callback_data='faq')
        ],
        [
            InlineKeyboardButton("📱 Contact Options", callback_data='contact_info')
        ],
        [
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_responsible_gambling_menu():
    """Responsible gambling resources"""
    keyboard = [
        [
            InlineKeyboardButton("⏰ Set Deposit Limits", url=f"{PICKWIN_BASE}/responsible-gaming/limits")
        ],
        [
            InlineKeyboardButton("🛑 Self-Exclusion", callback_data='self_exclusion'),
            InlineKeyboardButton("📊 Activity History", url=f"{PICKWIN_BASE}/account/history")
        ],
        [
            InlineKeyboardButton("📞 Get Help Resources", callback_data='help_resources')
        ],
        [
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_account_menu():
    """Account management menu"""
    keyboard = [
        [
            InlineKeyboardButton("🔐 Login", url=PICKWIN_LOGIN),
            InlineKeyboardButton("✨ Register", url=PICKWIN_REGISTER)
        ],
        [
            InlineKeyboardButton("👤 My Account", url=f"{PICKWIN_BASE}/account")
        ],
        [
            InlineKeyboardButton("💰 Deposit", url=PICKWIN_CASHIER),
            InlineKeyboardButton("💸 Withdraw", url=f"{PICKWIN_CASHIER}/withdraw")
        ],
        [
            InlineKeyboardButton("🎁 My Bonuses", url=f"{PICKWIN_BASE}/account/bonuses")
        ],
        [
            InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_quick_action_keyboard():
    """Quick action buttons"""
    keyboard = [
        [
            InlineKeyboardButton("🎮 Play Now", web_app=WebAppInfo(url=PICKWIN_BASE)),
        ],
        [
            InlineKeyboardButton("✨ Register", url=PICKWIN_REGISTER),
            InlineKeyboardButton("🔐 Login", url=PICKWIN_LOGIN)
        ],
        [
            InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_back_button():
    """Simple back button"""
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]]
    return InlineKeyboardMarkup(keyboard)

# --- Command Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message with main menu"""
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    # Track session start
    context.user_data['session_start'] = datetime.now()
    context.user_data['chat_id'] = chat_id
    
    welcome_text = (
        f"🎰 **Welcome to PickWin Casino!** 🎰\n\n"
        f"Hey {user.first_name}! 👋\n\n"
        f"🎁 **NEW PLAYER BONUS**\n"
        f"💰 100% up to $500 + Free Spins!\n\n"
        f"✨ **What We Offer:**\n"
        f"• 4,000+ Casino Games\n"
        f"• Live Dealer Tables\n"
        f"• Sports Betting\n"
        f"• Instant Crypto Withdrawals\n"
        f"• 24/7 Live Support\n\n"
        f"Choose an option below to get started:"
    )
    
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=BANNER_IMAGE,
        caption=welcome_text,
        parse_mode='Markdown',
        reply_markup=get_main_menu()
    )

# --- Callback Handlers ---

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all button callbacks"""
    query = update.callback_query
    await query.answer()
    
    # MAIN MENU
    if query.data == 'back_main':
        await show_main_menu(query, context)
    
    # GAMES MENU
    elif query.data == 'games_menu':
        text = (
            "🎮 **GAMES COLLECTION** 🎮\n\n"
            "Explore over 4,000 premium games:\n\n"
            "🎰 **Slots**\n"
            "• Classic Slots\n"
            "• Video Slots\n"
            "• Progressive Jackpots\n"
            "• Megaways Games\n\n"
            "🎲 **Live Casino**\n"
            "• Roulette, Blackjack, Baccarat\n"
            "• Game Shows\n"
            "• Poker Tables\n\n"
            "⚽ **Sports Betting**\n"
            "• Live & Pre-match\n"
            "• All major sports\n\n"
            "Select a category:"
        )
        await query.edit_message_caption(
            caption=text,
            reply_markup=get_games_menu(),
            parse_mode='Markdown'
        )
    
    # POPULAR GAMES
    elif query.data == 'popular_games':
        text = (
            "🔥 **POPULAR GAMES** 🔥\n\n"
            "🎰 **Top Slots:**\n"
            "• Sweet Bonanza 1000\n"
            "• Big Bass Bonanza\n"
            "• Gates of Olympus\n"
            "• Sugar Rush\n"
            "• The Dog House\n\n"
            "🎲 **Live Casino:**\n"
            "• Lightning Roulette\n"
            "• Crazy Time\n"
            "• Mega Ball\n"
            "• Dream Catcher\n\n"
            "Click 'Play Now' to start!"
        )
        await query.edit_message_caption(
            caption=text,
            reply_markup=get_quick_action_keyboard(),
            parse_mode='Markdown'
        )
    
    # GAME PROVIDERS
    elif query.data == 'game_providers':
        text = (
            "🏆 **GAME PROVIDERS** 🏆\n\n"
            "We partner with the best:\n\n"
            "⭐ **Top Providers:**\n"
            "• Pragmatic Play\n"
            "• Evolution Gaming\n"
            "• NetEnt\n"
            "• Play'n GO\n"
            "• Microgaming\n"
            "• Red Tiger\n"
            "• Quickspin\n"
            "• Yggdrasil\n"
            "• Big Time Gaming\n"
            "• Hacksaw Gaming\n\n"
            "...and 80+ more providers!\n\n"
            "All games are certified and fair ✅"
        )
        await query.edit_message_caption(
            caption=text,
            reply_markup=get_quick_action_keyboard(),
            parse_mode='Markdown'
        )
    
    # PROMOTIONS
    elif query.data == 'promotions':
        await show_promotions_menu(query)
    
    elif query.data == 'welcome_bonus':
        text = (
            "🎁 **WELCOME BONUS** 🎁\n\n"
            "💰 **100% up to $500**\n\n"
            "**How It Works:**\n"
            "1️⃣ Register your account\n"
            "2️⃣ Make your first deposit\n"
            "3️⃣ Get 100% bonus instantly!\n\n"
            "**Example:**\n"
            "Deposit $500 → Get $500 bonus\n"
            "Total: $1,000 to play! 🎰\n\n"
            "**Bonus Terms:**\n"
            "• Minimum deposit: $20\n"
            "• Wagering: 35x bonus\n"
            "• Valid for 30 days\n"
            "• All slots eligible\n\n"
            "Ready to claim?"
        )
        keyboard = [
            [InlineKeyboardButton("🎁 Claim Bonus Now", url=PICKWIN_REGISTER)],
            [InlineKeyboardButton("📋 Full Terms", url=f"{PICKWIN_PROMOTIONS}/welcome")],
            [InlineKeyboardButton("⬅️ Back", callback_data='promotions')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    elif query.data == 'reload_bonus':
        text = (
            "🔄 **RELOAD BONUS** 🔄\n\n"
            "💎 **50% up to $250**\n"
            "Every deposit!\n\n"
            "**Available For:**\n"
            "✅ Existing players\n"
            "✅ All deposits after 1st\n"
            "✅ Use promo code: RELOAD50\n\n"
            "**Terms:**\n"
            "• Min deposit: $50\n"
            "• Max bonus: $250\n"
            "• Wagering: 25x\n\n"
            "Keep playing, keep winning! 🎰"
        )
        await query.edit_message_caption(
            caption=text,
            reply_markup=get_quick_action_keyboard(),
            parse_mode='Markdown'
        )
    
    elif query.data == 'free_spins':
        text = (
            "🎰 **FREE SPINS BONUSES** 🎰\n\n"
            "**Daily Free Spins:**\n"
            "• 20 Free Spins on deposit\n"
            "• Different game each day\n\n"
            "**Weekend Boost:**\n"
            "• 50 Free Spins\n"
            "• Deposit $100+ on weekends\n\n"
            "**VIP Free Spins:**\n"
            "• Up to 200 Free Spins\n"
            "• Exclusive for VIP members\n\n"
            "No wagering on first 20 spins! 🎉"
        )
        await query.edit_message_caption(
            caption=text,
            reply_markup=get_quick_action_keyboard(),
            parse_mode='Markdown'
        )
    
    elif query.data == 'cashback':
        text = (
            "💸 **CASHBACK PROGRAM** 💸\n\n"
            "**Weekly Cashback:**\n"
            "Get back 10% of losses\n"
            "• Calculated every Monday\n"
            "• No wagering requirements\n"
            "• Instant credit to account\n\n"
            "**VIP Cashback:**\n"
            "• Bronze: 10%\n"
            "• Silver: 12%\n"
            "• Gold: 15%\n"
            "• Platinum: 20%\n\n"
            "The more you play, the more you get back! 🎁"
        )
        await query.edit_message_caption(
            caption=text,
            reply_markup=get_quick_action_keyboard(),
            parse_mode='Markdown'
        )
    
    # VIP INFO
    elif query.data == 'vip_info':
        text = (
            "👑 **VIP CLUB** 👑\n\n"
            "Exclusive benefits for our valued players:\n\n"
            "💎 **VIP Tiers:**\n"
            "🥉 Bronze - $1,000 wagered\n"
            "🥈 Silver - $10,000 wagered\n"
            "🥇 Gold - $50,000 wagered\n"
            "💎 Platinum - $250,000 wagered\n\n"
            "🎁 **VIP Benefits:**\n"
            "• Higher cashback rates\n"
            "• Exclusive bonuses\n"
            "• Personal account manager\n"
            "• Faster withdrawals\n"
            "• Birthday bonuses\n"
            "• Special tournament access\n"
            "• Luxury gifts\n\n"
            "Start playing to unlock VIP status!"
        )
        keyboard = [
            [InlineKeyboardButton("🏆 Join VIP Club", url=PICKWIN_VIP)],
            [InlineKeyboardButton("⬅️ Back", callback_data='back_main')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    # PAYMENT INFO
    elif query.data == 'crypto_info':
        text = (
            "🟠 **CRYPTO PAYMENTS** 🟠\n\n"
            "⚡ **Fast & Secure**\n\n"
            "**Accepted Cryptocurrencies:**\n"
            "• Bitcoin (BTC)\n"
            "• Ethereum (ETH)\n"
            "• Tether (USDT)\n"
            "• Litecoin (LTC)\n"
            "• Bitcoin Cash (BCH)\n\n"
            "💰 **Benefits:**\n"
            "✅ Instant deposits\n"
            "✅ Withdrawals in 5-15 minutes\n"
            "✅ No fees\n"
            "✅ Enhanced privacy\n"
            "✅ Higher limits\n\n"
            "**Withdrawal Speed:**\n"
            "🚀 Crypto: 5-15 mins\n"
            "vs\n"
            "🐌 Bank: 3-5 days"
        )
        keyboard = [
            [InlineKeyboardButton("💰 Deposit Crypto Now", url=PICKWIN_CASHIER)],
            [InlineKeyboardButton("⬅️ Back", callback_data='back_main')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    elif query.data == 'withdrawal_info':
        text = (
            "💰 **WITHDRAWAL INFORMATION** 💰\n\n"
            "**Withdrawal Methods:**\n"
            "🟠 Crypto: 5-15 minutes ⚡\n"
            "💳 E-Wallets: 24 hours\n"
            "🏦 Bank Transfer: 3-5 days\n\n"
            "**Withdrawal Limits:**\n"
            "• Min: $20\n"
            "• Max: $5,000/day (standard)\n"
            "• VIP: Up to $50,000/day\n\n"
            "**Requirements:**\n"
            "✅ Account verified (KYC)\n"
            "✅ Wagering completed\n"
            "✅ Same method as deposit\n\n"
            "**First Withdrawal?**\n"
            "You'll need to verify your identity.\n"
            "Takes 2-5 minutes. ⚡"
        )
        keyboard = [
            [InlineKeyboardButton("💸 Request Withdrawal", url=f"{PICKWIN_CASHIER}/withdraw")],
            [InlineKeyboardButton("📋 KYC Verification", callback_data='kyc_info')],
            [InlineKeyboardButton("⬅️ Back", callback_data='back_main')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    elif query.data == 'kyc_info':
        text = (
            "🔐 **ACCOUNT VERIFICATION (KYC)** 🔐\n\n"
            "**Required by law for your protection**\n\n"
            "📋 **What You Need:**\n"
            "• Valid ID or Passport\n"
            "• Proof of Address (utility bill)\n"
            "• Selfie with ID\n\n"
            "⚡ **Quick Process:**\n"
            "1️⃣ Upload documents\n"
            "2️⃣ Automatic verification\n"
            "3️⃣ Approved in 2-5 minutes\n\n"
            "🔒 **Why KYC?**\n"
            "✅ Prevents fraud\n"
            "✅ Protects your account\n"
            "✅ Ensures secure withdrawals\n"
            "✅ Required by gaming license\n"
            "✅ Prevents underage gambling\n\n"
            "Your data is encrypted and secure. 🛡️"
        )
        keyboard = [
            [InlineKeyboardButton("📸 Start Verification", url=f"{PICKWIN_BASE}/verification")],
            [InlineKeyboardButton("⬅️ Back", callback_data='withdrawal_info')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    # SUPPORT
    elif query.data == 'support':
        await show_support_menu(query)
    
    elif query.data == 'email_support':
        text = (
            "📧 **EMAIL SUPPORT** 📧\n\n"
            "**Contact Us:**\n"
            "📩 support@pickwin.fun\n\n"
            "**Response Time:**\n"
            "⏱️ Usually within 2-4 hours\n\n"
            "**What to Include:**\n"
            "• Your username\n"
            "• Detailed description\n"
            "• Screenshots (if applicable)\n"
            "• Transaction IDs\n\n"
            "💬 **Need faster help?**\n"
            "Use our 24/7 Live Chat!\n"
            "Response time: < 2 minutes"
        )
        keyboard = [
            [InlineKeyboardButton("💬 Live Chat", url=f"{PICKWIN_SUPPORT}/chat")],
            [InlineKeyboardButton("⬅️ Back", callback_data='support')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    elif query.data == 'faq':
        text = (
            "❓ **FREQUENTLY ASKED QUESTIONS** ❓\n\n"
            "**Account:**\n"
            "• How to register?\n"
            "• How to verify account?\n"
            "• Forgot password?\n\n"
            "**Payments:**\n"
            "• How to deposit?\n"
            "• Withdrawal times?\n"
            "• Payment methods?\n\n"
            "**Bonuses:**\n"
            "• How to claim bonus?\n"
            "• Wagering requirements?\n"
            "• Bonus terms?\n\n"
            "**Games:**\n"
            "• Game providers?\n"
            "• RTP information?\n"
            "• Mobile gaming?\n\n"
            "Click below for full FAQ database:"
        )
        keyboard = [
            [InlineKeyboardButton("📖 View Full FAQ", url=f"{PICKWIN_BASE}/faq")],
            [InlineKeyboardButton("💬 Ask Live Agent", url=f"{PICKWIN_SUPPORT}/chat")],
            [InlineKeyboardButton("⬅️ Back", callback_data='support')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    # RESPONSIBLE GAMBLING
    elif query.data == 'responsible_gambling':
        await show_responsible_gambling_menu(query)
    
    elif query.data == 'self_exclusion':
        text = (
            "🛑 **SELF-EXCLUSION** 🛑\n\n"
            "Take control of your gaming:\n\n"
            "**Options:**\n"
            "⏸️ **Take a Break**\n"
            "• 24 hours\n"
            "• 7 days\n"
            "• 30 days\n\n"
            "🔒 **Self-Exclusion**\n"
            "• 6 months\n"
            "• 1 year\n"
            "• 5 years\n"
            "• Permanent\n\n"
            "**What Happens:**\n"
            "• Account locked during period\n"
            "• No deposits allowed\n"
            "• Marketing emails stopped\n"
            "• Can withdraw remaining balance\n\n"
            "We support responsible gaming. 💚"
        )
        keyboard = [
            [InlineKeyboardButton("🛑 Set Self-Exclusion", url=f"{PICKWIN_BASE}/responsible-gaming/exclusion")],
            [InlineKeyboardButton("⬅️ Back", callback_data='responsible_gambling')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    elif query.data == 'help_resources':
        text = (
            "📞 **GAMBLING HELP RESOURCES** 📞\n\n"
            "If you or someone you know needs help:\n\n"
            "🌐 **International:**\n"
            "• GamCare: www.gamcare.org.uk\n"
            "• Gambling Therapy: www.gamblingtherapy.org\n\n"
            "🇺🇸 **USA:**\n"
            "• National Council on Problem Gambling\n"
            "• 1-800-522-4700\n\n"
            "🇬🇧 **UK:**\n"
            "• BeGambleAware: 0808 8020 133\n\n"
            "🇨🇦 **Canada:**\n"
            "• Responsible Gambling Council\n"
            "• 1-888-391-1111\n\n"
            "You're not alone. Help is available 24/7. 💚"
        )
        await query.edit_message_caption(
            caption=text,
            reply_markup=get_back_button(),
            parse_mode='Markdown'
        )
    
    # HELP / INFO
    elif query.data == 'help':
        text = (
            "❓ **HELP CENTER** ❓\n\n"
            "**Quick Links:**\n\n"
            "🎮 **Getting Started:**\n"
            "• How to register\n"
            "• How to deposit\n"
            "• How to play games\n\n"
            "💰 **Payments:**\n"
            "• Deposit methods\n"
            "• Withdrawal guide\n"
            "• Payment times\n\n"
            "🎁 **Bonuses:**\n"
            "• Welcome bonus guide\n"
            "• Bonus terms explained\n"
            "• How to claim promos\n\n"
            "🛡️ **Account Security:**\n"
            "• KYC verification\n"
            "• 2FA setup\n"
            "• Password reset\n\n"
            "Need more help? Contact us!"
        )
        keyboard = [
            [InlineKeyboardButton("📖 Full Help Center", url=f"{PICKWIN_BASE}/help")],
            [InlineKeyboardButton("💬 Live Support", url=f"{PICKWIN_SUPPORT}/chat")],
            [InlineKeyboardButton("⬅️ Back", callback_data='back_main')]
        ]
        await query.edit_message_caption(
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    # ACCOUNT ACTIONS
    elif query.data == 'my_account':
        await show_account_menu(query)

# Helper functions to show menus
async def show_main_menu(query, context):
    """Show main menu"""
    user = query.from_user
    text = (
        f"🎰 **PickWin Casino** 🎰\n\n"
        f"Welcome back, {user.first_name}! 👋\n\n"
        f"🎁 **Active Promotions:**\n"
        f"• $500 Welcome Bonus\n"
        f"• Daily Free Spins\n"
        f"• Weekend Cashback\n\n"
        f"Choose an option:"
    )
    await query.edit_message_caption(
        caption=text,
        reply_markup=get_main_menu(),
        parse_mode='Markdown'
    )

async def show_promotions_menu(query):
    """Show promotions menu"""
    text = (
        "🎁 **PROMOTIONS & BONUSES** 🎁\n\n"
        "**Available Now:**\n\n"
        "🌟 **Welcome Bonus**\n"
        "100% up to $500 + Free Spins\n\n"
        "💎 **VIP Rewards**\n"
        "Exclusive bonuses for VIP members\n\n"
        "🔄 **Reload Bonus**\n"
        "50% up to $250 on every deposit\n\n"
        "🎰 **Free Spins**\n"
        "Daily & weekly free spin offers\n\n"
        "💸 **Cashback**\n"
        "Get 10-20% back on losses\n\n"
        "Select a promotion for details:"
    )
    await query.edit_message_caption(
        caption=text,
        reply_markup=get_promotions_menu(),
        parse_mode='Markdown'
    )

async def show_support_menu(query):
    """Show support menu"""
    text = (
        "💬 **CUSTOMER SUPPORT** 💬\n\n"
        "We're here to help 24/7!\n\n"
        "**Contact Options:**\n\n"
        "💬 **Live Chat**\n"
        "Instant help, average response: 2 min\n\n"
        "📧 **Email**\n"
        "support@pickwin.fun\n"
        "Response: 2-4 hours\n\n"
        "❓ **FAQ**\n"
        "Instant answers to common questions\n\n"
        "Choose your preferred contact method:"
    )
    await query.edit_message_caption(
        caption=text,
        reply_markup=get_support_menu(),
        parse_mode='Markdown'
    )

async def show_responsible_gambling_menu(query):
    """Show responsible gambling menu"""
    text = (
        "🛡️ **RESPONSIBLE GAMBLING** 🛡️\n\n"
        "Your wellbeing is important to us.\n\n"
        "**Tools Available:**\n\n"
        "⏰ **Deposit Limits**\n"
        "Set daily, weekly, or monthly limits\n\n"
        "🛑 **Self-Exclusion**\n"
        "Take a break from gaming\n\n"
        "📊 **Activity History**\n"
        "Track your gaming patterns\n\n"
        "📞 **Get Help**\n"
        "24/7 support resources\n\n"
        "Remember: Gambling should be fun! 💚\n"
        "Play responsibly."
    )
    await query.edit_message_caption(
        caption=text,
        reply_markup=get_responsible_gambling_menu(),
        parse_mode='Markdown'
    )

async def show_account_menu(query):
    """Show account management menu"""
    text = (
        "👤 **ACCOUNT MANAGEMENT** 👤\n\n"
        "**Quick Actions:**\n\n"
        "🔐 **Login / Register**\n"
        "Access your account\n\n"
        "💰 **Cashier**\n"
        "Deposits & withdrawals\n\n"
        "🎁 **My Bonuses**\n"
        "View active & available bonuses\n\n"
        "⚙️ **Account Settings**\n"
        "Update profile & preferences\n\n"
        "Select an option:"
    )
    await query.edit_message_caption(
        caption=text,
        reply_markup=get_account_menu(),
        parse_mode='Markdown'
    )

# --- Message Handlers ---

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages with smart responses"""
    text = update.message.text.lower()
    
    # Check for common intents
    if any(word in text for word in ['login', 'log in', 'sign in', 'signin']):
        response = (
            "🔐 **Login to Your Account**\n\n"
            "Click the button below to access your PickWin account:\n\n"
            "Don't have an account yet?\n"
            "Register now and get $500 bonus! 🎁"
        )
        keyboard = [
            [InlineKeyboardButton("🔐 Login Now", url=PICKWIN_LOGIN)],
            [InlineKeyboardButton("✨ Register", url=PICKWIN_REGISTER)],
            [InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')]
        ]
        await update.message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        return
    
    elif any(word in text for word in ['register', 'sign up', 'signup', 'join', 'create account']):
        response = (
            "✨ **Create Your Account** ✨\n\n"
            "🎁 **Welcome Bonus Waiting!**\n"
            "Get 100% up to $500 on first deposit\n\n"
            "**Registration takes 30 seconds:**\n"
            "1️⃣ Click 'Register Now'\n"
            "2️⃣ Fill in basic details\n"
            "3️⃣ Verify email\n"
            "4️⃣ Start playing!\n\n"
            "Ready to join?"
        )
        keyboard = [
            [InlineKeyboardButton("🎁 Register & Get $500", url=PICKWIN_REGISTER)],
            [InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')]
        ]
        await update.message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        return
    
    elif any(word in text for word in ['deposit', 'add money', 'fund', 'cashier']):
        response = (
            "💰 **Make a Deposit** 💰\n\n"
            "**Quick & Secure:**\n"
            "🟠 Crypto - Instant\n"
            "💳 Cards - Instant\n"
            "💵 E-Wallets - Instant\n\n"
            "**Minimum:** $20\n"
            "**Maximum:** $10,000\n\n"
            "🎁 First deposit? Get 100% bonus!"
        )
        keyboard = [
            [InlineKeyboardButton("💰 Deposit Now", url=PICKWIN_CASHIER)],
            [InlineKeyboardButton("💳 Payment Methods", callback_data='crypto_info')],
            [InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')]
        ]
        await update.message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        return
    
    elif any(word in text for word in ['withdraw', 'withdrawal', 'cashout', 'cash out']):
        response = (
            "💸 **Withdraw Your Winnings** 💸\n\n"
            "**Withdrawal Times:**\n"
            "⚡ Crypto: 5-15 minutes\n"
            "💳 E-Wallets: 24 hours\n"
            "🏦 Bank: 3-5 days\n\n"
            "**First withdrawal?**\n"
            "Quick verification required (2-5 min)\n\n"
            "Ready to cash out?"
        )
        keyboard = [
            [InlineKeyboardButton("💸 Request Withdrawal", url=f"{PICKWIN_CASHIER}/withdraw")],
            [InlineKeyboardButton("📋 Withdrawal Info", callback_data='withdrawal_info')],
            [InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')]
        ]
        await update.message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        return
    
    elif any(word in text for word in ['bonus', 'promo', 'promotion', 'offer', 'free']):
        response = (
            "🎁 **Available Bonuses** 🎁\n\n"
            "💰 **Welcome Bonus**\n"
            "100% up to $500\n\n"
            "🔄 **Reload Bonus**\n"
            "50% up to $250\n\n"
            "🎰 **Free Spins**\n"
            "Daily offers\n\n"
            "💸 **Cashback**\n"
            "10-20% weekly\n\n"
            "Claim yours now!"
        )
        keyboard = [
            [InlineKeyboardButton("🎁 View All Promotions", callback_data='promotions')],
            [InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')]
        ]
        await update.message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        return
    
    elif any(word in text for word in ['help', 'support', 'contact', 'problem', 'issue']):
        response = (
            "💬 **Need Help?** 💬\n\n"
            "We're here 24/7!\n\n"
            "**Fastest Help:**\n"
            "💬 Live Chat - Instant response\n\n"
            "**Other Options:**\n"
            "📧 Email: support@pickwin.fun\n"
            "❓ FAQ: Instant answers\n\n"
            "How can we assist you?"
        )
        keyboard = [
            [InlineKeyboardButton("💬 Live Chat Now", url=f"{PICKWIN_SUPPORT}/chat")],
            [InlineKeyboardButton("❓ FAQ", callback_data='faq')],
            [InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')]
        ]
        await update.message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        return
    
    elif any(word in text for word in ['game', 'games', 'play', 'slot', 'slots', 'casino']):
        response = (
            "🎮 **Play Now!** 🎮\n\n"
            "**4,000+ Games Available:**\n"
            "🎰 Slots\n"
            "🎲 Live Casino\n"
            "⚽ Sports Betting\n\n"
            "**Popular Games:**\n"
            "• Sweet Bonanza 1000\n"
            "• Big Bass Bonanza\n"
            "• Lightning Roulette\n"
            "• Crazy Time\n\n"
            "Start playing now!"
        )
        keyboard = [
            [InlineKeyboardButton("🎮 Play Now", web_app=WebAppInfo(url=PICKWIN_BASE))],
            [InlineKeyboardButton("🎰 Browse Games", callback_data='games_menu')],
            [InlineKeyboardButton("⬅️ Main Menu", callback_data='back_main')]
        ]
        await update.message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        return
    
    # Default response for unrecognized messages
    user = update.effective_user
    default_response = (
        f"👋 Hey {user.first_name}!\n\n"
        f"I can help you with:\n\n"
        f"🔐 Login / Registration\n"
        f"💰 Deposits & Withdrawals\n"
        f"🎁 Bonuses & Promotions\n"
        f"🎮 Games & Betting\n"
        f"💬 Support & Help\n\n"
        f"Use the menu below or type what you need! 👇"
    )
    await update.message.reply_text(
        default_response,
        reply_markup=get_main_menu(),
        parse_mode='Markdown'
    )

# --- Error Handler ---

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Log errors and handle gracefully"""
    logger.error(f'Update {update} caused error {context.error}')
    
    if isinstance(context.error, BadRequest):
        error_message = str(context.error)
        if "Message can't be deleted" in error_message:
            logger.warning("Attempted to delete old message - ignoring")
            return
        if "Message is not modified" in error_message:
            logger.warning("Message unchanged - ignoring")
            return
    
    if isinstance(context.error, (TimedOut, NetworkError)):
        logger.warning(f"Network error: {context.error}")
        return

# --- Main Bot Execution ---

def main():
    """Start the bot"""
    application = Application.builder().token(API_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
    application.add_error_handler(error_handler)
    
    logger.info("🎰 PickWin Casino Bot is running...")
    print("🎰 PickWin Casino Bot is running... Press Ctrl+C to stop")
    
    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
