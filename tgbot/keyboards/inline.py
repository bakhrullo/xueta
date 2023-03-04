from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#
# msg_conf_or_rej_btn = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton('Ortga 🔙', callback_data='back'),
#                                                             InlineKeyboardButton('Qo\'shish ✅', callback_data='add'))

msg_send_or_add_btn = InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton('Ortga 🔙', callback_data='back'),
                                                            InlineKeyboardButton('Yana qo\'shish ➕', callback_data='add'),
                                                            InlineKeyboardButton('Boshlash ✅', callback_data='start'))


