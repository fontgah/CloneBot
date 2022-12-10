from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaDocument, InputMediaPhoto, InputMediaVideo, InputMediaAudio
from pyrogram.errors import FloodWait
import asyncio, os

Api_ID = 15628308
Api_HASH = "79583fe01a6a2bd774a2997f8d3924c2"
Session = "AgDueBQArPSaegMdE6_nFqBxcYha975cUUZVbgO1YFFGd0tt8cPNaLfJsPRcnN219ly5nrYmCO6u7bF0iYsmHDNPgGuFU6vZMsyB3x-PO6g2T9fEWk1L3ncMiyPggD45m8HirT9C8FNeHohS7oQT0RIKYj828wkwEDuYEfmGDPfq_CowOWrtGrb0pl95mZx1HP3GnZSOyAakul7MTBh7ZnsqLiMaaWAuJOUWX0W1YslCRoI2-Gnss5HhL4LjRgHYjeNoxtqOW9BYSjded8ceKYHMTuQPZ1s4zi7FF2KISLc_HkQTJeQHGjdPehJJ5eVNZFCU7GvjRYkdW0CBRr4BTWjz3tIm9QAAAAE9wn9BAA"

app = Client(
    name = "Clone-Bot",
    api_id = Api_ID,
    api_hash = Api_HASH,
    session_string = Session
)

print("""CloneBot is Running ..!

To start clonning, send this command:
• Clone {source.id} {target.id} {first_msg.id}-{last_msg.id}
 • {source.id} = The source channel id
 • {target.id} = The target channel id
 • {first_msg.id} = The first message id that you want to start from
 • {last_msg.id} = The last message id that you want to finish to""")

@app.on_message(filters.me & filters.regex('^[Cc][Ll][Oo][Nn][Ee] '))
async def clone(c: Client, m: Message):
    Source_CH = int(f"-100{m.text.split(' ')[1]}")
    Target_CH = int(f"-100{m.text.split(' ')[2]}")
    First_MSG = int(m.text.split(' ')[3].split('-')[0])
    Last_MSG = int(m.text.split(' ')[3].split('-')[1])
    await m.edit(f"Clone from <code>{m.text.split(' ')[1]}</code> to <code>{m.text.split(' ')[2]}</code>\n\n<b><u>Getting messages</u></b>\n\nPlease wait ..!")
    MSGs = range(First_MSG, Last_MSG+1)
    Messages = await get_msg(c, MSGs, Source_CH)
    await m.edit(f"<b><u>Starting process</u></b>\n\nPlease wait ..!")
    MEDIA = []
    Unseccess = 0
    Media_Group = 0
    for i in Messages:
        try:
            if i.text or i.photo or i.audio or i.document or i.video or i.video_note or i.animation or i.voice:
                if i.text:
                    if Media_Group != 0:
                        await c.send_media_group(Target_CH, MEDIA)
                        Media_Group = 0
                        MEDIA.clear()
                    await c.send_message(Target_CH, i.text, entities=None if not i.entities else i.entities)
                else:
                    if i.media_group_id:
                        if Media_Group == 0:
                            Media_Group = i.media_group_id
                            vc = await i.download()
                            if i.photo:
                                MEDIA.append(InputMediaPhoto(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.video:
                                MEDIA.append(InputMediaVideo(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.audio:
                                MEDIA.append(InputMediaAudio(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.document:
                                MEDIA.append(InputMediaDocument(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                        elif Media_Group == i.media_group_id:
                            vc = await i.download()
                            if i.photo:
                                MEDIA.append(InputMediaPhoto(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.video:
                                MEDIA.append(InputMediaVideo(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.audio:
                                MEDIA.append(InputMediaAudio(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.document:
                                MEDIA.append(InputMediaDocument(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                        else:
                            await c.send_media_group(Target_CH, MEDIA)
                            Media_Group = i.media_group_id
                            MEDIA.clear()
                            vc = await i.download()
                            if i.photo:
                                MEDIA.append(InputMediaPhoto(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.video:
                                MEDIA.append(InputMediaVideo(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.audio:
                                MEDIA.append(InputMediaAudio(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                            if i.document:
                                MEDIA.append(InputMediaDocument(vc, caption=None if not i.caption else i.caption, caption_entities= None if not i.caption_entities else i.caption_entities))
                    else:
                        if Media_Group != 0:
                            await c.send_media_group(Target_CH, MEDIA)
                            Media_Group = 0
                            MEDIA.clear()
                        mn = await i.download()
                        if i.photo:
                            await c.send_photo(Target_CH, mn, caption=None if not i.caption else i.caption, caption_entities=None if not i.caption_entities else i.caption_entities)
                        if i.audio:
                            await c.send_audio(Target_CH, mn, caption=None if not i.caption else i.caption, caption_entities=None if not i.caption_entities else i.caption_entities)
                        if i.video:
                            await c.send_video(Target_CH, mn, caption=None if not i.caption else i.caption, caption_entities=None if not i.caption_entities else i.caption_entities)
                        if i.video_note:
                            await c.send_video_note(Target_CH, mn)
                        if i.animation:
                            await c.send_animation(Target_CH, mn, caption=None if not i.caption else i.caption, caption_entities=None if not i.caption_entities else i.caption_entities)
                        if i.voice:
                            await c.send_voice(Target_CH, mn, caption=None if not i.caption else i.caption, caption_entities=None if not i.caption_entities else i.caption_entities)
                        if i.document:
                            await c.send_document(Target_CH, mn, caption=None if not i.caption else i.caption, caption_entities=None if not i.caption_entities else i.caption_entities)
                        os.remove(mn)
                await asyncio.sleep(0.5)
            else:
                Unseccess += 1
        except Exception as e:
            print(e)
    await m.edit(f"<b><u>Clone is finished!</u></b>\n\nSeccess: {(Last_MSG - First_MSG) - Unseccess}\nUnseccess: {Unseccess}")


async def get_msg(client, message_ids, Source_CH):
    messages = []
    total_messages = 0
    while total_messages != len(message_ids):
        temb_ids = message_ids[total_messages:total_messages+200]
        try:
            msgs = await client.get_messages(
                chat_id=Source_CH,
                message_ids=temb_ids
            )
        except FloodWait as e:
            await asyncio.sleep(e.value)
            msgs = await client.get_messages(
                chat_id=Source_CH,
                message_ids=temb_ids
            )
        except:
            pass
        total_messages += len(temb_ids)
        messages.extend(msgs)
    return messages
    
    
app.run()