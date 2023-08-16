import logging

from pathlib import Path
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

logger = logging.getLogger(__name__)

def main() -> None:
    updater = Updater("6095229139:AAFo_XcjRNY3xZb2M-y8yQeK19BdmFvtkIA")
    dispatcher = updater.dispatcher
    
    for extt in Path("ext/").glob("*.py"):
    	ext_name = extt.name.split(".")[0]
    	exec(f"from ext import {ext_name}")
    	exec(f"dispatcher.add_handler(CommandHandler(ext.{ext_name}.name, ext.{ext_name}.{ext_name}))")
    	print(f"CMD Extension Loaded: {ext_name}")
    
    for extt in Path("ext_msg/").glob("*.py"):
    	ext_name = extt.name.split(".")[0]
    	exec(f"from ext_msg import {ext_name}")
    	exec(f"dispatcher.add_handler(MessageHandler(~Filters.command, {ext_name}.{ext_name}))")
    	print(f"MSG Extension Loaded: {ext_name}")
    
    for extt in Path("ext_btn/").glob("*.py"):
    	ext_name = extt.name.split(".")[0]
    	exec(f"from ext_btn import {ext_name}")
    	exec(f"dispatcher.add_handler(CallbackQueryHandler({ext_name}.name, {ext_name}.{ext_name}))")
    	print(f"BTN Extension Loaded: {ext_name}")
    
    updater.start_polling()
    print("bot is ready")
    updater.idle()
if __name__ == '__main__':
    main()
