import telebot, jsonpickle, subprocess

API_KEY = '123:abc'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact'])

def main (message):
    Updates = {}
    Updates['message'] = message.json
    encode = jsonpickle.encode(Updates)
    
    command = subprocess.Popen(['php', 'bot.php', format(encode)])

bot.polling()

# >> @api_tele