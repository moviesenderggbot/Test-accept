from pyrogram import utils as pyroutils

pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
#async def approve(_, m : Message):
#    op = m.chat
#    kk = m.from_user
#    try:
#        add_group(m.chat.id) 
#        await app.approve_chat_join_request(op.id, kk.id)
#        img = random.choice(gif)
#        await app.send_video(kk.id,img, "**Hello {}!\nWelcome To {}\n\n__Powerd By : @xyz_bots **".format(m.from_user.mention, m.chat.title))
#        add_user(kk.id)
#    except errors.PeerIdInvalid as e:
#        print("user isn't start bot(means group)")
#    except Exception as err:
#        print(str(err))    

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m: Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        welcome_text = "**Hello {}!\nWelcome To {}\n\n__Powered By : @xyz_bots **".format(kk.mention, op.title)
        button = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("1. 😍🔥 𝘀𝗲𝘅𝘆 𝗯𝗵𝗮𝗯𝗵𝗶 𝗟𝗼𝘃𝗲𝗿𝘀 🔥😍", url="https://t.me/GB_Links_Offical")
            ],[
            InlineKeyboardButton("2. 🖤👅 𝗶𝗻𝘀𝘁𝗮 𝘃𝗶𝗿𝗮𝗹 𝘃𝗶𝗱𝗲𝗼𝘀 🤤💋 ", url="https://t.me/GB_LINKS")
            ],[
            InlineKeyboardButton("3. 😍🤤 𝗗𝗲𝘀𝗶 𝗥𝗮𝗻𝗱𝗶 𝗰𝗵𝘂𝘁 👅💋", url="https://t.me/+eudmbU69FGwzMDQ0")
            ],[
            InlineKeyboardButton("4. 👅💋𝗰𝗵𝗮𝗿𝗮𝗺 𝘀𝘂𝗸𝗵 𝘃𝗶𝗱𝗲𝗼𝘀 🖤❤️‍🔥", url="https://t.me/+iDDgbgZ7PK0yNGNk")
            ],[
            InlineKeyboardButton("5. 🔥😍𝗦𝗲𝘅𝘆 𝘃𝗶𝗿𝗮𝗹 𝘃𝗶𝗱𝗲𝗼𝘀 🖤💋", url="https://t.me/+KiqAAgBg7NEyYzFk")
            ],[
            InlineKeyboardButton("6. 🔥😍porn Hub collection 🖤💋", url="https://t.me/+StAWi9MLzZZhZTY8")
            ],[
            InlineKeyboardButton("7.👄💦Aunty lovers 👻❤️‍🔥❤️‍🔥", url="https://t.me/+kh_w3pkctocyYzI0")  
            ],[
            InlineKeyboardButton("8.😻🔥 𝗴𝗳 𝗯𝗳 𝗸𝗶 𝗰𝗵𝘂𝗱𝗮𝗶👅💋", url="https://t.me/dasi_video_sex")
            ],[
            InlineKeyboardButton("9. DESI GF BF VIDEOS🥵🌚", url="https://t.me/+R4JHodCSQ2IzMDll")
            ],[
            InlineKeyboardButton("10.👄💦Instagram Viral 👻❤️‍🔥❤️‍🔥", url="https://t.me/GB_Links_Backup")
            ],[
            InlineKeyboardButton("👉👉 𝙾𝚗𝚎 𝚝𝚊𝚙 𝚓𝚘𝚒𝚗 𝚊𝚕𝚕 👈👈", url="https://t.me/addlist/EGw8nT_eBjRhMTRl")
        ]])
        await app.send_video(
            kk.id, 
            img, 
            caption=welcome_text, 
            reply_markup=button
        )
        add_user(kk.id)
    
    except errors.PeerIdInvalid as e:
        print("User hasn't started the bot yet (PeerIdInvalid)")
    except Exception as err:
        print(str(err))
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/xyz_bots"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/XYZ_Support_Chat")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/XYZ_Auto_Accept_bot?startgroup")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://telegra.ph/file/c7ac07501e857860334e7.jpg https://telegra.ph/file/943126cf288c36e0e086d.jpg https://telegra.ph/file/63b6dc593585363ded68d.jpg", caption="**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @xyz_bots **".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/XYZ_Auto_Accept_bot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 Hello {}!\nwrite me private for more details**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**⚠️Access Denied!⚠️\n\nPlease Join @{} to use me.If you joined click check again button to confirm.**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/xyz_bots"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/XYZ_Support_Chat")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/XYZ_Auto_Accept_bot?startgroup")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @xyz_bots **".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ You are not joined to channel join and try again. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now!")
app.run()
