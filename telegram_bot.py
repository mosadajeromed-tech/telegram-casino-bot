import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from telegram.error import BadRequest, TimedOut, NetworkError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Basic Setup ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Secure token from environment variable (set BOT_TOKEN in your env or .env file)
API_TOKEN = os.environ.get('BOT_TOKEN')
if not API_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# --- Keyboard Layouts ---
# Main menu keyboard with the "glowing" bonus button
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("✨ Claim Your Bonus! ✨", callback_data='bonus_start')],
        [InlineKeyboardButton("🎮 Mini App", web_app=WebAppInfo(url='https://bet88.ph/en/'))],  # Replace with real URL if needed
        [InlineKeyboardButton("❓ Help & Info", callback_data='help')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Player type selection
def get_player_type_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎯 Beginner Player (Low Deposit)", callback_data='player_beginner')],
        [InlineKeyboardButton("💎 High Roller (Large Deposit)", callback_data='player_highroller')],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Account check keyboard
def get_account_check_keyboard():
    keyboard = [
        [InlineKeyboardButton("✅ Yes, I have an account", callback_data='has_account_yes')],
        [InlineKeyboardButton("❌ No, I need to create one", callback_data='has_account_no')],
        [InlineKeyboardButton("⬅️ Back", callback_data='bonus_start')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Verification ready keyboard
def get_verification_keyboard():
    keyboard = [
        [InlineKeyboardButton("✅ Yes, my account is ready!", callback_data='account_ready_yes')],
        [InlineKeyboardButton("🔄 Show tutorials again", callback_data='show_tutorials')],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Back to menu button
def get_back_button():
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_main')]]
    return InlineKeyboardMarkup(keyboard)

# Status menu keyboard
def get_status_menu():
    keyboard = [
        [InlineKeyboardButton("✅ Check Status", callback_data='check_status')],
        [InlineKeyboardButton("🔄 Start New Request", callback_data='restart_fresh')],
        [InlineKeyboardButton("❓ Help & Info", callback_data='help')]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- Command Handlers ---
# /start command - Sends an image with a caption and keyboard
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This function handles both /start command and direct text messages.
    # It determines the chat ID from either the message or the callback query.
    chat_id = update.effective_chat.id
    user = update.effective_user
    if not user:
        return  # Safety check
    # Check if user has pending verification
    waiting_for = context.user_data.get('waiting_for')
    if waiting_for == 'pending_verification':
        # User has pending request - show status
        submitted_id = context.user_data.get('submitted_id', 'N/A')
        submitted_username = context.user_data.get('submitted_username', 'N/A')
        status_text = (
            f"👋 **Welcome back, {user.first_name}!**\n\n"
            "⏳ **You have a pending verification request**\n\n"
            "📋 **Your Submission:**\n"
        )
        if submitted_id != 'N/A':
            status_text += f"• Account ID: `{submitted_id}`\n"
        if submitted_username != 'N/A':
            status_text += f"• Username: `{submitted_username}`\n"
        status_text += (
            "\n🎁 Our team is processing your bonus request!\n\n"
            "💬 You'll receive a notification when ready.\n\n"
            "What would you like to do?"
        )
        image_url = 'https://fireart.studio/wp-content/uploads/2021/09/9-145.jpg'
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=image_url,
            caption=status_text,
            parse_mode='Markdown',
            reply_markup=get_status_menu()
        )
    else:
        # Normal welcome message
        welcome_text = (
            f"🎰 **Welcome to PickWin Casino Bot!** 🎰\n\n"
            f"Hey {user.first_name}! 👋\n\n"
            f"I'm here to help you get started with exclusive bonuses, "
            f"account setup, and more!\n\n"
            f"Choose an option below to continue:"
        )
        image_url = 'https://fireart.studio/wp-content/uploads/2021/09/9-145.jpg'
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=image_url,
            caption=welcome_text,
            parse_mode='Markdown',
            reply_markup=get_main_menu()
        )

# --- Callback & Message Handlers ---
# Button callback handler
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    # BONUS START
    if query.data == 'bonus_start':
        text = (
            "🎁 **WELCOME TO BONUS PROGRAM!** 🎁\n\n"
            "💰 Get exclusive bonuses and rewards!\n\n"
            "First, let's get to know you better...\n\n"
            "**What type of player are you?** 🎮"
        )
        await query.edit_message_caption(caption=text, reply_markup=get_player_type_keyboard(), parse_mode='Markdown')
    # PLAYER TYPE SELECTION
    elif query.data in ['player_beginner', 'player_highroller']:
        player_type = "🎯 Beginner" if query.data == 'player_beginner' else "💎 High Roller"
        text = (
            f"✨ Great choice! You selected: **{player_type}**\n\n"
            f"Now, let me ask you...\n\n"
            f"**Do you already have a PickWin account?** 🎰"
        )
        context.user_data['player_type'] = player_type
        await query.edit_message_caption(caption=text, reply_markup=get_account_check_keyboard(), parse_mode='Markdown')
    # HAS ACCOUNT - YES
    elif query.data == 'has_account_yes':
        text = (
            "✅ **Awesome! You already have an account!**\n\n"
            "📝 Please provide your **PickWin Account ID** or **Username**:\n\n"
            "👉 Just type it in the chat and send it to me!\n\n"
            "⚠️ _Note: A human agent will verify your account and process your bonus shortly._"
        )
        context.user_data['waiting_for'] = 'account_id'
        await query.edit_message_caption(caption=text, reply_markup=get_back_button(), parse_mode='Markdown')
    # HAS ACCOUNT - NO
    elif query.data == 'has_account_no':
        text = (
            "🎯 **No problem! Let's get you set up!**\n\n"
            "I'll guide you through 3 simple steps:\n\n"
            "**STEP 1: Create Your Account** 📱\n"
            "Click the link below to register:\n"
            "👉 https://pickwin-casino.example.com/register\n\n"
            "**STEP 2: VPN Setup** 🔒\n"
            "For security and access, you'll need a VPN.\n"
            "📖 Tutorial: https://vpn-tutorial.example.com\n\n"
            "**Quick VPN Guide:**\n"
            "1️⃣ Download a VPN app (NordVPN, ExpressVPN, etc.)\n"
            "2️⃣ Connect to a recommended server\n"
            "3️⃣ Open PickWin and enjoy!\n\n"
            "**STEP 3: Verification** ✅\n"
            "Once your account is created, come back here!\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "**Have you completed the setup?** 👇"
        )
        await query.edit_message_caption(caption=text, reply_markup=get_verification_keyboard(), parse_mode='Markdown')
    # ACCOUNT READY - YES
    elif query.data == 'account_ready_yes':
        text = (
            "🎉 **Fantastic! Your account is ready!**\n\n"
            "📝 Please provide your **PickWin Username**:\n\n"
            "👉 Just type it in the chat below!\n\n"
            "⏳ _We'll verify your account and add your bonuses shortly._\n"
            "💬 _A human agent may contact you for verification._"
        )
        context.user_data['waiting_for'] = 'username_verify'
        await query.edit_message_caption(caption=text, reply_markup=get_back_button(), parse_mode='Markdown')
    # SHOW TUTORIALS AGAIN
    elif query.data == 'show_tutorials':
        text = (
            "📚 **SETUP TUTORIALS**\n\n"
            "**STEP 1: Create Account** 📱\n"
            "👉 https://pickwin-casino.example.com/register\n\n"
            "**STEP 2: VPN Setup** 🔒\n"
            "📖 Full Tutorial: https://vpn-tutorial.example.com\n\n"
            "**Quick Steps:**\n"
            "1️⃣ Download VPN app (NordVPN recommended)\n"
            "2️⃣ Connect to server (US or UK)\n"
            "3️⃣ Open PickWin casino\n"
            "4️⃣ Start playing!\n\n"
            "**Need help?** Contact support anytime! 💬"
        )
        await query.edit_message_caption(caption=text, reply_markup=get_verification_keyboard(), parse_mode='Markdown')
    # HELP & INFO
    elif query.data == 'help':
        text = (
            "❓ **HELP & INFORMATION**\n\n"
            "**About PickWin Casino** 🎰\n"
            "Your trusted online casino platform with:\n"
            "• 🎮 1000+ Games\n"
            "• 💰 Daily Bonuses\n"
            "• ⚡ Instant Withdrawals\n"
            "• 🔒 Secure & Licensed\n\n"
            "**How to Get Started:**\n"
            "1️⃣ Click '✨ Claim Your Bonus! ✨'\n"
            "2️⃣ Choose your player type\n"
            "3️⃣ Create account or login\n"
            "4️⃣ Get your bonuses!\n\n"
            "**Support:**\n"
            "📧 Email: support@pickwin.example.com\n"
            "💬 Live Chat: 24/7 available\n"
            "📱 Telegram: @PickWinSupport\n\n"
            "**Quick Links:**\n"
            "🌐 Website: https://pickwin.example.com\n"
            "📖 FAQ: https://pickwin.example.com/faq"
        )
        await query.edit_message_caption(caption=text, reply_markup=get_back_button(), parse_mode='Markdown')
    # CHECK STATUS
    elif query.data == 'check_status':
        submitted_id = context.user_data.get('submitted_id', 'N/A')
        submitted_username = context.user_data.get('submitted_username', 'N/A')
        status_text = (
            "🔍 **Request Status**\n\n"
            "📋 **Submitted Information:**\n"
        )
        if submitted_id != 'N/A':
            status_text += f"• Account ID: `{submitted_id}`\n"
        if submitted_username != 'N/A':
            status_text += f"• Username: `{submitted_username}`\n"
        status_text += (
            "\n⏰ **Status:** Pending Review\n\n"
            "💬 Our team typically responds within 24 hours.\n\n"
            "📧 You'll be notified when complete!"
        )
        await query.edit_message_caption(
            caption=status_text,
            reply_markup=get_back_button(),
            parse_mode='Markdown'
        )
    # RESTART FRESH
    elif query.data == 'restart_fresh':
        # Clear all data and start fresh
        context.user_data.clear()
        user = query.from_user
        welcome_text = (
            f"🎰 **Welcome Back to PickWin Casino Bot!** 🎰\n\n"
            f"Hey {user.first_name}! 👋\n\n"
            f"Starting fresh! Choose an option below:"
        )
        try:
            await query.edit_message_caption(
                caption=welcome_text,
                reply_markup=get_main_menu(),
                parse_mode='Markdown'
            )
        except BadRequest as e:
            logger.warning(f"Could not edit message: {e}. Sending new message.")
            image_url = 'https://fireart.studio/wp-content/uploads/2021/09/9-145.jpg'
            await query.message.reply_photo(
                photo=image_url,
                caption=welcome_text,
                parse_mode='Markdown',
                reply_markup=get_main_menu()
            )
    # BACK TO MAIN MENU
    elif query.data == 'back_main':
        # Check if user has pending verification
        waiting_for = context.user_data.get('waiting_for')
        if waiting_for == 'pending_verification':
            # Show status instead of starting over
            submitted_id = context.user_data.get('submitted_id', 'N/A')
            submitted_username = context.user_data.get('submitted_username', 'N/A')
            status_text = (
                "⏳ **Verification In Progress**\n\n"
                "📋 **Your Submission:**\n"
            )
            if submitted_id != 'N/A':
                status_text += f"• Account ID: `{submitted_id}`\n"
            if submitted_username != 'N/A':
                status_text += f"• Username: `{submitted_username}`\n"
            status_text += (
                "\n🎁 Our team is processing your bonus request!\n\n"
                "💬 You'll receive a notification when ready.\n\n"
                "🔄 **What would you like to do?**"
            )
            try:
                await query.edit_message_caption(
                    caption=status_text,
                    reply_markup=get_status_menu(),
                    parse_mode='Markdown'
                )
            except BadRequest as e:
                logger.warning(f"Could not edit message: {e}. Sending new message.")
                await query.message.reply_text(
                    status_text,
                    parse_mode='Markdown',
                    reply_markup=get_status_menu()
                )
        else:
            # Normal back to main menu
            user = query.from_user
            welcome_text = (
                f"🎰 **Welcome to PickWin Casino Bot!** 🎰\n\n"
                f"Hey {user.first_name}! 👋\n\n"
                f"I'm here to help you get started with exclusive bonuses, "
                f"account setup, and more!\n\n"
                f"Choose an option below to continue:"
            )
            try:
                await query.edit_message_caption(
                    caption=welcome_text,
                    reply_markup=get_main_menu(),
                    parse_mode='Markdown'
                )
            except BadRequest as e:
                logger.warning(f"Could not edit message: {e}. Sending new message.")
                image_url = 'https://fireart.studio/wp-content/uploads/2021/09/9-145.jpg'
                await query.message.reply_photo(
                    photo=image_url,
                    caption=welcome_text,
                    parse_mode='Markdown',
                    reply_markup=get_main_menu()
                )

# Handle text messages (account ID, username input)
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return  # Ignore non-text
    text = update.message.text.strip().lower()
    waiting_for = context.user_data.get('waiting_for')
    original_text = update.message.text.strip()  # Keep original for display
    
    # Basic input sanitization (limit length to prevent abuse)
    if len(original_text) > 100:
        await update.message.reply_text("Input too long! Please keep it under 100 characters.")
        return
    
    # Handle specific expected inputs first
    if waiting_for == 'account_id':
        response = (
            f"✅ **Account ID Received!**\n\n"
            f"📋 Your Account ID: `{original_text}`\n\n"
            f"⏳ **Processing your request...**\n\n"
            f"🎁 A human agent will verify your account and process your bonus within 24 hours!\n\n"
            f"💬 You'll receive a notification once it's ready.\n\n"
            f"Thank you for your patience! 🙏"
        )
        context.user_data['waiting_for'] = 'pending_verification'
        context.user_data['submitted_id'] = original_text
        await update.message.reply_text(response, reply_markup=get_back_button(), parse_mode='Markdown')
        return
    elif waiting_for == 'username_verify':
        response = (
            f"🎉 **Username Received!**\n\n"
            f"👤 Username: `{original_text}`\n\n"
            f"🔍 **Verifying your account...**\n\n"
            f"✨ We're checking our system for your account.\n"
            f"💰 Your bonuses will be added once verified!\n\n"
            f"⏰ This usually takes 5-30 minutes.\n\n"
            f"Thank you! 🎰"
        )
        context.user_data['waiting_for'] = 'pending_verification'
        context.user_data['submitted_username'] = original_text
        await update.message.reply_text(response, reply_markup=get_back_button(), parse_mode='Markdown')
        return
    elif waiting_for == 'pending_verification':
        # User already submitted - remind them
        response = (
            "⏳ **Your request is still being processed!**\n\n"
            "📋 We have your information and our team is working on it.\n\n"
            "💬 You'll be notified once your bonus is ready!\n\n"
            "🔄 Want to check status or start over? Type /start"
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        return
    # Handle common user intents when bot isn't waiting for input
    # Check for help-related keywords
    if any(word in text for word in ['help', 'support', 'assist', 'info', 'information', '?']):
        help_text = (
            "❓ **HELP & INFORMATION**\n\n"
            "**About PickWin Casino** 🎰\n"
            "Your trusted online casino platform with:\n"
            "• 🎮 1000+ Games\n"
            "• 💰 Daily Bonuses\n"
            "• ⚡ Instant Withdrawals\n"
            "• 🔒 Secure & Licensed\n\n"
            "**How to Get Started:**\n"
            "1️⃣ Click '✨ Claim Your Bonus! ✨'\n"
            "2️⃣ Choose your player type\n"
            "3️⃣ Create account or login\n"
            "4️⃣ Get your bonuses!\n\n"
            "**Support:**\n"
            "📧 Email: support@pickwin.example.com\n"
            "💬 Live Chat: 24/7 available\n"
            "📱 Telegram: @PickWinSupport\n\n"
            "**Quick Links:**\n"
            "🌐 Website: https://pickwin.example.com\n"
            "📖 FAQ: https://pickwin.example.com/faq"
        )
        await update.message.reply_text(help_text, reply_markup=get_back_button(), parse_mode='Markdown')
        return
    # Check for status-related keywords
    if any(word in text for word in ['status', 'check', 'pending', 'verify', 'verification', 'waiting']):
        submitted_id = context.user_data.get('submitted_id')
        submitted_username = context.user_data.get('submitted_username')
        if submitted_id or submitted_username:
            status_text = (
                "🔍 **Request Status**\n\n"
                "📋 **Submitted Information:**\n"
            )
            if submitted_id:
                status_text += f"• Account ID: `{submitted_id}`\n"
            if submitted_username:
                status_text += f"• Username: `{submitted_username}`\n"
            status_text += (
                "\n⏰ **Status:** Pending Review\n\n"
                "💬 Our team typically responds within 24 hours.\n\n"
                "📧 You'll be notified when complete!"
            )
            await update.message.reply_text(status_text, reply_markup=get_back_button(), parse_mode='Markdown')
        else:
            await update.message.reply_text(
                "You don't have any pending requests.\n\nType /start to begin! 🎰",
                parse_mode='Markdown'
            )
        return
    # Check for bonus-related keywords
    if any(word in text for word in ['bonus', 'claim', 'reward', 'promotion', 'promo', 'offer']):
        bonus_text = (
            "🎁 **Ready to claim your bonus?**\n\n"
            "Click the button below to get started!\n\n"
            "💰 Exclusive bonuses waiting for you!"
        )
        keyboard = [[InlineKeyboardButton("✨ Claim Your Bonus! ✨", callback_data='bonus_start')]]
        await update.message.reply_text(
            bonus_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
        return
    # Check for greetings
    if any(word in text for word in ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']):
        user = update.effective_user
        greeting_text = (
            f"👋 Hello {user.first_name}!\n\n"
            f"Welcome to PickWin Casino Bot! 🎰\n\n"
            f"I'm here to help you get exclusive bonuses and set up your account.\n\n"
            f"Type /start to see the main menu!"
        )
        await update.message.reply_text(greeting_text, parse_mode='Markdown')
        return
    # Check for thank you messages
    if any(word in text for word in ['thank', 'thanks', 'thx', 'ty', 'appreciate']):
        await update.message.reply_text(
            "You're welcome! 😊\n\nNeed anything else? Type /start for the main menu!",
            parse_mode='Markdown'
        )
        return
    # Default response for unrecognized messages
    user = update.effective_user
    default_response = (
        f"👋 Hey {user.first_name}!\n\n"
        f"I'm not sure what you're looking for, but I'm here to help! 🎰\n\n"
        f"**Quick Commands:**\n"
        f"• Type /start - Main menu\n"
        f"• Say 'help' - Get support info\n"
        f"• Say 'bonus' - Claim bonuses\n"
        f"• Say 'status' - Check your request\n\n"
        f"Or just click the button below! 👇"
    )
    keyboard = [[InlineKeyboardButton("🎰 Show Main Menu", callback_data='back_main')]]
    await update.message.reply_text(
        default_response,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

# --- Error Handler ---
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f'Update {update} caused error {context.error}')
    # Ignore common non-critical errors
    if isinstance(context.error, BadRequest):
        error_message = str(context.error)
        if "Message can't be deleted" in error_message:
            logger.warning("Attempted to delete an old message (>48h) - ignoring error")
            return
        if "Message is not modified" in error_message:
            logger.warning("Message content unchanged - ignoring error")
            return
    # For network errors, just log them (they're usually temporary)
    if isinstance(context.error, (TimedOut, NetworkError)):
        logger.warning(f"Network error occurred: {context.error}")
        return

# --- Main Bot Execution ---
def main():
    application = Application.builder().token(API_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
    application.add_error_handler(error_handler)
    
    # For render.com deployment
    print("🎰 PickWin Casino Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()