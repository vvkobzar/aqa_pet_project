import json
import os
from dotenv import load_dotenv

load_dotenv()

config_path = os.path.join(os.getcwd(), 'notifications/config.json')

token = os.getenv('TELEGRAM_BOT_TOKEN')
chat = os.getenv('TELEGRAM_CHAT')

with open(config_path, 'r+') as file:
    config = json.load(file)
    if token:
        config['telegram']['token'] = token
    if chat:
        config['telegram']['chat'] = chat
    file.seek(0)
    json.dump(config, file, indent=2)
    file.truncate()
