from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = "6507544190:AAGH-4YRNFFu7L-SO5YVFUbTodmxtrVbFww"
TELEGRAM_CHAT_ID = 5796341739

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    issue_title = data.get('title', 'No Title')
    project_name = data.get('project', 'Unknown Project')
    message = f"New Sentry Issue in {project_name}: {issue_title}"

    send_telegram_message(message)

    return jsonify({'status': 'ok'})

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
    }
    response = requests.post(url, params=params)
    return response.json()

