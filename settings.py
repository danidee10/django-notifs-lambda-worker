# Configure django settings
# Remove unnecessary settings
# Don't forget to set environment variables in .env file!!!

import os


NOTIFICATIONS_PUSHER_CHANNELS_URL = os.getenv('NOTIFICATIONS_PUSHER_CHANNELS_URL')
NOTIFICATIONS_SLACK_BOT_TOKEN = os.getenv('NOTIFICATIONS_SLACK_BOT_TOKEN')

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')

DEFAULT_FROM_SMS = os.getenv('DEFAULT_FROM_SMS')
SMS_BACKEND = os.getenv('SMS_BACKEND')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
