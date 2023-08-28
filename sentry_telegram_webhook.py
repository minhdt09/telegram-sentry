from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

TELEGRAM_BOT_TOKEN = "6507544190:AAGH-4YRNFFu7L-SO5YVFUbTodmxtrVbFww"
TELEGRAM_CHAT_ID = 5796341739

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Your existing processing logic here
        # ...

        message = "Your message to Telegram"
        send_telegram_message(message)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"OK")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
    }
    response = requests.post(url, params=params)
    return response.json()

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WebhookHandler)
    httpd.serve_forever()
