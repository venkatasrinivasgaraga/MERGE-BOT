import os


class Config(object):
    API_HASH = os.environ.get("8a714c643f86acb3d07a2baa4831f95b")
    BOT_TOKEN = os.environ.get("7926389008:AAE84r3NKMfPxttKXsVYZNUcEUj6OCZAEHA")
    TELEGRAM_API = os.environ.get("22648485")
    OWNER = os.environ.get("1074804932")
    OWNER_USERNAME = os.environ.get("Orewasrinivas")
    PASSWORD = os.environ.get("crushalone")
    DATABASE_URL = os.environ.get("mongodb+srv://sainallamilli:Filestore1@cluster0.8urcp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1004794153304")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
