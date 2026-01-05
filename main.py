from pyrogram import Client, filters
from pyrogram.types import Message

BOT_TOKEN = "8433474851:AAGFt_WZ2agAWcM-UVmLxzhSrH-aySkIcaw"
API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"

app = Client(
    "name",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# ================= NAME FONT =================
FONT_MAP = {
    "a": "ᴧ","b":"ʙ","c":"ᴄ","d":"ᴅ","e":"є","f":"ғ","g":"ɢ","h":"ʜ","i":"ɪ",
    "j":"ᴊ","k":"ᴋ","l":"ʟ","m":"ϻ","n":"η","o":"σ","p":"ᴘ","q":"ǫ","r":"ꝛ",
    "s":"s","t":"ᴛ","u":"υ","v":"ᴠ","w":"ᴡ","x":"x","y":"ʏ","z":"ᴢ",
    "A":"𝐀","B":"𝐁","C":"𝐂","D":"𝐃","E":"𝐄","F":"𝐅","G":"𝐆",
    "H":"𝐇","I":"𝐈","J":"𝐉","K":"𝐊","L":"𝐋","M":"𝐌","N":"𝐍",
    "O":"𝐎","P":"𝐏","Q":"𝐐","R":"𝐑","S":"𝐒","T":"𝐓","U":"𝐔",
    "V":"𝐕","W":"𝐖","X":"𝐗","Y":"𝐘","Z":"𝐙",
}

def convert(text: str) -> str:
    return "".join(FONT_MAP.get(ch, ch) for ch in text)

# ================= BIO FONT =================
BIO_FONT_MAP = {
    "a":"ɑ","b":"ß","c":"c","d":"d","e":"ə","f":"f","g":"ɢ","h":"h",
    "i":"ı","j":"j","k":"k","l":"ɭ","m":"ɱ","n":"η","o":"❍","p":"ρ",
    "q":"q","r":"r","s":"σ","t":"ʈ","u":"ʋ","v":"ʋ","w":"w","x":"x",
    "y":"γ","z":"z",
    "A":"ɑ","B":"ß","C":"C","D":"D","E":"E","F":"F","G":"G",
    "H":"H","I":"ı","J":"J","K":"K","L":"L","M":"M","N":"N",
    "O":"❍","P":"P","Q":"Q","R":"R","S":"S","T":"ʈ","U":"ʋ",
    "V":"ʋ","W":"W","X":"X","Y":"Y","Z":"Z",
}

def bio_convert(text: str) -> str:
    return "".join(BIO_FONT_MAP.get(ch, ch) for ch in text)

# ================= BIO STYLES =================
BIO_STYLES = [
    ("", " ⚠️🕸️☆°•____"),
    ("𓆩🖤⃝ ", " 🕯☠"),
    ("◄⏤ ", " ⏤►🩸"),
    ("𓆩🔥 ", " 👑𓆪"),
    ("✦ ", " ✦"),
    ("⛧ ", " ☠"),
]

# ================= NAME STYLES (AS GIVEN) =================
STYLES = [  # (same list tumhari wali, untouched)
    ("𓂃❛ ⟶", "❜ 🌙⤹🌸"),
    ("❍⏤●", "●───♫▷"),
    ("🤍 ⍣⃪ ᶦ ᵃᵐ⛦⃕", "❛𝆺𝅥⤹࿗𓆪ꪾ™"),
    # 🔥 baki sab tumhare styles yahin rahenge (unchanged)
]

# ================= /name =================
@app.on_message(filters.command("name"))
async def stylish_name(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /name your_name")

    text = convert(" ".join(message.command[1:]))

    out = "𓆩 𝐒ᴛʏʟɪꜱʜ 𝐍ᴀᴍᴇ 𓆪\n\n"
    for pre, suf in STYLES:
        out += f"{pre}{text}{suf}\n\n"

    await message.reply_text(out)

# ================= /bio =================
@app.on_message(filters.command("bio"))
async def bio_style(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /bio your normal bio text")

    text = " ".join(message.command[1:])
    fancy = bio_convert(text)

    out = "𓆩 𝐁ɪᴏ ꜱᴛʏʟᴇ 𓆪\n\n"
    for pre, suf in BIO_STYLES:
        out += f"{pre}{fancy}{suf}\n\n"

    await message.reply_text(out)

app.run()
