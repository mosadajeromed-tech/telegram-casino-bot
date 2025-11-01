"""
PickWin Casino Bot - Main
Simple entry point
"""
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

import config
import handlers

# ============================================================================
# LOGGING
# ============================================================================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# ============================================================================
# MAIN
# ============================================================================
def main():
    """Start bot"""
    logger.info("🎰 PickWin Bot Starting...")
    
    # Create app
    application = Application.builder().token(config.BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", handlers.start_command))
    application.add_handler(CallbackQueryHandler(handlers.button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_text_message))
    application.add_error_handler(handlers.error_handler)
    
    # Run
    logger.info("✅ Bot Running!")
    print("\n🎰 PickWin Bot is RUNNING!")
    print("Press Ctrl+C to stop\n")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped")
        print("\n✅ Bot stopped")
