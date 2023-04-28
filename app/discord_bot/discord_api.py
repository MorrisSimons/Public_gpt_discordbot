from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')


class myClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author == self.user:
            return
        command, user_message = None, None

        for text in ['/bot', '/gpt4', '/gpt3.5']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)

        if command == '/gpt3.5' or command == '/bot' or command == '/gpt4':
            # gpt3.5 and gpt4 are for later fittning
            if command == '/gpt4':
                model = 'gpt-4'
            else:
                model = 'text-davinci-003'
            print(f"[+]Loading answer from {model}")
            bot_response = chatgpt_response(prompt=user_message, model=model)
            await message.channel.send(f"Answer: {bot_response}")


intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents=intents)
