import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import executor
import pprint
import requests
from bs4 import BeautifulSoup
from settings.config import *

logging.basicConfig(level=logging.INFO)
from settings.HdRezkaApi import *

bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MovieState(StatesGroup):
    movie = State()


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Привіт! Введи /movie, щоб ввести назву фільму.")


@dp.message_handler(Command("movie"))
async def cmd_movie(message: types.Message):#, state: FSMContext):
    #await state.finish()

    #await dp.storage.reset_state(chat=message.chat.id)
    await message.reply("Введи назву фільму:")
    await MovieState.movie.set()


@dp.message_handler(state=MovieState.movie)
async def process_movie(message: types.Message, state: FSMContext):
    movie_name = message.text

    await state.update_data(movie_name=movie_name)
    datadict = {}
    search_text = message.text
    url = 'https://rezka.ag/search/'

    search_response = requests.get(url, headers=headers, params={'do': 'search',
                                                                 'subaction': 'search',
                                                                 'q': search_text}).content
    search_data = BeautifulSoup(search_response, 'html.parser')
    results = search_data.select('div.b-content__inline_item')

    for i in range(len(results)):
        movie_img_tag = results[i].find('img')
        name_movie = movie_img_tag['alt']

        a_tags = results[i].find('a')
        href = a_tags.get('href')
        rezka = HdRezkaApi(href)
        try:
            movie_href = rezka.getStream()('480p')
        except TypeError:
            continue
        except UnicodeDecodeError:
            continue
        datadict[name_movie] = movie_href

    await state.update_data(datadict=datadict)

    #pprint.pprint(datadict)
    await show_menu(message, state)


@dp.callback_query_handler(lambda c: c.data == 'next', state=MovieState.movie)
async def next_page(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await show_menu(callback_query.message, state, next_page=True)


@dp.callback_query_handler(lambda c: c.data == 'previous', state=MovieState.movie)
async def previous_page(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await show_menu(callback_query.message, state, previous_page=True)


async def show_menu(message: types.Message, state: FSMContext, next_page=False, previous_page=False):
    data = await state.get_data()
    datadict = data.get('datadict', {})

    #print(data)
    current_page = data.get('current_page', 1)
    #print(current_page)

    start_index = (current_page - 1) * 5
    if start_index == 0:
        start_index = 1
    #print('SI', start_index)
    end_index = start_index + 5
    #print('EI', end_index)

    num_pages = (len(datadict) + 4) // 5
    #print(num_pages)

    if next_page:
        current_page += 1
        if current_page > num_pages:
            current_page = num_pages
    elif previous_page:
        current_page -= 1
        if current_page < 1:
            current_page = 1

    await state.update_data(current_page=current_page)

    menu_text = "Результати пошуку:\n"
    for i, (movie_name, movie_link) in enumerate(list(datadict.items())[start_index:end_index], start=1):
        menu_text += f"[{movie_name}]({movie_link})\n"

    keyboard = types.InlineKeyboardMarkup()

    if current_page > 1:
        keyboard.add(types.InlineKeyboardButton("Попередня сторінка", callback_data="previous"))

    if current_page < num_pages:
        keyboard.add(types.InlineKeyboardButton("Наступна сторінка", callback_data="next"))

    await bot.send_message(
        chat_id=message.chat.id,
        text=menu_text,
        reply_markup=keyboard,
        parse_mode=types.ParseMode.MARKDOWN
    )



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
