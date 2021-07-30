import os
import slack
from ml import MLHandler
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

# handling environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#starting flask and slack events handler
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(
    os.environ['SIGINING_SECRET'], "/slack/events", app)

#slack token handler and bot id retrieval to avoid duplication
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

#basic function which reads for messages and then calls the ml function
@slack_events_adapter.on('message')
def handle_message(event_data):
    event= event_data.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        val = MLHandler(text)
        client.chat_postMessage(channel=channel_id, text=val)

if __name__ == '__main__':
    app.run(debug=True)
