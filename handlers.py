"""
PickWin Casino Bot - Handlers
With Bonus Flow
"""
import logging
from telegram import Update, InputMediaPhoto
from telegram.ext import ContextTypes

from config import get_random_image, WELCOME_TEXT, CASINO_TEXT, SPORTS_TEXT, URLS
from keyboards import (
    get_main_menu, get_casino_menu, get_sports_menu,
    get_player_type_keyboard, get_account_check_keyboard,
    get_verification_keyboard, get_status_menu, get_back_button
)

logger = logging.getLogger(__name__)

# ============================================================================
# COMMAND HANDLER
# ============================================================================
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    try:
        user = update.effective_user
        chat_id = update.effective_chat.id
        
        logger.info(f"User {user.id} started bot")
        
        # Check if user has pending verification
        waiting_for = context.user_data.get('waiting_for')
        
        if waiting_for == 'pending_verification':
            # User has pending request - show status
            submitted_id = context.user_data.get('submitted_id', 'N/A')
            submitted_username = context.user_data.get('submitted_username', 'N/A')
            player_type = context.user_data.get('player_type', 'N/A')
            
            status_text = (
                f"👋 **Welcome back, {user.first_name}!**\n\n"
                "⏳ **You have a pending verification request**\n\n"
                "📋 **Your Submission:**\n"
            )
            
            if player_type != 'N/A':
                status_text += f"• Player Type: {player_type}\n"
            if submitted_id != 'N/A':
                status_text += f"• Account ID: `{submitted_id}`\n"
            if submitted_username != 'N/A':
                status_text += f"• Username: `{submitted_username}`\n"
            
            status_text += (
                "\n🎁 Our team is processing your bonus request!\n\n"
                "💬 You'll receive a notification when ready.\n\n"
                "What would you like to do?"
            )
            
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=get_random_image(),
                caption=status_text,
                parse_mode='Markdown',
                reply_markup=get_status_menu()
            )
        else:
            # Normal welcome
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=get_random_image(),
                caption=WELCOME_TEXT,
                parse_mode='Markdown',
                reply_markup=get_main_menu()
            )
    except Exception as e:
        logger.error(f"Error in start: {e}")

# ============================================================================
# CALLBACK HANDLER
# ============================================================================
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    try:
        query = update.callback_query
        await query.answer()
        
        # MAIN MENU
        if query.data == 'back_main':
            context.user_data.clear()  # Clear all user data
            await query.edit_message_media(
                media=InputMediaPhoto(
                    media=get_random_image(),
                    caption=WELCOME_TEXT,
                    parse_mode='Markdown'
                ),
                reply_markup=get_main_menu()
            )
        
        # BONUS START
        elif query.data == 'bonus_start':
            text = (
                "🎁 **WELCOME TO BONUS PROGRAM!** 🎁\n\n"
                "💰 Get exclusive bonuses and rewards!\n\n"
                "First, let's get to know you better...\n\n"
                "**What type of player are you?** 🎮"
            )
            await query.edit_message_caption(
                caption=text,
                reply_markup=get_player_type_keyboard(),
                parse_mode='Markdown'
            )
        
        # PLAYER TYPE SELECTION
        elif query.data in ['player_beginner', 'player_highroller']:
            player_type = "🎯 Beginner" if query.data == 'player_beginner' else "💎 High Roller"
            text = (
                f"✨ Great choice! You selected: **{player_type}**\n\n"
                f"Now, let me ask you...\n\n"
                f"**Do you already have a PickWin account?** 🎰"
            )
            context.user_data['player_type'] = player_type
            await query.edit_message_caption(
                caption=text,
                reply_markup=get_account_check_keyboard(),
                parse_mode='Markdown'
            )
        
        # HAS ACCOUNT - YES
        elif query.data == 'has_account_yes':
            text = (
                "✅ **Awesome! You already have an account!**\n\n"
                "📝 Please provide your **PickWin Account ID** or **Username**:\n\n"
                "👉 Just type it in the chat and send it to me!\n\n"
                "⚠️ *Note: A human agent will verify your account and process your bonus shortly.*"
            )
            context.user_data['waiting_for'] = 'account_id'
            await query.edit_message_caption(
                caption=text,
                reply_markup=get_back_button(),
                parse_mode='Markdown'
            )
        
        # HAS ACCOUNT - NO
        elif query.data == 'has_account_no':
            text = (
                "🎯 **No problem! Let's get you set up!**\n\n"
                "I'll guide you through 3 simple steps:\n\n"
                "**STEP 1: Create Your Account** 📱\n"
                f"Click the link below to register:\n"
                f"👉 {URLS['register']}\n\n"
                "**STEP 2: Make Your First Deposit** 💰\n"
                "Login and deposit to start playing!\n\n"
                "**STEP 3: Come Back Here** ✅\n"
                "Once your account is created and funded, return here!\n\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "**Have you completed the setup?** 👇"
            )
            await query.edit_message_caption(
                caption=text,
                reply_markup=get_verification_keyboard(),
                parse_mode='Markdown'
            )
        
        # SHOW TUTORIALS AGAIN
        elif query.data == 'show_tutorials':
            text = (
                "📖 **SETUP GUIDE** 📖\n\n"
                "**STEP 1: Create Your Account** 📱\n"
                f"Register here: {URLS['register']}\n\n"
                "**STEP 2: Login** 🔐\n"
                f"Login here: {URLS['login']}\n\n"
                "**STEP 3: Make Deposit** 💰\n"
                "Go to Cashier and fund your account\n\n"
                "**STEP 4: Return Here** ✅\n"
                "Come back and claim your bonus!\n\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "**Ready now?** 👇"
            )
            await query.edit_message_caption(
                caption=text,
                reply_markup=get_verification_keyboard(),
                parse_mode='Markdown'
            )
        
        # ACCOUNT READY - YES
        elif query.data == 'account_ready_yes':
            text = (
                "🎉 **Fantastic! Your account is ready!**\n\n"
                "📝 Please provide your **PickWin Username**:\n\n"
                "👉 Just type it in the chat below!\n\n"
                "⏳ *We'll verify your account and add your bonuses shortly.*\n"
                "💬 *A human agent may contact you for verification.*"
            )
            context.user_data['waiting_for'] = 'account_id'
            await query.edit_message_caption(
                caption=text,
                reply_markup=get_back_button(),
                parse_mode='Markdown'
            )
        
        # STATUS CHECK
        elif query.data == 'check_status':
            submitted_id = context.user_data.get('submitted_id', 'N/A')
            submitted_username = context.user_data.get('submitted_username', 'N/A')
            player_type = context.user_data.get('player_type', 'N/A')
            
            status_text = (
                "📊 **VERIFICATION STATUS** 📊\n\n"
                "⏳ **Status:** Pending Review\n\n"
                "📋 **Your Information:**\n"
            )
            
            if player_type != 'N/A':
                status_text += f"• Player Type: {player_type}\n"
            if submitted_id != 'N/A':
                status_text += f"• Account ID: `{submitted_id}`\n"
            if submitted_username != 'N/A':
                status_text += f"• Username: `{submitted_username}`\n"
            
            status_text += (
                "\n🎁 **What's Next:**\n"
                "• Our team will verify your account\n"
                "• You'll receive a notification\n"
                "• Bonuses will be added automatically\n\n"
                "💬 Average wait time: 24-48 hours"
            )
            
            await query.edit_message_caption(
                caption=status_text,
                reply_markup=get_status_menu(),
                parse_mode='Markdown'
            )
        
        # RESTART FRESH
        elif query.data == 'restart_fresh':
            context.user_data.clear()
            text = (
                "🔄 **Starting Fresh!**\n\n"
                "Your previous request has been cleared.\n\n"
                "Let's start over! 🎁"
            )
            await query.edit_message_caption(
                caption=text,
                reply_markup=get_main_menu(),
                parse_mode='Markdown'
            )
        
        # CASINO MENU
        elif query.data == 'casino_menu':
            await query.edit_message_media(
                media=InputMediaPhoto(
                    media=get_random_image(),
                    caption=CASINO_TEXT,
                    parse_mode='Markdown'
                ),
                reply_markup=get_casino_menu()
            )
        
        # SPORTS MENU
        elif query.data == 'sports_menu':
            await query.edit_message_media(
                media=InputMediaPhoto(
                    media=get_random_image(),
                    caption=SPORTS_TEXT,
                    parse_mode='Markdown'
                ),
                reply_markup=get_sports_menu()
            )
            
    except Exception as e:
        logger.error(f"Error in callback: {e}")

