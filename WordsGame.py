import telebot
import random
import json

token = "5372417597:AAFO1bYnI69aHwFaI8nSVTRq2QGRj4uOQLk"
bot = telebot.TeleBot(token, parse_mode=None)

data = ""
with open('DictionaryVerified.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())
        data += line.strip()
dictionary = json.loads(data)
print("Datatype after deserialization : " + str(type(data)))
# print("-" * 20)
# word, definition = random.choice(list(dictionary.items()))
# print(word)
# print(definition)

@bot.message_handler(commands=['start'])
def welcome_message(message):
	bot.send_message(message.from_user.id, 'Hey! If you want to play just press /RandomWord.')
	print(f"Recieved message from {message.from_user.username} : {message.from_user.first_name} {message.from_user.last_name}")

@bot.message_handler(commands=['RandomWord'])
def welcome_message(message):
	word, definition = random.choice(list(dictionary.items()))
	bot.send_message(message.from_user.id, f"{word} - \n{definition}")
	print(f"Recieved message from {message.from_user.username} : {message.from_user.first_name} {message.from_user.last_name}")

print("Bot started.")
print("#" * 20)

bot.polling(none_stop = True)