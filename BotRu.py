# 601427286:AAFkJz9Qz-F2A41xS4JGVjF3mU-CyE8S7B4

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging
from ApiRu import ApiRu

# Ativar Registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__) 
api = ApiRu()

def iniciar(bot, update):
    user = update.message.from_user
    # reply_keyboard = [['Cardápio', 'Sobre']]
    update.message.reply_text('Oi! Quer saber o cardápio de qual dia? \n\n/segunda \n/terca \n/quarta \n/quinta \n/sexta \n\n/sobre')
    logger.info("Usuário %s iniciou o bot.", user.first_name)
    # return 0

def segunda(bot, update):
    update.message.reply_text('Estou olhando o cardápio de segunda, espera aí...')
    cardapio = api.getPalmasSegunda()
    update.message.reply_text('{}'.format(cardapio))

def terca(bot, update):
    update.message.reply_text('Estou olhando o cardápio de terça, espera aí...')
    cardapio = api.getPalmasTerca()
    update.message.reply_text('{}'.format(cardapio))

def quarta(bot, update):
    update.message.reply_text('Estou olhando o cardápio de quarta, espera aí...')
    cardapio = api.getPalmasQuarta()
    update.message.reply_text('{}'.format(cardapio))

def quinta(bot, update):
    update.message.reply_text('Estou olhando o cardápio de quinta, espera aí...')
    cardapio = api.getPalmasQuinta()
    update.message.reply_text('{}'.format(cardapio))

def sexta(bot, update):
    update.message.reply_text('Estou olhando o cardápio de sexta, espera aí...')
    cardapio = api.getPalmasSexta()
    update.message.reply_text('{}'.format(cardapio))

def escolha(bot, update):
    reply_keyboard = [['Almoço', 'Jantar']]

    update.message.reply_text(
        'Qual a refeição?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

# def menu(bot, update):
#     update.message.reply_text('Menu de opções')
    # return 1

# def cardapio(bor, update):
#     update.message.reply_text('Estou olhando o cardápio, espera aí...')
#     texto = api.getCardapioPalmas()
#     update.message.reply_text('{}'.format(texto))

def sobre(bor, update):
    update.message.reply_text('Kleyson me criou com o propósito de dominar o mundo.')

def cancelar(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Criando o EventHandler e informando o token do bot.
    updater = Updater("601427286:AAFkJz9Qz-F2A41xS4JGVjF3mU-CyE8S7B4")

    # Obter o despachante para registrar manipuladores
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", iniciar))
    # dp.add_handler(CommandHandler("cardapio", cardapio))
    dp.add_handler(CommandHandler("sobre", sobre))

    dp.add_handler(CommandHandler("segunda", segunda))
    dp.add_handler(CommandHandler("terca", terca))
    dp.add_handler(CommandHandler("quarta", quarta))
    dp.add_handler(CommandHandler("quinta", quinta))
    dp.add_handler(CommandHandler("sexta", sexta))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()