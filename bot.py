import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# هنا سيقرأ البوت التوكن من إعدادات موقع Render تلقائياً
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="العلوم الإنسانية", callback_data="humanities"))
    builder.row(types.InlineKeyboardButton(text="كلية الإدارة", callback_data="management"))
    await message.answer("أهلاً بك في manarmebot! اختر القسم:", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "humanities")
async def show_humanities(callback: types.CallbackQuery):
    await callback.message.answer("لقد اخترت العلوم الإنسانية.")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())