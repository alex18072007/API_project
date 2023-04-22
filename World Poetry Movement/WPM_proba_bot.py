import telebot
from telebot import types
import sqlite3


bot = telebot.TeleBot('6142973414:AAHKHtoFcR7sKtZvf_13OL_H_u2-F9idcaA')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='🇷🇺 Русский')
    btn2 = types.KeyboardButton(text='🇬🇧 English')
    btn3 = types.KeyboardButton('🇪🇸 Español')
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, '🇷🇺 Чтобы начать, выберите язык / 🇬🇧 To get started, select a language'
                                      ' / 🇪🇸 Para empezar, seleccione el idioma',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_message(message):

    #Русский язык
    if message.text == '🇷🇺 Русский':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='📰 Биография поэтов мира')
        btn2 = types.KeyboardButton(text='🔎 Наш сайт')
        btn3 = types.KeyboardButton(text='🔙 Вернуться к выбору языка')
        btn4 = types.KeyboardButton(text='📜 Поэзия поэтов мира')
        keyboard.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, '👋 Вас приветствует бот сайта WorldPoetryMovement', reply_markup=keyboard)
        bot.send_message(message.chat.id, '👀 Выберите интересующий вас раздел')

    elif message.text == '🔙 Вернуться к выбору языка':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        btn3 = types.KeyboardButton('🇪🇸 Español')
        keyboard.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, '🇷🇺 Чтобы начать, выберите язык / 🇬🇧 To get started, select a language'
                                          ' / 🇪🇸 Para empezar, seleccione el idioma',
                         reply_markup=keyboard)

    elif message.text == '🔎 Наш сайт':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, '📲 Перейти на наш официальный сайт по' +
                                          ' [ссылке](https://worldpoetrymovement.org/)', reply_markup=keyboard)

    elif message.text == '🔙 Главное меню':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='📰 Биография поэтов мира')
        btn2 = types.KeyboardButton(text='🔎 Наш сайт')
        btn3 = types.KeyboardButton(text='🔙 Вернуться к выбору языка')
        btn4 = types.KeyboardButton(text='📜 Поэзия поэтов мира')
        keyboard.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, '👀 Выберите интересующий вас раздел', reply_markup=keyboard)

    elif message.text == '📜 Поэзия поэтов мира':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        btn2 = types.KeyboardButton(text='_Вадим Терёхин_')
        btn3 = types.KeyboardButton(text='_Фернандо Рендон_')
        btn4 = types.KeyboardButton(text='_Рати Саксена_')
        btn5 = types.KeyboardButton(text='_Атаол Бехрамоглу_')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Выберите интересующего вас поэта', reply_markup=keyboard)

    elif message.text == '_Атаол Бехрамоглу_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Поэзия поэта',
                                          url='https://reading-hall.ru/publication.php?id=9115')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'АТАОЛ БЕХРАМОГЛУ', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Здесь можно ознакомиться с поэзией и творчеством данного поэта...',
                         reply_markup=board)

    elif message.text == '_Рати Саксена_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Поэзия поэта',
                                          url='https://www.poemhunter.com/rati-saxena/')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'РАТИ САКСЕНА', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Здесь можно ознакомиться с поэзией и творчеством данного поэта...',
                         reply_markup=board)

    elif message.text == '_Фернандо Рендон_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Поэзия поэта',
                                          url='https://www.poemhunter.com/fernando-rend-n/')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'ФЕРНАНДО РЕНДОН', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Здесь можно ознакомиться с поэзией и творчеством данного поэта...',
                         reply_markup=board)

    elif message.text == '_Вадим Терёхин_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Поэзия поэта',
                                          url='https://reading-hall.ru/publication.php?id=12479')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'ВАДИМ ТЕРЁХИН', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Здесь можно ознакомиться с поэзией и творчеством данного поэта...',
                         reply_markup=board)

    elif message.text == '📰 Биография поэтов мира':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        btn2 = types.KeyboardButton(text='Вадим Терёхин')
        btn3 = types.KeyboardButton(text='Фернандо Рендон')
        btn4 = types.KeyboardButton(text='Рати Саксена')
        btn5 = types.KeyboardButton(text='Атаол Бехрамоглу')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Выберите интересующего вас поэта', reply_markup=keyboard)

    elif message.text == 'Атаол Бехрамоглу':
        photo = open('photo/Ataol-Behramoglu.jpg', 'rb')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 Подробнее...',
                                          url='https://translated.turbopages.org/proxy_u/en-ru.ru.72bef0e3-643a53e0-41debe5e-74722d776562/https/en.wikipedia.org/wiki/Ataol_Behramoğlu')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_v = cur.execute('SELECT two FROM poetry WHERE id = 10').fetchone()
        bot.send_message(message.chat.id, poetry_v)
        bot.send_message(message.chat.id, '📲 Здесь можно прочитать полную биографию данного поэта...',
                         reply_markup=board)

    elif message.text == 'Рати Саксена':
        photo = open('photo/Рати фото IMG-20220108-WA0025 (1).jpg', 'rb')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 Подробнее...',
                                          url='https://jaipurliteraturefestival.org/speaker/rati-saxena')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_v = cur.execute('SELECT two FROM poetry WHERE id = 7').fetchone()
        bot.send_message(message.chat.id, poetry_v)
        bot.send_message(message.chat.id, '📲 Здесь можно прочитать полную биографию данного поэта...',
                         reply_markup=board)

    elif message.text == 'Фернандо Рендон':
        photo = open('photo/Фернандо Рендон!.jpg', 'rb')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 Подробнее...',
                                          url='https://es.wikipedia.org/wiki/Fernando_Rend%C3%B3n')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_v = cur.execute('SELECT two FROM poetry WHERE id = 4').fetchone()
        bot.send_message(message.chat.id, poetry_v)
        bot.send_message(message.chat.id, '📲 Здесь можно прочитать полную биографию данного поэта...',
                         reply_markup=board)

    elif message.text == 'Вадим Терёхин':
        photo = open('photo/Vadim.jpg', 'rb')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 Подробнее...',
                                          url='https://ru.wikipedia.org/wiki/Терёхин,_Вадим_Фёдорович')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Главное меню')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_v = cur.execute('SELECT two FROM poetry WHERE id = 1').fetchone()
        bot.send_message(message.chat.id, poetry_v)
        bot.send_message(message.chat.id, '📲 Здесь можно прочитать полную биографию данного поэта...',
                         reply_markup=board)

    #English Language
    elif message.text == '🇬🇧 English':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='📰 Biography of poets of the world')
        btn2 = types.KeyboardButton(text='🔎 Our website')
        btn3 = types.KeyboardButton(text='🔙 Back to language selection')
        btn4 = types.KeyboardButton(text='📜 Poetry of the poets of the world')
        keyboard.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, '👋 You are welcomed by the bot for the WorldPoetryMovement website',
                         reply_markup=keyboard)
        bot.send_message(message.chat.id, '👀 Select the section you are interested in')

    elif message.text == '🔙 Back to language selection':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        btn3 = types.KeyboardButton('🇪🇸 Español')
        keyboard.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, '🇷🇺 Чтобы начать, выберите язык / 🇬🇧 To get started, select a language'
                                          ' / 🇪🇸 Para empezar, seleccione el idioma',
                         reply_markup=keyboard)

    elif message.text == '📜 Poetry of the poets of the world':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        btn2 = types.KeyboardButton(text='_Vadim Terehin_')
        btn3 = types.KeyboardButton(text='_Fernando Rendon_')
        btn4 = types.KeyboardButton(text='_Rati Saxena_')
        btn5 = types.KeyboardButton(text='_Ataol Behramoglu_')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Choose the poet you are interested in', reply_markup=keyboard)

    elif message.text == '_Ataol Behramoglu_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Poetry of the poet',
                                          url='https://reading-hall.ru/publication.php?id=9115')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'ATAOL BEHRAMOGLU', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Here you can get acquainted with'
                                          ' the poetry and creativity of this poet...',
                         reply_markup=board)

    elif message.text == '_Rati Saxena_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Poetry of the poet',
                                          url='https://www.poemhunter.com/rati-saxena/')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'RATI SAXENA', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Here you can get acquainted with'
                                          ' the poetry and creativity of this poet...',
                         reply_markup=board)

    elif message.text == '_Fernando Rendon_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Poetry of the poet',
                                          url='https://www.poemhunter.com/fernando-rend-n/')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'FERNANDO RENDON', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Here you can get acquainted with'
                                          ' the poetry and creativity of this poet...',
                         reply_markup=board)

    elif message.text == '_Vadim Terehin_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Poetry of the poet',
                                          url='https://reading-hall.ru/publication.php?id=12479')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'VADIM TEREHIN', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Here you can get acquainted with'
                                          ' the poetry and creativity of this poet...',
                         reply_markup=board)

    elif message.text == '🔎 Our website':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, '📲 Go to our official website by' +
                                          ' [link](https://worldpoetrymovement.org/)', reply_markup=keyboard)
    elif message.text == '🔙 Main menu':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='📰 Biography of poets of the world')
        btn2 = types.KeyboardButton(text='🔎 Our website')
        btn3 = types.KeyboardButton(text='🔙 Back to language selection')
        btn4 = types.KeyboardButton(text='📜 Poetry of the poets of the world')
        keyboard.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, '👀 Select the section you are interested in', reply_markup=keyboard)

    elif message.text == '📰 Biography of poets of the world':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        btn2 = types.KeyboardButton(text='Vadim Terehin')
        btn3 = types.KeyboardButton(text='Fernando Rendon')
        btn4 = types.KeyboardButton(text='Rati Saxena')
        btn5 = types.KeyboardButton(text='Ataol Behramoglu')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Choose the poet you are interested in', reply_markup=keyboard)

    elif message.text == 'Ataol Behramoglu':
        photo = open('photo/Ataol-Behramoglu.jpg', 'rb')
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 More detailed...',
                                          url='https://translated.turbopages.org/proxy_u/en-ru.ru.72bef0e3-643a53e0-41debe5e-74722d776562/https/en.wikipedia.org/wiki/Ataol_Behramoğlu')
        board.add(link)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_va = cur.execute('SELECT two FROM poetry WHERE id = 11').fetchone()
        bot.send_message(message.chat.id, poetry_va)
        bot.send_message(message.chat.id, '📲 Here you can read the full biography of this poet...',
                         reply_markup=board)

    elif message.text == 'Rati Saxena':
        photo = open('photo/Рати фото IMG-20220108-WA0025 (1).jpg', 'rb')
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 More detailed...',
                                          url='https://jaipurliteraturefestival.org/speaker/rati-saxena')
        board.add(link)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_va = cur.execute('SELECT two FROM poetry WHERE id = 8').fetchone()
        bot.send_message(message.chat.id, poetry_va)
        bot.send_message(message.chat.id, '📲 Here you can read the full biography of this poet...',
                         reply_markup=board)

    elif message.text == 'Fernando Rendon':
        photo = open('photo/Фернандо Рендон!.jpg', 'rb')
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 More detailed...',
                                          url='https://es.wikipedia.org/wiki/Fernando_Rend%C3%B3n')
        board.add(link)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_va = cur.execute('SELECT two FROM poetry WHERE id = 5').fetchone()
        bot.send_message(message.chat.id, poetry_va)
        bot.send_message(message.chat.id, '📲 Here you can read the full biography of this poet...',
                         reply_markup=board)

    elif message.text == 'Vadim Terehin':
        photo = open('photo/Vadim.jpg', 'rb')
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 More detailed...',
                                          url='https://ru.wikipedia.org/wiki/Терёхин,_Вадим_Фёдорович')
        board.add(link)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Main menu')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_va = cur.execute('SELECT two FROM poetry WHERE id = 2').fetchone()
        bot.send_message(message.chat.id, poetry_va)
        bot.send_message(message.chat.id, '📲 Here you can read the full biography of this poet...',
                         reply_markup=board)

    #Español
    if message.text == '🇪🇸 Español':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='📰 Biografía de los poetas del mundo')
        btn2 = types.KeyboardButton(text='🔎 Nuestro sitio web')
        btn3 = types.KeyboardButton(text='🔙 Volver a la selección de idioma')
        btn4 = types.KeyboardButton(text='📜 Poesía de los poetas del mundo')
        keyboard.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, '👋 Bienvenido al bot del sitio WorldPoetryMovement', reply_markup=keyboard)
        bot.send_message(message.chat.id, '👀 Seleccione la sección que le interesa')

    elif message.text == '🔙 Volver a la selección de idioma':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        btn3 = types.KeyboardButton('🇪🇸 Español')
        keyboard.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, '🇷🇺 Чтобы начать, выберите язык / 🇬🇧 To get started, select a language'
                                          ' / 🇪🇸 Para empezar, seleccione el idioma',
                         reply_markup=keyboard)

    elif message.text == '🔎 Nuestro sitio web':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, '📲 Ir a nuestro sitio web oficial' +
                                          ' [referencia](https://worldpoetrymovement.org/)', reply_markup=keyboard)

    elif message.text == '🔙 Menú principal':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='📰 Biografía de los poetas del mundo')
        btn2 = types.KeyboardButton(text='🔎 Nuestro sitio web')
        btn3 = types.KeyboardButton(text='🔙 Volver a la selección de idioma')
        btn4 = types.KeyboardButton(text='📜 Poesía de los poetas del mundo')
        keyboard.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, '👀 Seleccione la sección que le interesa', reply_markup=keyboard)

    elif message.text == '📜 Poesía de los poetas del mundo':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        btn2 = types.KeyboardButton(text='_Vadim Terekhin_')
        btn3 = types.KeyboardButton(text='_Fernrando Rendon_')
        btn4 = types.KeyboardButton(text='_Rati Saxsena_')
        btn5 = types.KeyboardButton(text='_Ataol Behramoglue_')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Elige el poeta que te interesa', reply_markup=keyboard)

    elif message.text == '_Ataol Behramoglue_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Poesía del poeta',
                                          url='https://reading-hall.ru/publication.php?id=9115')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'ATAOL BEHRAMOGLU', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Aquí puedes conocer la poesía y la obra de este poeta...',
                         reply_markup=board)

    elif message.text == '_Rati Saxsena_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Poesía del poeta',
                                          url='https://www.poemhunter.com/rati-saxena/')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'Rati Saxsena', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Aquí puedes conocer la poesía y la obra de este poeta...',
                         reply_markup=board)

    elif message.text == '_Fernrando Rendon_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Poesía del poeta',
                                          url='https://www.poemhunter.com/fernando-rend-n/')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'Fernando Rendon', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Aquí puedes conocer la poesía y la obra de este poeta...',
                         reply_markup=board)

    elif message.text == '_Vadim Terekhin_':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='📧 Poesía del poeta',
                                          url='https://reading-hall.ru/publication.php?id=12479')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'VADIM TEREKHIN', reply_markup=keyboard)
        bot.send_message(message.chat.id, '📲 Aquí puedes conocer la poesía y la obra de este poeta...',
                         reply_markup=board)

    elif message.text == '📰 Biografía de los poetas del mundo':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        btn2 = types.KeyboardButton(text='Vadim Terekhin')
        btn3 = types.KeyboardButton(text='Fernrando Rendon')
        btn4 = types.KeyboardButton(text='Rati Saxsena')
        btn5 = types.KeyboardButton(text='Ataol Behramoglue')
        keyboard.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Elige el poeta que te interesa', reply_markup=keyboard)

    elif message.text == 'Ataol Behramoglue':
        photo = open('photo/Ataol-Behramoglu.jpg', 'rb')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 Detallado...',
                                          url='https://translated.turbopages.org/proxy_u/en-ru.ru.72bef0e3-643a53e0-41debe5e-74722d776562/https/en.wikipedia.org/wiki/Ataol_Behramoğlu')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_vad = cur.execute('SELECT two FROM poetry WHERE id = 12').fetchone()
        bot.send_message(message.chat.id, poetry_vad)
        bot.send_message(message.chat.id, '📲 Aquí se puede Leer la biografía completa del poeta...',
                         reply_markup=board)

    elif message.text == 'Rati Saxsena':
        photo = open('photo/Рати фото IMG-20220108-WA0025 (1).jpg', 'rb')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 Detallado...',
                                          url='https://jaipurliteraturefestival.org/speaker/rati-saxena')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_vad = cur.execute('SELECT two FROM poetry WHERE id = 9').fetchone()
        bot.send_message(message.chat.id, poetry_vad)
        bot.send_message(message.chat.id, '📲 Aquí se puede Leer la biografía completa del poeta...',
                         reply_markup=board)

    elif message.text == 'Fernrando Rendon':
        photo = open('photo/Фернандо Рендон!.jpg', 'rb')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 Detallado...',
                                          url='https://es.wikipedia.org/wiki/Fernando_Rend%C3%B3n')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_vad = cur.execute('SELECT two FROM poetry WHERE id = 6').fetchone()
        bot.send_message(message.chat.id, poetry_vad)
        bot.send_message(message.chat.id, '📲 Aquí se puede Leer la biografía completa del poeta...',
                         reply_markup=board)

    elif message.text == 'Vadim Terekhin':
        photo = open('photo/Vadim.jpg', 'rb')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        board = types.InlineKeyboardMarkup(row_width=1)
        link = types.InlineKeyboardButton(text='🎯 Detallado...',
                                          url='https://ru.wikipedia.org/wiki/Терёхин,_Вадим_Фёдорович')
        board.add(link)
        btn1 = types.KeyboardButton(text='🔙 Menú principal')
        keyboard.add(btn1)
        bot.send_photo(message.chat.id, photo,
                       reply_markup=keyboard)
        connect = sqlite3.connect('films_db (2).sqlite')
        cur = connect.cursor()
        poetry_vad = cur.execute('SELECT two FROM poetry WHERE id = 3').fetchone()
        bot.send_message(message.chat.id, poetry_vad)
        bot.send_message(message.chat.id, '📲 Aquí se puede Leer la biografía completa del poeta...',
                         reply_markup=board)


bot.polling(none_stop=False, interval=0)
