# 601427286:AAFkJz9Qz-F2A41xS4JGVjF3mU-CyE8S7B4
'''
Olá, a hora do (almoço/jantar) está próxima! Gostaria de saber qual é o cardápio de hoje? Tenho certeza que a comida estará maravilhosa 😜. Se quiser, também posso te passar umas informações sobre os RUs da UFT.
HOJE       OUTRO_DIA        INFOS

-> caso ainda seja horário de almoço
—— exibe cardápio almoço, aí se já tiver cadastrado o jantar:
Quer saber sobre o jantar também? Se eu fosse você, não perderia por nada!! 😱🍽
SIM 😍      AGORA_NÃO

-> caso selecione outro dia
Diz aí o cardápio de qual dia da semana você quer dar uma espiadinha 👀
SEG    TER    QUA    QUI    SEX

-> caso não esteja disponível
Ainda não me passaram quais serão os pratos. Mas volta mais tarde que eu te falo, e se brincar a gente ainda se encontra lá 😄✌🏼
'''

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, CallbackQueryHandler)

import logging
from ApiRu import ApiRu

# Ativar Registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__) 
api = ApiRu()

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def iniciar(bot, update):
    opcoes = [['/hoje', '/outro_dia'], ['/INFOS']]
    user = update.message.from_user
    logger.info("Usuário %s iniciou o bot.", user.first_name)
    update.message.reply_text('Olá {0}, {1}'.format(user.first_name, api.refeicao), reply_markup=ReplyKeyboardMarkup(opcoes, 
        one_time_keyboard=True, resize_keyboard=True))

def ru_hoje(bot, update):
    update.message.reply_text('Estou olhando o cardápio de hoje, espera aí...')
    cardapio = api.getHoje()
    update.message.reply_text('{}'.format(cardapio))

def ru_outro_dia(bot, update):
    opcoes = [['/segunda'], ['/terca'], ['/quarta'], ['/quinta'], ['/sexta']]
    update.message.reply_text('Me diz aí qual dia você quer saber', reply_markup=ReplyKeyboardMarkup(opcoes, 
        one_time_keyboard=True, resize_keyboard=True))

def segunda(bot, update):
    update.message.reply_text('Estou olhando o cardápio de segunda, espera aí...')
    cardapio = api.getPalmasSegunda(completo=True)
    update.message.reply_text('{}'.format(cardapio))

def terca(bot, update):
    update.message.reply_text('Estou olhando o cardápio de terça, espera aí...')
    cardapio = api.getPalmasTerca(completo=True)
    update.message.reply_text('{}'.format(cardapio))

def quarta(bot, update):
    update.message.reply_text('Estou olhando o cardápio de quarta, espera aí...')
    cardapio = api.getPalmasQuarta(completo=True)
    update.message.reply_text('{}'.format(cardapio))

def quinta(bot, update):
    update.message.reply_text('Estou olhando o cardápio de quinta, espera aí...')
    cardapio = api.getPalmasQuinta(completo=True)
    update.message.reply_text('{}'.format(cardapio))

def sexta(bot, update):
    update.message.reply_text('Estou olhando o cardápio de sexta, espera aí...')
    cardapio = api.getPalmasSexta(completo=True)
    update.message.reply_text('{}'.format(cardapio))

def sobre(bor, update):
    update.message.reply_text('Kleyson e Paulo me criaram com o propósito de dominar o mundo.')

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

    dp.add_handler(CommandHandler("hoje", ru_hoje))
    dp.add_handler(CommandHandler("outro_dia", ru_outro_dia))
    dp.add_handler(CommandHandler("INFOS", sobre))
    dp.add_handler(CommandHandler("segunda", segunda))
    dp.add_handler(CommandHandler("terca", terca))
    dp.add_handler(CommandHandler("quarta", quarta))
    dp.add_handler(CommandHandler("quinta", quinta))
    dp.add_handler(CommandHandler("sexta", sexta))

    # updater.dispatcher.add_handler(CallbackQueryHandler(button))

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