"""
PickWin Casino Bot - Handlers
All callback and message handling functions
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram.error import BadRequest

import config
import keyboards
import utils

logger = logging.getLogger(__name__)

# ============================================================================
# COMMAND HANDLERS
# ============================================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    # Initialize user session
    utils.init_user_session(context, user.id)
    utils.track_interaction(context, 'start')
    
    # Get random main menu image
    image_url = utils.get_random_image('main')
    
    # Format welcome text with user's name
    welcome_text = config.WELCOME_TEXT.format(name=user.first_name)
    
    # Send welcome message with image
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=image_url,
        caption=welcome_text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_main_menu()
    )
    
    logger.info(f"User {user.id} ({user.first_name}) started the bot")

# ============================================================================
# CALLBACK QUERY HANDLERS
# ============================================================================

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all button callbacks"""
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    utils.track_interaction(context, f'callback_{callback_data}')
    
    try:
        # ============= MAIN NAVIGATION =============
        if callback_data == 'back_main':
            await show_main_menu(query, context)
        
        # ============= CASINO =============
        elif callback_data == 'casino_menu':
            await show_casino_menu(query, context)
        
        # ============= SPORTS =============
        elif callback_data == 'sports_menu':
            await show_sports_menu(query, context)
        
        # ============= PROMOTIONS =============
        elif callback_data == 'promotions_menu':
            await show_promotions_menu(query, context)
        
        elif callback_data == 'promo_welcome':
            await show_welcome_bonus(query, context)
        
        elif callback_data == 'promo_reload':
            await show_reload_bonus(query, context)
        
        elif callback_data == 'promo_freespins':
            await show_free_spins(query, context)
        
        elif callback_data == 'promo_cashback':
            await show_cashback(query, context)
        
        elif callback_data == 'promo_vip':
            await show_vip_program(query, context)
        
        # ============= ACCOUNT =============
        elif callback_data == 'account_menu':
            await show_account_menu(query, context)
        
        elif callback_data == 'vip_info':
            await show_vip_program(query, context)
        
        # ============= SUPPORT =============
        elif callback_data == 'support_menu':
            await show_support_menu(query, context)
        
        elif callback_data == 'support_email':
            await show_email_support(query, context)
        
        elif callback_data == 'responsible_gaming':
            await show_responsible_gaming(query, context)
        
        elif callback_data == 'help_resources':
            await show_help_resources(query, context)
        
        # ============= HELP =============
        elif callback_data == 'help_menu':
            await show_help_menu(query, context)
        
        elif callback_data == 'help_payments':
            await show_payment_info(query, context)
        
        elif callback_data == 'help_bonuses':
            await show_bonus_guide(query, context)
        
        elif callback_data == 'help_kyc':
            await show_kyc_info(query, context)
        
        elif callback_data == 'help_withdrawals':
            await show_withdrawal_info(query, context)
        
        elif callback_data == 'payment_crypto':
            await show_crypto_info(query, context)
        
        elif callback_data == 'payment_cards':
            await show_card_info(query, context)
        
        else:
            logger.warning(f"Unknown callback data: {callback_data}")
    
    except BadRequest as e:
        if utils.is_message_too_old_error(e):
            logger.warning("Message too old to edit, ignoring")
        elif utils.is_message_not_modified_error(e):
            logger.warning("Message content unchanged, ignoring")
        else:
            logger.error(f"BadRequest error: {e}")
    except Exception as e:
        logger.error(f"Error in button_callback: {e}")
        utils.log_error(e, update)

# ============================================================================
# MENU DISPLAY FUNCTIONS
# ============================================================================

async def show_main_menu(query, context):
    """Display main menu"""
    user = query.from_user
    image_url = utils.get_random_image('main')
    text = config.WELCOME_TEXT.format(name=user.first_name)
    
    try:
        # Try to edit the existing message
        await query.edit_message_media(
            media=f"photo:{image_url}",
            caption=text,
            parse_mode='Markdown',
            reply_markup=keyboards.get_main_menu()
        )
    except:
        # If edit fails, send new message
        await query.message.reply_photo(
            photo=image_url,
            caption=text,
            parse_mode='Markdown',
            reply_markup=keyboards.get_main_menu()
        )

