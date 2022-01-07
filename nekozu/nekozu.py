import telebot,requests
token = "Token botmu"
bot = telebot.TeleBot(token=token,threaded=False)



def simsimi(text):
	response = requests.get(f"https://api.simsimi.net/v2/?text={text}&lang=id")
	results = response.json()
	return results["success"]

@bot.message_handler(commands=["start"])
def welcome(message):
	# print(message)
	nama = message.from_user.first_name
	pesan = f"Halo {nama} apa kabar? 😄"
	bot.send_message(message.from_user.id,pesan)

@bot.message_handler(func=lambda msg: msg.text is not None)
def other(message):
	pesan = simsimi(message.text)
	bot.reply_to(message,pesan)

if __name__ == '__main__':
	print("Nekozu Siap Dipakai..")
	# bot.polling()
	while True:
		try:
			bot.polling()
		except Exception as e:
			bot.stop_polling()
