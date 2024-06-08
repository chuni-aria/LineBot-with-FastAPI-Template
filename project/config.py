import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LINE Bot 設定
LINE_CHANNEL_SECRET = os.environ.get("527df324216858c4bc8ef8cc20fe8652")
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("fzUW9//V6lYTsVqhjD5GWFGbr55irneEG4XOEBxsCdKD/xQ652hmNtBOooXXFRKnUYhM/qeManMK380gtIqA0J/MfxTRyzc5uCLoOO8iwDpIiwbp2tSfDN0kz86ZV3wAzrhTJrh+nzApSaKUTEBJagdB04t89/1O/w1cDnyilFU=")
GOOGLE_API_KEY = os.environ.get('AIzaSyBbrZXqpQC1HYIoRZLcug9j3oUwQI78yvw')
FIREBASE_URL = os.environ.get('https://mazda-ead30-default-rtdb.firebaseio.com/')
