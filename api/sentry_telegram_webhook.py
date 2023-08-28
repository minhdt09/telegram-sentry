from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = "6507544190:AAGH-4YRNFFu7L-SO5YVFUbTodmxtrVbFww"
TELEGRAM_CHAT_ID = 5796341739

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    app.logger.info(data)

    # Extract issue details
    issue_title = data.get('message', 'No Title Test')
    project_name = data.get('project_name', 'Unknown Project')
    culprit = data.get('culprit', 'No Culprit')
    event_id = data.get('id', 'No Event ID')
    level = data.get('level', 'No Level')
    url = data.get('url', 'No URL')

    # Create a detailed message
    message = f"New Sentry Issue in {project_name}: {issue_title}\n"
    message += f"Event ID: {event_id}\n"
    message += f"Culprit: {culprit}\n"
    message += f"Level: {level}\n"
    message += f"URL: {url}"

    # Send detailed message to Telegram
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

@app.route('/', methods=['GET'])
def home():
    return "Hello Minh"