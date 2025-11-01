"""
PickWin Casino Bot - Handlers
Simple and clean
"""
import logging
from telegram import Update, InputMediaPhoto
from telegram.ext import ContextTypes

from config import get_random_image, WELCOME_TEXT, CASINO_TEXT, SPORTS_TEXT
from keyboards import get_main_menu, get_casino_menu, get_sports_menu

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
        
        # Main menu
        if query.data == 'back_main':
            await query.edit_message_media(
                media=InputMediaPhoto(
                    media=get_random_image(),
                    caption=WELCOME_TEXT,
                    parse_mode='Markdown'
                ),
                reply_markup=get_main_menu()
            )
        
        # Casino menu
        elif query.data == 'casino_menu':
            await query.edit_message_media(
                media=InputMediaPhoto(
                    media=get_random_image(),
                    caption=CASINO_TEXT,
                    parse_mode='Markdown'
                ),
                reply_markup=get_casino_menu()
            )
        
        # Sports menu
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
        text = update.message.text.lower()
        
        # Casino keywords
        if any(word in text for word in ['casino', 'slot', 'game', 'play']):
            await update.message.reply_photo(
                photo=get_random_image(),
                caption=CASINO_TEXT,
                parse_mode='Markdown',
                reply_markup=get_casino_menu()
            )
        
        # Sports keywords
        elif any(word in text for word in ['sport', 'bet', 'soccer', 'basketball']):
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
