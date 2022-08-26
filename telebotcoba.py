import telebot
from BotResponseTime import get_response_time
from telebot import apihelper
from SRBOT import succes_rate
from CeriaRegister import get_register
from CeriaLogin import get_login
from CeriaApplyLoan import get_loan
from CeriaCreditActivation import get_activation
from CeriaProfile import get_profile
from CeriaProfileChangePin import get_changepin
from CeriaProfileForgotPin import get_forgotpin
from CeriaBill import get_bill
from CeriaInstallment import get_installment
from CeriaMerchantPayment import get_merchant
from CeriaCashout import get_cashout




apihelper.proxy = {"http":"http://proxy1.bri.co.id:1707", "https":"http://proxy1.bri.co.id:1707"}

api = "5174902194:AAGLYeuWWY-8lJwxTBwRF9-Ri2w-2Ep1dl4"
bot = telebot.TeleBot(api)

#response = requests.post(url, data=json.dumps(slack_data), headers=headers, proxies=proxy)
#proxy = { "http":"http://proxy1.bri.co.id:1707", "https":"http://proxy1.bri.co.id:1707" }

# handle commands, /start
@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Halo Tim monitoring")

@bot.message_handler(commands=['ceria_succes_rate'])
def handle_command1(message):
    bot.reply_to(message, succes_rate())

@bot.message_handler(commands=['ceria_respond_time'])
def handle_command3(message):
    bot.reply_to(message, get_response_time())

@bot.message_handler(commands=['ceria_respond_code'])
def handle_command2(message):
    bot.reply_to(message, get_register())
    bot.reply_to(message, get_login())
    bot.reply_to(message, get_loan())
    bot.reply_to(message, get_activation())
    bot.reply_to(message, get_profile())
    bot.reply_to(message, get_changepin())
    bot.reply_to(message, get_forgotpin())
    bot.reply_to(message, get_bill())
    bot.reply_to(message, get_installment())
    bot.reply_to(message, get_merchant())
    bot.reply_to(message, get_cashout())


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
	bot.send_message(message, message.text)
 
bot.polling()