# Twitch Chat Text-To-Speech Bot

This is a simple Twitch chat bot that uses Google Text-to-Speech (TTS) to convert messages in chat to audio and plays them through the bot's audio output.
Audio is routed through the default audio output.

## Features

- Connects to the Twitch IRC server using the `twitchio` library.
- Uses the Google TTS API to convert messages in chat to audio content.
- Plays the audio content through the bot's audio output using the `pygame` library.
- Responds to the `?hello` command with a greeting in chat.

## Installation

To install the dependencies for this project, run the following command:

```sh
pip install -r requirements.txt
```

Edit a `.env` file in the project directory with the following variables:
```
token=your_twitch_api_token
initial_channels=your_twitch_username
```

# Usage

Once the bot is running, join your Twitch channel and start typing messages in the chat. The bot will convert your messages to speech and play the resulting audio.

You can also use the `?hello` command to test the bot's responsiveness.

## Special Thanks

This project was inspired by the Twitch channel of [Prof. Andrea Pollini](https://www.twitch.tv/profandreapollini) and the supportive Twitch community. Thanks to their encouragement and feedback, this bot was created to enhance the Twitch chat experience. Special thanks also go to the developers of Pygame and gTTS for their excellent libraries. 



## License

This project is licensed under the MIT License - see the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) for details.