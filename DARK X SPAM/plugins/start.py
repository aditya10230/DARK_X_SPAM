import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from DARK X SPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID

DARK X SPAM_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/c6f99c0b68ff07439ed72.jpg"

DARK X SPAM_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/Dark_X_ChattingZone")
        ],
        [
        Button.url("• ᴍᴀɪɴᴛᴀɪɴ ʙʏ •", "https://t.me/NARUT0XD")
        ]
        ]
               
Dark_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/DARK_X_CHANNEL"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/DARK_X_CHANNEL")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •","https://github.com/aditya10230/DARK_X_SPAM")
        ]
        ]
        
        
#USERS 


@BOT0.on(events.NewMessage(pattern="/start"))
@BOT1.on(events.NewMessage(pattern="/start"))
@BOT2.on(events.NewMessage(pattern="/start"))
@BOT3.on(events.NewMessage(pattern="/start"))
@BOT4.on(events.NewMessage(pattern="/start"))
@BOT5.on(events.NewMessage(pattern="/start"))
@BOT6.on(events.NewMessage(pattern="/start"))
@BOT7.on(events.NewMessage(pattern="/start"))
@BOT8.on(events.NewMessage(pattern="/start"))
@BOT9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DarkBot = await event.client.get_me()
       bot_id = DarkBot.first_name
       bot_username = DarkBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheDark= event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheDARK,
                  DARK X SPAM_IMG,
                  caption=ownermsg, 
                  buttons=DARK X SPAM_Button)
       else:
            await event.client.send_file(TheDark,
                  DARK X SPAM_IMG,
                  caption=usermsg, 
                  buttons=DARK X SPAM_Button)
                
