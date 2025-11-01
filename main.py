"""
PickWin Casino Bot - Main Application
Entry point for the bot
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

import config
import handlers

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('pickwin_bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Start the bot"""
    logger.info("=" * 60)
    logger.info("🎰 PickWin Casino Bot Starting...")
    logger.info("=" * 60)
    
    # Create application
    application = Application.builder().token(config.BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", handlers.start_command))
    
    # Add callback query handler for all buttons
    application.add_handler(CallbackQueryHandler(handlers.button_callback))
    
    # Add message handler for text messages
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_text_message)
    )
    
    # Add error handler
    application.add_error_handler(handlers.error_handler)
    
    # Start the bot
    logger.info("✅ All handlers registered successfully")
    logger.info("🚀 Bot is now running...")
    logger.info("⏸  Press Ctrl+C to stop")
    logger.info("=" * 60)
    
    print("\n" + "=" * 60)
    print("🎰 PickWin Casino Bot is RUNNING!")
    print("=" * 60)
    print("✅ Ready to accept messages")
    print("💬 Type /start in Telegram to begin")
    print("⏸  Press Ctrl+C to stop the bot")
    print("=" * 60 + "\n")
    
    # Run the bot
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True
    )

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\n🛑 Bot stopped by user")
        print("\n🛑 Bot stopped successfully")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        print(f"\n❌ Error: {e}")
        raise
