from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22620068"))
    API_HASH = getenv("API_HASH", "11e2c113078324f7e36688baa86c3911")
    BOT_TOKEN = getenv("BOT_TOKEN", "7274390732:AAHq3xQfTtkckKAe-7vdkeYcyb4GkpY0QPY")
    FSUB = getenv("FSUB", "xyz_bots")
    CHID = int(getenv("CHID", "-1002186382302"))
    SUDO = 72299906119
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://t54s2lqiv6:2mOV4n1iL21cMcMH@cluster0.ma3sm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
