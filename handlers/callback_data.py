from create_bot import dp, bot
from data_base.config import ADMINS
from data_base.sqlite_db import sql_read2, sql_delete_command, delete_cmd


@dp.callback_query_handler()
async def adr_c(call):
    if call.data == call.data:
        delete_cmd.append(call.data)
        await sql_read2(call, call.data)
    if call.data == 'delete_btn':
        if call.from_user.id == ADMINS:
            await sql_delete_command(delete_cmd)
            await bot.answer_callback_query(call.id, text='Удалена', show_alert=True)