# Import necessary libraries
import os, io
from gtts import gTTS
from twitchio.ext import commands
from dotenv import load_dotenv
import pygame

# Load environment variables
load_dotenv()

# Initialize Pygame and Pygame.mixer
pygame.init()
pygame.mixer.init()

# Define function to convert message to audio content
def tts_message(message):
    # Set the language for the text-to-speech conversion
    lingua = 'it'
    # Create a gTTS object with the message and language
    tts = gTTS(text=message, lang=lingua)
    # Create an empty byte stream to write the audio content to
    audio_content = io.BytesIO()
    # Write the audio content to the byte stream
    tts.write_to_fp(audio_content)
    # Set the byte stream position to the beginning
    audio_content.seek(0)
    # Return the byte stream containing the audio content
    return audio_content

# Define a Bot class that extends the commands.Bot class from the twitchio library
class Bot(commands.Bot):

    def __init__(self):
        # Call the constructor of the parent class with the Twitch API token and prefix
        # Also specify the initial channels to join
        super().__init__(token=os.getenv('token'), prefix='?', initial_channels=[os.getenv('initial_channels'),])

    # Define an event handler for when the bot is ready to start processing events
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    # Define an event handler for when a message is received
    async def event_message(self, message):
        # Load the audio content for the message into the Pygame mixer
        pygame.mixer.music.load(tts_message(message.content))
        # Play the audio content
        pygame.mixer.music.play()
        # Print the message to the console
        print(f"{message.author.name}: {message.content}")

    # Define a command for the bot to respond to
    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a response to the channel
        await ctx.send(f'Hello {ctx.author.name}!')

# Create an instance of the Bot class
bot = Bot()
# Start the bot
bot.run()

# Quit Pygame.mixer and Pygame
pygame.mixer.quit()
pygame.quit()