# ============================================================================
# MESSAGE HANDLER
# ============================================================================
async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages"""
    try:
        text = update.message.text
        user = update.effective_user
        
        # Check if waiting for account ID/username
        waiting_for = context.user_data.get('waiting_for')
        
        if waiting_for == 'account_id':
            # User is providing username/ID
            player_type = context.user_data.get('player_type', 'Not specified')
            
            # Save the info
            context.user_data['submitted_username'] = text
            context.user_data['submitted_id'] = text
            context.user_data['waiting_for'] = 'pending_verification'
            
            response = (
                "✅ **SUBMISSION RECEIVED!** ✅\n\n"
                f"📝 **Your Information:**\n"
                f"• Player Type: {player_type}\n"
                f"• Username/ID: `{text}`\n\n"
                "🎁 **What Happens Next:**\n"
                "1️⃣ Our team will verify your account\n"
                "2️⃣ We'll check your deposit status\n"
                "3️⃣ Bonuses will be added to your account\n"
                "4️⃣ You'll receive a notification here\n\n"
                "⏱️ **Wait Time:** Usually 24-48 hours\n\n"
                "💬 **Need help?** A support agent may contact you.\n\n"
                "Thank you for choosing PickWin! 🎰"
            )
            
            await update.message.reply_photo(
                photo=get_random_image(),
                caption=response,
                parse_mode='Markdown',
                reply_markup=get_status_menu()
            )
            
            # Log to admin (you can add your admin chat ID here)
            admin_notification = (
                "🔔 **NEW BONUS REQUEST**\n\n"
                f"👤 User: {user.first_name} (@{user.username or 'No username'})\n"
                f"🆔 Telegram ID: `{user.id}`\n"
                f"🎯 Player Type: {player_type}\n"
                f"📝 Account: `{text}`\n\n"
                "⏳ Awaiting verification"
            )
            logger.info(admin_notification)
            
        # Keywords
        elif any(word in text.lower() for word in ['casino', 'slot', 'game', 'play']):
            await update.message.reply_photo(
                photo=get_random_image(),
                caption=CASINO_TEXT,
                parse_mode='Markdown',
                reply_markup=get_casino_menu()
            )
        
        elif any(word in text.lower() for word in ['sport', 'bet', 'soccer', 'basketball']):
            await update.message.reply_photo(
                photo=get_random_image(),
                caption=SPORTS_TEXT,
                parse_mode='Markdown',
                reply_markup=get_sports_menu()
            )
        
        # Default
        else:
            await update.message.reply_photo(
                photo=get_random_image(),
                caption=WELCOME_TEXT,
                parse_mode='Markdown',
                reply_markup=get_main_menu()
            )
            
    except Exception as e:
        logger.error(f"Error handling message: {e}")

# ============================================================================
# ERROR HANDLER
# ============================================================================
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Error: {context.error}")
