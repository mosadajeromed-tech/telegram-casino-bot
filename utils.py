"""
PickWin Casino Bot - Utility Functions
Helper functions for bot operations
"""

import random
import logging
from datetime import datetime
from config import IMAGES

logger = logging.getLogger(__name__)

# ============================================================================
# IMAGE SELECTION
# ============================================================================

def get_random_image(menu_type='main'):
    """
    Get a random image for the specified menu type
    
    Args:
        menu_type (str): Type of menu ('main', 'casino', 'sports', 'promotions', 'account')
    
    Returns:
        str: URL of a random image for that menu
    """
    if menu_type in IMAGES:
        return random.choice(IMAGES[menu_type])
    # Fallback to main images if menu type not found
    return random.choice(IMAGES['main'])

# ============================================================================
# SESSION TRACKING
# ============================================================================

def init_user_session(context, user_id):
    """Initialize user session data"""
    if 'session_start' not in context.user_data:
        context.user_data['session_start'] = datetime.now()
        context.user_data['user_id'] = user_id
        context.user_data['interactions'] = 0
        logger.info(f"New session initialized for user {user_id}")

def track_interaction(context, interaction_type):
    """Track user interactions"""
    context.user_data['interactions'] = context.user_data.get('interactions', 0) + 1
    context.user_data['last_interaction'] = datetime.now()
    context.user_data['last_action'] = interaction_type
    logger.info(f"User interaction: {interaction_type}")

# ============================================================================
# TEXT FORMATTING
# ============================================================================

def format_currency(amount):
    """Format currency amounts"""
    if isinstance(amount, str):
        return amount
    return f"${amount:,.2f}"

def format_percentage(percentage):
    """Format percentage values"""
    if isinstance(percentage, str):
        return percentage
    return f"{percentage}%"

# ============================================================================
# BONUS INFORMATION FORMATTING
# ============================================================================

def format_welcome_bonus_details():
    """Format welcome bonus information"""
    from config import WELCOME_BONUS
    
    text = f"""🎁 **WELCOME BONUS** 🎁

💰 **{WELCOME_BONUS['percentage']} up to {WELCOME_BONUS['amount']}**

**How It Works:**
1️⃣ Register your account
2️⃣ Make your first deposit
3️⃣ Get {WELCOME_BONUS['percentage']} bonus instantly!

**Example:**
Deposit $500 → Get $500 bonus
Total: $1,000 to play! 🎰

**Bonus Terms:**
• Minimum deposit: {WELCOME_BONUS['min_deposit']}
• Wagering: {WELCOME_BONUS['wagering']}
• Valid for: {WELCOME_BONUS['validity']}
• All slots eligible

Ready to claim?"""
    return text

def format_reload_bonus_details():
    """Format reload bonus information"""
    text = """🔄 **RELOAD BONUS** 🔄

💎 **50% up to $250**
Every deposit!

**Available For:**
✅ Existing players
✅ All deposits after 1st
✅ Use promo code: RELOAD50

**Terms:**
• Min deposit: $50
• Max bonus: $250
• Wagering: 25x
• Valid on all slots

Keep playing, keep winning! 🎰"""
    return text

def format_free_spins_details():
    """Format free spins information"""
    text = """🎰 **FREE SPINS BONUSES** 🎰

**Daily Free Spins:**
• 20 Free Spins on deposit
• Different game each day
• No wagering requirements!

**Weekend Boost:**
• 50 Free Spins
• Deposit $100+ on weekends
• Low 10x wagering

**VIP Free Spins:**
• Up to 200 Free Spins
• Exclusive for VIP members
• Wager-free!

Spin to win! 🎉"""
    return text

def format_cashback_details():
    """Format cashback program information"""
    text = """💸 **CASHBACK PROGRAM** 💸

**Weekly Cashback:**
Get back 10-20% of losses

• Calculated every Monday
• No wagering requirements
• Instant credit to account
• Based on net losses

**VIP Cashback Rates:**
• 🥉 Bronze: 10%
• 🥈 Silver: 12%
• 🥇 Gold: 15%
• 💎 Platinum: 20%

The more you play, the more you get back! 🎁"""
    return text

def format_vip_program_details():
    """Format VIP program information"""
    from config import VIP_TIERS
    
    text = """👑 **VIP PROGRAM** 👑

Exclusive benefits for valued players:

**VIP Tiers:**
"""
    for tier_key, tier in VIP_TIERS.items():
        text += f"\n{tier['name']} - Wager {tier['requirement']}\n"
        text += f"  • Cashback: {tier['cashback']}\n"
    
    text += """
**VIP Benefits:**
• Higher cashback rates
• Exclusive bonuses
• Personal account manager
• Faster withdrawals (priority)
• Birthday bonuses
• Special tournament access
• Luxury gifts & experiences

Start playing to unlock VIP status!"""
    return text

