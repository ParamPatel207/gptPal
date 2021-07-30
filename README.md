## Slack Bot Gpt3 integration
We are working on a bot that will allow you to interact with the Gpt3 API and use various features of the Gpt3 platform like summarization and classification.

## TO-DO
- [x] Setup slack bot configuration
- [x] Create slack bot integration 
- [x] Integrate slack bot with Gpt3
- [ ] Integrate feature to activate slack bot when bot is called using @gpt-Pal
- [ ] Write test cases for slack bot
- [ ] Deploy on Digital Ocean droplet

# Steps to setup slack bot
- ```sh pip install slackclient python-dotenv flask slackeventsapi openai newspaper3k urlextract ```
(for mac user use pip3 instead of pip)
- create .env file with SLACK_TOKEN, SIGINING_SECRET and OPEN_AI variables.
- use ```sh python3 gptPal.py``` in the terminal to run the bot
- run ```sh chmod +x ngrok``` to make the file executable
- run ```sh ngrok http 5000``` to start the ngrok server
- copy the ngrok url from the terminal as shown in the attached image![Screenshot](/images/ngrok.png)
- paste it in the slack bot configuration as shown in the attached image![Screenshot](/images/slack_event.png)
- your bot should be up and running!