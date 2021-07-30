import os
import slack
from ml import FinalOutput
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(
    os.environ['SIGINING_SECRET'], "/slack/events", app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
print(BOT_ID)
@slack_events_adapter.on('message')
def handle_message(event_data):
    event= event_data.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        val = FinalOutput(text)
        client.chat_postMessage(channel=channel_id, text=val)

if __name__ == '__main__':
    app.run(debug=True)
