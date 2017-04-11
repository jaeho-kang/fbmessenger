from flask import Flask, request
import requests
from engine.commonGate import commonGate
from messenger.bot import Bot
import logging
import json
import ssl


app = Flask(__name__)
cg = commonGate()


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"

@app.route('/hello',methods=['GET'])
def hello():
    return 'hello'

@app.route('/', methods=['POST'])
def webhook():
    payload = request.json
    print(payload)
    for sender, msg in bot.messaging_events(payload):
        print(sender)
        response = cg.reply(sender, msg)
        bot.send_text_message(sender, response)
    return "ok"


if __name__ == '__main__':
    
    config = json.load(open("./config/config.json","r"))

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(config["SSL"]["crt"],config["SSL"]["key"])
    logging.basicConfig(filename='./logs/chatbot.log', level=logging.WARNING)

    ACCESS_TOKEN = config["FB_TOKEN"]["ACCESS_TOKEN"]
    VERIFY_TOKEN = config["FB_TOKEN"]["VERIFY_TOKEN"]
    bot = Bot(ACCESS_TOKEN, api_verion=2.6)

    app.run(debug=True, 
            host='0.0.0.0', 
        ssl_context=context)

