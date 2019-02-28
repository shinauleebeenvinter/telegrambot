from flask import Flask, request
from telepot import Bot
import telepot


TOKEN = "667940096:AAHPD6lVQ1yTxRsZi48HXPilfAhVkO3sYhY"
app = Flask(__name__)
bot = Bot(TOKEN)


@app.route("/webhook", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.headers["Content-Type"] == "application/json":
            messages = request.get_json()
            if "message" in messages:
                OnMessage(messages["message"])
        return "OK"
    else:
        return "webhook"


def OnMessage(message):
    content_type, chat_type, chat_id = telepot.glance(
        message)
    if chat_type == "private":
        if content_type == "text":
            bot.sendMessage(chat_id=chat_id, text=message["text"])


if __name__ == "__main__":
    bot.setWebhook(url="https://8f0eb3c2.ap.ngrok.io/webhook")
    print(bot.getMe())
    app.run()
