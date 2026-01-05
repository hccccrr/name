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

# ================= BIO FONTS (REAL DIFFERENT STYLES) =================
BIO_FONTS = [

    # Style 1 – NickFinder clean
    {
        "a":"ɑ","b":"ß","c":"c","d":"d","e":"ə","f":"f","g":"ɢ","h":"h",
        "i":"ı","j":"j","k":"k","l":"ɭ","m":"ɱ","n":"η","o":"❍","p":"ρ",
        "r":"r","s":"σ","t":"ʈ","u":"ʋ","v":"ʋ","w":"w","y":"γ",
    },

    # Style 2 – small caps
    {
        "a":"ᴀ","b":"ʙ","c":"ᴄ","d":"ᴅ","e":"ᴇ","f":"ғ","g":"ɢ","h":"ʜ",
        "i":"ɪ","j":"ᴊ","k":"ᴋ","l":"ʟ","m":"ᴍ","n":"ɴ","o":"ᴏ","p":"ᴘ",
        "r":"ʀ","s":"s","t":"ᴛ","u":"ᴜ","v":"ᴠ","w":"ᴡ","y":"ʏ",
    },

    # Style 3 – cute / readable
    {
        "a":"α","b":"в","c":"c","d":"∂","e":"є","f":"ƒ","g":"g","h":"н",
        "i":"ι","k":"к","l":"ℓ","m":"м","n":"η","o":"σ","p":"ρ",
        "r":"я","s":"ѕ","t":"т","u":"υ","w":"ω","y":"у",
    },

    # Style 4 – dark bio
    {
        "a":"Δ","b":"β","d":"Ð","e":"Ξ","f":"Ғ","g":"Ǥ","h":"Ħ",
        "i":"Ɨ","k":"Ҡ","l":"Ł","m":"₥","n":"₦","o":"Ø","p":"Ᵽ",
        "r":"Ɽ","s":"Ϟ","t":"Ŧ","u":"Ʉ","w":"₩","y":"Ɏ",
    },

    # Style 5 – mix stylish
    {
        "a":"ä","b":"ɓ","c":"ç","d":"đ","e":"ë","f":"ƒ","g":"ğ","h":"ħ",
        "i":"ï","k":"ķ","l":"ł","m":"ɱ","n":"ñ","o":"ö","p":"ρ",
        "r":"ř","s":"ş","t":"ţ","u":"ü","w":"ω","y":"ÿ",
    },
]

def bio_convert(text: str, font: dict) -> str:
    return "".join(font.get(ch.lower(), ch) for ch in text)

# ================= NAME STYLES (AS YOU GAVE) =================
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

# ================= /bio (NEW SYSTEM) =================
@app.on_message(filters.command("bio"))
async def bio_style(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /bio your normal bio text")

    text = " ".join(message.command[1:])

    out = "𓆩 𝐁ɪᴏ ꜱᴛʏʟᴇ 𓆪\n\n"

    for font in BIO_FONTS:
        fancy = bio_convert(text, font)
        out += f"{fancy} ⚠️🕸️☆°•____\n\n"

    await message.reply_text(out)

app.run()
