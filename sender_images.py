def send_image_with_tg_bot(bot, chat_id, file_path):
        with open(file_path, 'rb') as document:
            bot.send_document(chat_id, document)
