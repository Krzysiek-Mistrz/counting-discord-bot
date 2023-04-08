import discord
from collections import defaultdict

intents = discord.Intents.default()
intents.members = True
intents.messages = True

PREFIX = '!'

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready and connected to Discord!')

@client.event
async def on_message(message):

    print("\nMessage received!\n")

    if message.author == client.user:
        return

    else:
        channel = client.get_channel() #count from channel
        message_counts = defaultdict(int)

        async for message in channel.history(limit=None):
            message_counts[message.author] += 1

        total_messages = sum(message_counts.values())
        sorted_message_counts = sorted(message_counts.items(), key=lambda x: x[1], reverse=True)
        user_message_counts = "\n".join(f"{user.name}: {count}" for user, count in sorted_message_counts)
        message_to_send = f"Total messages sent: {total_messages}\n\nMessages sent by each user:\n{user_message_counts}"
        
        channel = client.get_channel() #send to channel
        await channel.send(message_to_send)

client.run('') #server token