# ============================================================================
# PAYMENT INFORMATION FORMATTING
# ============================================================================

def format_crypto_payment_info():
    """Format cryptocurrency payment information"""
    from config import CRYPTO_CURRENCIES
    
    text = """🟠 **CRYPTO PAYMENTS** 🟠

⚡ **Fast & Secure**

**Accepted Cryptocurrencies:**
"""
    for crypto in CRYPTO_CURRENCIES:
        text += f"• {crypto}\n"
    
    text += """
💰 **Benefits:**
✅ Instant deposits
✅ Withdrawals in 5-15 minutes
✅ No fees
✅ Enhanced privacy
✅ Higher limits

**Withdrawal Speed Comparison:**
🚀 Crypto: 5-15 mins
vs
🐌 Bank: 3-5 days

Choose crypto for fastest gaming!"""
    return text

def format_card_payment_info():
    """Format card payment information"""
    text = """💳 **CARD PAYMENTS** 💳

**Accepted Cards:**
• Visa
• Mastercard
• Maestro

**Deposits:**
✅ Instant processing
✅ Min: $20
✅ Max: $5,000
✅ Secure 3D verification

**Withdrawals:**
⏱️ 1-3 business days
📋 Verification required
🔒 Same card as deposit

Safe and reliable payment method."""
    return text

def format_withdrawal_info():
    """Format withdrawal information"""
    text = """💰 **WITHDRAWAL INFORMATION** 💰

**Withdrawal Methods:**
🟠 Crypto: 5-15 minutes ⚡
💳 E-Wallets: 24 hours
💳 Cards: 1-3 days
🏦 Bank Transfer: 3-5 days

**Withdrawal Limits:**
• Min: $20
• Max: $5,000/day (standard)
• VIP: Up to $50,000/day

**Requirements:**
✅ Account verified (KYC)
✅ Wagering completed
✅ Same method as deposit

**First Withdrawal?**
You'll need to verify your identity.
Takes 2-5 minutes with our automated system."""
    return text

def format_kyc_info():
    """Format KYC verification information"""
    text = """🔐 **ACCOUNT VERIFICATION (KYC)** 🔐

**Required by law for your protection**

📋 **What You Need:**
• Valid ID or Passport
• Proof of Address (utility bill)
• Selfie with ID (for security)

⚡ **Quick Process:**
1️⃣ Upload documents via secure portal
2️⃣ Automatic verification system
3️⃣ Approved in 2-5 minutes
4️⃣ Start withdrawing!

🔒 **Why KYC?**
✅ Prevents fraud & identity theft
✅ Protects your account
✅ Ensures secure withdrawals
✅ Required by gaming license
✅ Prevents underage gambling

Your data is encrypted and never shared. 🛡️"""
    return text

# ============================================================================
# SUPPORT INFORMATION FORMATTING
# ============================================================================

def format_email_support_info():
    """Format email support information"""
    from config import SUPPORT_EMAIL
    
    text = f"""📧 **EMAIL SUPPORT** 📧

**Contact Us:**
📩 {SUPPORT_EMAIL}

**Response Time:**
⏱️ Usually within 2-4 hours
🚀 Urgent issues: < 1 hour

**What to Include:**
• Your username
• Detailed description
• Screenshots (if applicable)
• Transaction IDs
• Date and time of issue

💬 **Need faster help?**
Use our 24/7 Live Chat!
Response time: < 2 minutes"""
    return text

def format_help_resources():
    """Format gambling help resources"""
    from config import HELP_RESOURCES
    
    text = """📞 **GAMBLING HELP RESOURCES** 📞

If you or someone you know needs help:

🌐 **International:**
"""
    for org, url in HELP_RESOURCES['international'].items():
        text += f"• {org}: {url}\n"
    
    text += f"""
🇺🇸 **USA:**
• {HELP_RESOURCES['usa']['name']}
• {HELP_RESOURCES['usa']['phone']}

🇬🇧 **UK:**
• {HELP_RESOURCES['uk']['name']}
• {HELP_RESOURCES['uk']['phone']}

🇨🇦 **Canada:**
• {HELP_RESOURCES['canada']['name']}
• {HELP_RESOURCES['canada']['phone']}

You're not alone. Help is available 24/7. 💚

Remember: Gambling should be fun!
Play responsibly."""
    return text

# ============================================================================
# ERROR HANDLING
# ============================================================================

def log_error(error, update=None):
    """Log errors with context"""
    logger.error(f"Error occurred: {error}")
    if update:
        logger.error(f"Update: {update}")

def is_message_too_old_error(error):
    """Check if error is due to message being too old"""
    error_str = str(error).lower()
    return "can't be deleted" in error_str or "message can't be edited" in error_str

def is_message_not_modified_error(error):
    """Check if error is due to message not being modified"""
    return "message is not modified" in str(error).lower()
