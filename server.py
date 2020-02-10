from flask import Flask, Response, request
import requests
from methods import is_prime, is_palindrome, sqrt, popular
from wrapped_methods import wrap_is_prime, wrap_sqrt, wrap_is_palindrome, wrap_is_fact
import database
from collections import defaultdict

app = Flask(__name__)
TOKEN = '1088073499:AAEdGd0iJnt4ftRgz-2eImd3WTaXEqYLGVo'
dictionary_commands = {"/check": wrap_is_prime, "/palindrome": wrap_is_palindrome, "/sqrt": wrap_sqrt,
                       "/fact": wrap_is_fact, "/popular": popular}
command_count = defaultdict(int)


@app.route('/sanity')
def sanity(): return "Server is running"


def start():
    TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://54c374fb.ngrok.io/message'.format(
        TOKEN)
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)


def parse_text(text: str):
    data = text.split()
    return data


def add_command(command_name):
    command_count[command_name] += 1


def get_command(first_word):
    return dictionary_commands.get(first_word, None)
    # return dictionary_commands.keys()


@app.route('/message', methods=["POST"])
def handle_message():
    print(request.get_json())
    chat_id = request.get_json()['message']['chat']['id']
    text = request.get_json()['message']['text']
    first_word = text.split(' ', 1)[0]
    print(request.get_json()["message"]["chat"])
    command = get_command(first_word)
    if not command:
        result = f"Command {first_word} not found"
    else:
        parsed_text = parse_text(text)
        result = command(parsed_text)
        add_command(first_word)
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                       .format(TOKEN, chat_id, result))
    database.save_popular(command_count)
    return Response("success", status=200)


if __name__ == '__main__':
    start()
    app.run(port=5002)
