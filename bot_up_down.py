import telebot
import time
import wget
token =
bot = telebot.TeleBot(token)
dir=r'C:\Users\zol\Desktop\filedatelegram'


@bot.message_handler(commands=['help','start'])
def send_welcome(msg):
    id=msg.chat.id
    bot.send_message(id,"ciao sono Trybot")

@bot.message_handler(commands=['stop'])
def send_stop(msg):
    bot.send_message(msg.chat.id,"mi stoppo ")
    bot.stop_bot()

@bot.message_handler(func=lambda message:True, content_types=['photo'])
def send_risp(msg):
    bot.send_message(msg.chat.id,'ricevuta foto '+str(msg.id))
    photo_id=msg.photo[-1].file_id
    remote_url=bot.get_file_url(photo_id)
    wget.download(remote_url,r'C:\Users\zol\Desktop\filedatelegram')
    bot.send_message(msg.chat.id,'scaricata foto '+ str(msg.id))

@bot.message_handler(func=lambda message:True, content_types=['video'])
def send_risp(msg):
    bot.send_message(msg.chat.id,'ricevuto video '+str(msg.id))
    video_id=msg.video.file_id
    remote_url=bot.get_file_url(video_id)
    wget.download(remote_url,r'C:\Users\zol\Desktop\filedatelegram')
    bot.send_message(msg.chat.id,'scaricato video '+str(msg.id))

@bot.message_handler(func=lambda message:True, content_types=['document'])
def send_risp(msg):
    bot.send_message(msg.chat.id,'ricevuto documento'+str(msg.id))
    document_id=msg.document.file_id
    remote_url=bot.get_file_url(document_id)
    wget.download(remote_url,r'C:\Users\zol\Desktop\filedatelegram')
    bot.send_message(msg.chat.id,'scaricato documento '+str(msg.id))

@bot.message_handler(func=lambda message:True, content_types=['audio'])
def send_risp(msg):
    bot.send_message(msg.chat.id,'ricevuto audio'+str(msg.id))
    audio_id=msg.document.file_id
    remote_url=bot.get_file_url(audio_id)
    wget.download(remote_url,r'C:\Users\zol\Desktop\filedatelegram')
    bot.send_message(msg.chat.id,'scaricato audio '+str(msg.id))

#@bot.message_handler(commands=['codicefiscale'])
#def send_invio(msg):
#    bot.send_photo(msg.chat.id,photo=open((picCF),'rb'))

#@bot.message_handler(commands=['patente'])
#def send_invio(msg):
#    bot.send_photo(msg.chat.id,photo=open((picPG),'rb'))

#@bot.message_handler(commands=['greepass'])
#def send_invio(msg):
#    bot.send_photo(msg.chat.id,photo=open((picGP),'rb'))
bot.polling()