async def show_casino_menu(query, context):
    """Display casino menu"""
    image_url = utils.get_random_image('casino')
    
    try:
        await query.edit_message_media(
            media=f"photo:{image_url}",
            caption=config.CASINO_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_casino_menu()
        )
    except:
        await query.message.reply_photo(
            photo=image_url,
            caption=config.CASINO_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_casino_menu()
        )

async def show_sports_menu(query, context):
    """Display sports menu"""
    image_url = utils.get_random_image('sports')
    
    try:
        await query.edit_message_media(
            media=f"photo:{image_url}",
            caption=config.SPORTS_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_sports_menu()
        )
    except:
        await query.message.reply_photo(
            photo=image_url,
            caption=config.SPORTS_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_sports_menu()
        )

async def show_promotions_menu(query, context):
    """Display promotions menu"""
    image_url = utils.get_random_image('promotions')
    
    try:
        await query.edit_message_media(
            media=f"photo:{image_url}",
            caption=config.PROMOTIONS_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_promotions_menu()
        )
    except:
        await query.message.reply_photo(
            photo=image_url,
            caption=config.PROMOTIONS_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_promotions_menu()
        )

async def show_account_menu(query, context):
    """Display account menu"""
    image_url = utils.get_random_image('account')
    
    try:
        await query.edit_message_media(
            media=f"photo:{image_url}",
            caption=config.ACCOUNT_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_account_menu()
        )
    except:
        await query.message.reply_photo(
            photo=image_url,
            caption=config.ACCOUNT_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_account_menu()
        )

async def show_support_menu(query, context):
    """Display support menu"""
    image_url = utils.get_random_image('account')
    
    try:
        await query.edit_message_caption(
            caption=config.SUPPORT_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_support_menu()
        )
    except:
        await query.message.reply_text(
            text=config.SUPPORT_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_support_menu()
        )

async def show_help_menu(query, context):
    """Display help menu"""
    text = """❓ **HELP CENTER** ❓

**Quick Links:**

🎮 **Getting Started:**
• How to register
• How to deposit
• How to play games

💰 **Payments:**
• Deposit methods
• Withdrawal guide
• Payment times

🎁 **Bonuses:**
• Welcome bonus guide
• Bonus terms explained
• How to claim promos

🛡️ **Account Security:**
• KYC verification
• 2FA setup
• Password reset

Select a topic:"""
    
    try:
        await query.edit_message_caption(
            caption=text,
            parse_mode='Markdown',
            reply_markup=keyboards.get_help_menu()
        )
    except:
        await query.message.reply_text(
            text=text,
            parse_mode='Markdown',
            reply_markup=keyboards.get_help_menu()
        )

# ============================================================================
# DETAILED INFORMATION DISPLAYS
# ============================================================================

async def show_welcome_bonus(query, context):
    """Show welcome bonus details"""
    text = utils.format_welcome_bonus_details()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_welcome_bonus_keyboard()
    )

async def show_reload_bonus(query, context):
    """Show reload bonus details"""
    text = utils.format_reload_bonus_details()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_promo_action_keyboard('reload')
    )

async def show_free_spins(query, context):
    """Show free spins details"""
    text = utils.format_free_spins_details()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_promo_action_keyboard('freespins')
    )

async def show_cashback(query, context):
    """Show cashback details"""
    text = utils.format_cashback_details()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_promo_action_keyboard('cashback')
    )

async def show_vip_program(query, context):
    """Show VIP program details"""
    text = utils.format_vip_program_details()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_promo_action_keyboard('vip')
    )

async def show_email_support(query, context):
    """Show email support info"""
    text = utils.format_email_support_info()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_back_to_main_button()
    )

