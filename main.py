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
    "a":"ᴧ","b":"ʙ","c":"ᴄ","d":"ᴅ","e":"є","f":"ғ","g":"ɢ","h":"ʜ","i":"ɪ",
    "j":"ᴊ","k":"ᴋ","l":"ʟ","m":"ϻ","n":"η","o":"σ","p":"ᴘ","q":"ǫ","r":"ꝛ",
    "s":"s","t":"ᴛ","u":"υ","v":"ᴠ","w":"ᴡ","x":"x","y":"ʏ","z":"ᴢ",
    "A":"𝐀","B":"𝐁","C":"𝐂","D":"𝐃","E":"𝐄","F":"𝐅","G":"𝐆",
    "H":"𝐇","I":"𝐈","J":"𝐉","K":"𝐊","L":"𝐋","M":"𝐌","N":"𝐍",
    "O":"𝐎","P":"𝐏","Q":"𝐐","R":"𝐑","S":"𝐒","T":"𝐓","U":"𝐔",
    "V":"𝐕","W":"𝐖","X":"𝐗","Y":"𝐘","Z":"𝐙",
}

def convert(text: str) -> str:
    return "".join(FONT_MAP.get(ch, ch) for ch in text)

# ================= BEST SINGLE BIO FONT (YR WALI) =================
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

def bio_single_convert(text: str) -> str:
    return "".join(BIO_FONT_MAP.get(ch, ch) for ch in text)

# ================= MULTI BIO FONTS =================
BIO_FONTS = [

    # NickFinder clean
    {
        "a":"ɑ","b":"ß","c":"c","d":"d","e":"ə","f":"f","g":"ɢ","h":"h",
        "i":"ı","l":"ɭ","m":"ɱ","n":"η","o":"❍","p":"ρ",
        "r":"r","s":"σ","t":"ʈ","u":"ʋ","v":"ʋ","w":"w","y":"γ",
    },

    # Small caps
    {
        "a":"ᴀ","b":"ʙ","c":"ᴄ","d":"ᴅ","e":"ᴇ","f":"ғ","g":"ɢ","h":"ʜ",
        "i":"ɪ","j":"ᴊ","k":"ᴋ","l":"ʟ","m":"ᴍ","n":"ɴ","o":"ᴏ","p":"ᴘ",
        "r":"ʀ","s":"s","t":"ᴛ","u":"ᴜ","v":"ᴠ","w":"ᴡ","y":"ʏ",
    },

    # Cute
    {
        "a":"α","b":"в","d":"∂","e":"є","f":"ƒ","h":"н",
        "i":"ι","l":"ℓ","m":"м","n":"η","o":"σ","p":"ρ",
        "r":"я","s":"ѕ","t":"т","u":"υ","w":"ω","y":"у",
    },

    # Dark
    {
        "a":"Δ","b":"β","d":"Ð","e":"Ξ","f":"Ғ","h":"Ħ",
        "i":"Ɨ","l":"Ł","m":"₥","n":"₦","o":"Ø","p":"Ᵽ",
        "r":"Ɽ","s":"Ϟ","t":"Ŧ","u":"Ʉ","w":"₩","y":"Ɏ",
    },
]

def bio_convert(text: str, font: dict) -> str:
    return "".join(font.get(ch.lower(), ch) for ch in text)

# ================= NAME STYLES =================
STYLES = [
    ("𓂃❛ ⟶", "❜ 🌙⤹🌸"),
    ("❍⏤●", "●───♫▷"),
    ("🤍 ⍣⃪ ᶦ ᵃᵐ⛦⃕", "❛𝆺𝅥⤹࿗𓆪ꪾ™"),
]

# ================= /name =================
@app.on_message(filters.command("name"))
async def stylish_name(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /name your name")

    text = convert(" ".join(message.command[1:]))

    out = "𓆩 𝐒ᴛʏʟɪꜱʜ 𝐍ᴀᴍᴇ 𓆪\n\n"
    for pre, suf in STYLES:
        out += f"{pre}{text}{suf}\n\n"

    await message.reply_text(out)

# ================= /bio =================
@app.on_message(filters.command("bio"))
async def bio_style(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/bio your text\n/bio single your text"
        )

    # /bio single
    if message.command[1].lower() == "single":
        if len(message.command) < 3:
            return await message.reply_text("Usage: /bio single your text")

        text = " ".join(message.command[2:])
        fancy = bio_single_convert(text)

        await message.reply_text(
            f"𓆩 𝐁ɪᴏ ꜱɪɴɢʟᴇ 𓆪\n\n"
            f"{fancy} ⚠️🕸️☆°•____"
        )
        return

    # /bio (multiple)
    text = " ".join(message.command[1:])
    out = "𓆩 𝐁ɪᴏ ꜱᴛʏʟᴇ 𓆪\n\n"

    for font in BIO_FONTS:
        fancy = bio_convert(text, font)
        out += f"{fancy} ⚠️🕸️☆°•____\n\n"

    await message.reply_text(out)

app.run()
