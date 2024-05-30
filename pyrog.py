import re
from util import remove_duplicates
from list_of_channel import l_o_ch
from pyrogram import Client
from loadenv import *

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

final = ""


app_pyrogram = Client("my_account", api_id=api_id, api_hash=api_hash)

salavati = """#profile-title: base64:8J+RkfCflKXimqHvuI9TYWxhdmF0aS1GYXN08J+Nu/Cfjrjwn4+04oCN4pig77iP
#profile-update-interval: 1
#subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
#support-url: https://github.com/Mohammad5-M/
#profile-web-page-url: https://github.com/Mohammad5-M/


"""

def main():
    app_pyrogram.start()

    global final
    vless_or_vmess = ""
    final = ""
    
    for message in app_pyrogram.search_global("vless://", limit=50):
        if message.text is not None:
            vless_or_vmess = vless_or_vmess + message.text + "\n"
    for message in app_pyrogram.search_global("vmess://", limit=50):
        if message.text is not None:
            vless_or_vmess = vless_or_vmess + message.text + "\n"

    r = re.findall(r"vmess\:\/\/.*", vless_or_vmess)
    r = remove_duplicates(r, len(r))
    final = final + "{}".format("\n".join(r[1:]))
    r = re.findall(r"vless\:\/\/.*", vless_or_vmess)
    r = remove_duplicates(r, len(r))
    final = final + "{}".format("\n".join(r[1:]))

    app_pyrogram.stop()
    return salavati + final


def main2():
    app_pyrogram.start()

    global final
    vless_or_vmess = ""
    final = ""
    
    for i in l_o_ch:
        for message in app_pyrogram.search_messages(i, "vless://", limit=4):
            if message.text is not None:
                vless_or_vmess = vless_or_vmess + message.text + "\n"
        for message in app_pyrogram.search_messages(i, "vmess://", limit=4):
            if message.text is not None:
                vless_or_vmess = vless_or_vmess + message.text + "\n"
    r = re.findall(r"vmess\:\/\/.*", vless_or_vmess)
    r = remove_duplicates(r, len(r))
    final = final + "{}".format("\n".join(r[1:]))
    r = re.findall(r"vless\:\/\/.*", vless_or_vmess)
    r = remove_duplicates(r, len(r))
    final = final + "{}".format("\n".join(r[1:]))

    app_pyrogram.stop()
    return salavati + final
