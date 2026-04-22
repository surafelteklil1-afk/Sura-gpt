from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import os

# books text load
with open("books.txt", "r", encoding="utf-8") as f:
    BOOK = f.read().lower()

def search_answer(question):
    q = question.lower()

    if q in BOOK:
        return "📚 ከመፅሀፍ:\n" + q
    else:
        return "❌ ይህ ጥያቄ ከመፅሀፍ ውጪ ነው"

async def handle(update: Update, context):
    text = update.message.text
    answer = search_answer(text)
    await update.message.reply_text(answer)

app = ApplicationBuilder().token(os.getenv("8788917132:AAG4G76ZUT_gs55p34zA9ppaZby2-5r6fNg")).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
