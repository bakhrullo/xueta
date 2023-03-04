import asyncio
from datetime import datetime

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy import select

from tgbot import config
from tgbot.config import load_config
from tgbot.keyboards.inline import msg_send_or_add_btn
from tgbot.misc.states import AdminState
from tgbot.models.model import Task, Msg


async def admin_start(m: Message):
    await m.reply("Salom admin! 👋\n"
                  "Kanalga yuborish kerak bo\'lgan xabarlarni yuboring.")
    await AdminState.get_msg.set()


async def get_msg(m: Message, state: FSMContext):
    try:
        data = await state.get_data()
        msg_ids = data['msg_id']
        msg_ids.append(m.message_id)
        await state.update_data(msg_id=msg_ids)
    except:
        await state.update_data(msg_id=[m.message_id])
    await m.bot.copy_message(from_chat_id=m.from_user.id, chat_id=m.from_user.id, message_id=m.message_id,
                             reply_markup=msg_send_or_add_btn)
    await AdminState.conf_msg.set()


async def add_msg(c: CallbackQuery):
    await c.message.delete()
    await c.message.answer("Kanalga yuborish kerak bo\'lgan xabarlarni yuboring.")
    await AdminState.get_msg.set()


async def start(c: CallbackQuery, state: FSMContext, scheduler: AsyncIOScheduler):
    data = await state.get_data()
    msg_ids = data["msg_id"]
    db_session = c.bot.get("db")
    async with db_session() as session:
        ses = await session.merge(
            Task(admin_id=c.from_user.id))
        await session.commit()
        count = 1
        for i in msg_ids:
            await session.merge(
                Msg(task=ses.id, msg_id=str(i), queue=count)
            )
            ses.posts += 1
            count += 1
        await session.commit()
    await state.reset_data()
    scheduler.add_job(channel_send, 'interval', seconds=10, start_date=datetime.now(), args=(c, ses.id, scheduler), id='msg_send')
    await c.message.delete()
    await c.message.answer("⏳")
    await c.message.answer("Avto e\'lon boshlandi! 😄 \nTugashi bilan sizga xabar beramiz.\nYangi e\'lon berish uchun /start ni bosing")


async def channel_send(c: CallbackQuery, rec_id, scheduler):
    db_session = c.bot.get("db")
    channel_id = load_config(".env")
    async with db_session() as session:
        data = await session.execute(select(Task).where(Task.id == rec_id))
        datas = data.scalars()
        for i in datas:
            i.queue += 1
            if i.queue == i.posts:
                scheduler.remove_job('msg_send')
                await c.message.answer("✅")
                await c.message.answer("Avto e'lon yakuniga yetdi ✅\nYangi e\'lon berish uchun /start ni bosing! 😄")
            await session.commit()
            msg = await session.execute(select(Msg).where(Msg.task == i.id, Msg.queue == i.queue))
            msgs = msg.scalars()
            for d in msgs:
                await c.bot.copy_message(from_chat_id=i.admin_id, chat_id=channel_id.tg_bot.channel_id, message_id=d.msg_id)
                for h in channel_id.tg_bot.channel_id:
                    await c.bot.copy_message(from_chat_id=i.admin_id, chat_id=h, message_id=d.msg_id)
                    await asyncio.sleep(1)


async def back(c: CallbackQuery, state: FSMContext):
    await c.message.delete()
    await state.reset_data()
    await c.message.answer("Salom admin! 👋\n"
                           "Kanalga yuborish kerak bo\'lgan xabarlarni yuboring.")
    await AdminState.get_msg.set()


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(get_msg, content_types=types.ContentType.ANY, state=AdminState.get_msg, is_admin=True)
    dp.register_callback_query_handler(add_msg, Text(equals="add"), state=AdminState.conf_msg, is_admin=True)
    dp.register_callback_query_handler(start, Text(equals="start"), state=AdminState.conf_msg, is_admin=True)
    dp.register_callback_query_handler(back, Text(equals="back"), state="*", is_admin=True)