async def show_responsible_gaming(query, context):
    """Show responsible gaming options"""
    text = """🛡️ **RESPONSIBLE GAMBLING** 🛡️

Your wellbeing is important to us.

**Tools Available:**

⏰ **Deposit Limits**
Set daily, weekly, or monthly limits

🛑 **Self-Exclusion**
Take a break from gaming (24h to permanent)

📊 **Activity History**
Track your gaming patterns

📞 **Get Help**
24/7 support resources

Remember: Gambling should be fun! 💚
Play responsibly."""
    
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_responsible_gaming_keyboard()
    )

async def show_help_resources(query, context):
    """Show gambling help resources"""
    text = utils.format_help_resources()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_back_to_main_button()
    )

async def show_payment_info(query, context):
    """Show payment methods info"""
    text = """💰 **PAYMENT METHODS** 💰

We offer multiple secure payment options:

**Cryptocurrencies** 🟠
• Bitcoin, Ethereum, Tether, etc.
• Instant deposits
• Withdrawals in 5-15 minutes
• No fees

**Credit/Debit Cards** 💳
• Visa, Mastercard, Maestro
• Instant deposits
• Withdrawals in 1-3 days

**E-Wallets** 💵
• PayPal, Skrill, Neteller
• Instant deposits
• Fast withdrawals

Select for more details:"""
    
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_payment_info_keyboard()
    )

async def show_bonus_guide(query, context):
    """Show bonus guide"""
    await show_welcome_bonus(query, context)

async def show_kyc_info(query, context):
    """Show KYC verification info"""
    text = utils.format_kyc_info()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_back_to_main_button()
    )

async def show_withdrawal_info(query, context):
    """Show withdrawal info"""
    text = utils.format_withdrawal_info()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_back_to_main_button()
    )

async def show_crypto_info(query, context):
    """Show cryptocurrency info"""
    text = utils.format_crypto_payment_info()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_payment_info_keyboard()
    )

async def show_card_info(query, context):
    """Show card payment info"""
    text = utils.format_card_payment_info()
    await query.edit_message_caption(
        caption=text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_payment_info_keyboard()
    )

# ============================================================================
# MESSAGE HANDLERS
# ============================================================================

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages from users"""
    text = update.message.text.lower()
    user = update.effective_user
    
    utils.track_interaction(context, f'message_{text[:20]}')
    
    # Casino-related keywords
    if any(word in text for word in ['casino', 'slot', 'slots', 'games', 'play']):
        image_url = utils.get_random_image('casino')
        await update.message.reply_photo(
            photo=image_url,
            caption=config.CASINO_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_casino_menu()
        )
        return
    
    # Sports-related keywords
    if any(word in text for word in ['sport', 'sports', 'bet', 'betting', 'football', 'soccer', 'basketball']):
        image_url = utils.get_random_image('sports')
        await update.message.reply_photo(
            photo=image_url,
            caption=config.SPORTS_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_sports_menu()
        )
        return
    
    # Bonus/promo keywords
    if any(word in text for word in ['bonus', 'promo', 'promotion', 'offer', 'free']):
        image_url = utils.get_random_image('promotions')
        await update.message.reply_photo(
            photo=image_url,
            caption=config.PROMOTIONS_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_promotions_menu()
        )
        return
    
    # Support/help keywords
    if any(word in text for word in ['help', 'support', 'problem', 'issue', 'question']):
        await update.message.reply_text(
            text=config.SUPPORT_TEXT,
            parse_mode='Markdown',
            reply_markup=keyboards.get_support_menu()
        )
        return
    
    # Default response - show main menu
    image_url = utils.get_random_image('main')
    response_text = f"""👋 Hey {user.first_name}!

I can help you with:

🎰 **Casino Games**
⚽ **Sports Betting**
🎁 **Bonuses & Promotions**
👤 **Account Management**
💬 **Support & Help**

Use the menu below or tell me what you need!"""
    
    await update.message.reply_photo(
        photo=image_url,
        caption=response_text,
        parse_mode='Markdown',
        reply_markup=keyboards.get_main_menu()
    )

# ============================================================================
# ERROR HANDLER
# ============================================================================

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f'Update {update} caused error {context.error}')
    utils.log_error(context.error, update)
