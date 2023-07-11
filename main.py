import pyrogram , pyromod

from pyromod import listen
from keep import alive
from pyrogram import Client, filters, enums
p = dict(root='plugins')
from kvsqlite.sync import Client

db = Client("data.sqlite", 'fuck')
if not db.exists("admin_list"):
    db.set('admin_list', [5927744467,5927744467])
if not db.exists("sessions"):
    db.set('sessions', [])
if not db.exists("ban_list"):
    db.set("ban_list", [])
x = Client(name='lossclhos', api_id=28494428, api_hash='6892bbe7444d283bfa9f81fbe090b385', bot_token='1695705994:AAHFxL6TV10RFIUEv12IcEKGBLAqAGFl_6g', workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)
alive()
x.run()
