from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('AZvfO6pLukri47LoR5m5zul0wdMZed+m2vYj93sQfcdP93f9RzhrjjNApUKehD+cD/NhIoWH0F8oX6gIws1FrhVpMMNEThDWfp2J9nEksfEW7odLKTGEJsOW3m86kxXwHJF4guVZGqTVWcJtgTtKfQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5fa8f758e580bb8c1503e58f68c0d917')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎'))


if __name__ == "__main__":
    app.run()