import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#İklim değişikliğiyle ilgili kısa ve olabildiğince öz bilgiler bilgiler. Bu sayede insanlar yeni bilgiler öğrenir.
id_bilgi = [
    "Son 200 yıl içinde atmosferdeki karbondioksit seviyesi %40 arttı.",
    "Küresel sıcaklıklar 1880'den bu yana 1.2°C arttı.",
    "Buzullar 1994'ten bu yana her yıl ortalama 400 milyar ton buz kaybediyor.",
    "Deniz seviyeleri yılda yaklaşık 3.3 mm yükseliyor.",
    "İklim değişikliği, mercan resiflerinin %70'ini tehdit ediyor."
]

#Meme linkleri
id_meme = [
    "https://imgix.bustle.com/lovelace/uploads/1055/dba34200-2841-0133-775b-0aecee5a8273.jpg?w=760&h=508&fit=crop&crop=faces&auto=format%2Ccompress&q=50&dpr=2",
    "https://th.bing.com/th/id/OIP.i_4R4zwt-jxIX3MgkLLDwwHaE6?pid=ImgDet&w=474&h=314&rs=1",
    "https://th.bing.com/th/id/OIP.ui32KZdbK9Z41VklN1fT5wAAAA?rs=1&pid=ImgDetMain",
    "https://th.bing.com/th/id/OIP.vQXsmHB42PvgcnUR8kFdkAHaLQ?rs=1&pid=ImgDetMain",
    "https://th.bing.com/th/id/OIP.8sX3HuPj2MOSgzWXmX2CWgHaIQ?rs=1&pid=ImgDetMain",
    "https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/climate-change-at-the-north-pole-funny-global-warming-christmas-card-stink-pad.jpg",
    "https://th.bing.com/th/id/OIP.kONOmnX8NMyesxwJcYnAYwHaHa?rs=1&pid=ImgDetMain",
    "https://www.usnews.com/dims4/USNEWS/1345302/2147483647/resize/1200x%3E/quality/85/?url=https:%2F%2Fmedia.beam.usnews.com%2F49%2F54%2F71a76fc443379d5c23bd9f2e65e6%2Fkn022820dapc.jpg",
    "https://th.bing.com/th/id/OIP.MfSB35lKYNGkx5PT6TZjXgHaFC?rs=1&pid=ImgDetMain",
    "https://th.bing.com/th/id/OIP.lAtRYAjfUOuAM5ggFLDMUAHaFj?rs=1&pid=ImgDetMain",
]

#Botun cevap verdiği kodlar.
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!gw') or message.content.startswith('!id'):
        response_type = random.choice(["fact", "meme"])
        if response_type == "fact":
            fact = random.choice(id_bilgi)
            await message.channel.send(f"🌍 İklim Değişikliği Bilgisi: {fact}")
        elif response_type == "meme":
            meme = random.choice(id_meme)
            await message.channel.send(f"🌍 İklim Değişikliği Meme:\n{meme}")

client.run("token")