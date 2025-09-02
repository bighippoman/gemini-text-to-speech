# Gemini Text-to-Speech Web Interface

A user-friendly web interface for converting text to speech using Google's Gemini AI models.

## Features

- **Web Interface**: Web UI accessible from any browser
- **Multiple TTS Models**: Supports Gemini 2.5 Flash and Pro TTS models
- **30+ Voices**: Wide variety of voice options including Puck, Kore, Charon, and more
- **Multi-Speaker Support**: Create conversations with different voices
- **Content Generation**: Use Gemini to generate creative content then convert to speech
- **API Key Integration**: Secure client-side API key management
- **Command-line Interface**: Also includes CLI options for advanced users

## Quick Start

### 1. Get your API key
Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 2. Run the application

**Recommended (easiest):**
```bash
python start.py
```

**Alternative options:**
```bash
# Shell script (if you prefer bash)
./start_web.sh

# Direct server start (advanced users)
python web_server.py
```

This will automatically open your browser to `http://localhost:8080`

### 3. Use the web interface
- Paste your API key in the web interface
- Select a voice and enter your text
- Click generate to create and play audio!

## Available Voices

The program supports 30 different voices:

- **Bright**: Zephyr, Autonoe
- **Upbeat**: Puck, Laomedeia  
- **Firm**: Kore, Orus, Alnilam
- **Informative**: Charon, Rasalgethi
- **Excitable**: Fenrir
- **Youthful**: Leda
- **Breezy**: Aoede
- **Easy-going**: Callirrhoe, Umbriel
- **Breathy**: Enceladus
- **Clear**: Iapetus, Erinome
- **Smooth**: Algieba, Despina
- **Gravelly**: Algenib
- **Soft**: Achernar
- **Even**: Schedar
- **Mature**: Gacrux
- **Forward**: Pulcherrima
- **Friendly**: Achird
- **Casual**: Zubenelgenubi
- **Gentle**: Vindemiatrix
- **Lively**: Sadachbia
- **Knowledgeable**: Sadaltager
- **Warm**: Sulafat

## Usage

### Command Line Interface

#### Basic single-speaker TTS:
```bash
python gemini_tts.py --text "Hello, this is a test" --voice Puck --output hello.wav
```

#### Multi-speaker conversation:
```bash
python gemini_tts.py --text "Jane: Hello Joe! Joe: Hi Jane, how are you?" --multi-speaker --speakers "Jane:Kore" "Joe:Puck" --output conversation.wav
```

#### Generate content and convert to speech:
```bash
python gemini_tts.py --generate "artificial intelligence" --output ai_explanation.wav
```

#### Generate multi-speaker content:
```bash
python gemini_tts.py --generate "climate change" --multi-speaker --speakers "Dr.Smith:Charon" "Sarah:Leda" --output climate_discussion.wav
```

#### List all available voices:
```bash
python gemini_tts.py --list-voices
```

### Interactive Mode

Run the interactive interface:
```bash
python interactive_tts.py
```

Available commands in interactive mode:
- `speak <text>` - Convert text to speech
- `multi <speaker1:voice1> <speaker2:voice2> <text>` - Multi-speaker TTS
- `generate <topic>` - Generate and convert content about a topic
- `voices` - List all available voices
- `help` - Show help
- `quit` - Exit

### Python API

```python
from gemini_tts import GeminiTTS

# Initialize (will use GOOGLE_API_KEY env var)
tts = GeminiTTS()

# Single speaker
tts.single_speaker_tts(
    text="Hello world!",
    voice_name='Puck',
    output_file='hello.wav'
)

# Multi-speaker
speakers = {'Alice': 'Puck', 'Bob': 'Kore'}
tts.multi_speaker_tts(
    text="Alice: Hi Bob! Bob: Hello Alice!",
    speakers=speakers,
    output_file='conversation.wav'
)

# Generate content and speak
tts.generate_and_speak(
    topic="space exploration",
    output_file='space_talk.wav'
)
```

## Examples

See `examples.py` for detailed usage examples including:
- Basic single-speaker TTS
- Multi-speaker conversations
- Styled speech with prompts
- Content generation and TTS

## Supported Languages

The TTS models automatically detect input language and support 24 languages including:
- English (US, India)
- Spanish, French, German, Italian
- Japanese, Korean, Chinese
- Arabic, Hindi, Portuguese
- And many more

## Supported Models

- `gemini-2.5-flash-preview-tts` (default)
- `gemini-2.5-pro-preview-tts`

## Error Handling

The program includes comprehensive error handling for:
- Missing API keys
- Invalid voice names
- API response errors
- File I/O errors
- Network issues

## Tips for Best Results

1. **Voice Selection**: Choose voices that match the intended style (e.g., 'Enceladus' for breathy/whisper effects)
2. **Multi-speaker**: Clearly specify speaker names in your text that match the speaker configuration
3. **Style Control**: Use descriptive prompts like "Say cheerfully:" or "Whisper mysteriously:"
4. **Content Length**: Keep generated content around 100 words for optimal results

## Limitations

- Maximum 2 speakers for multi-speaker mode
- Text-only inputs (no audio or other modalities)
- Audio-only outputs
- Preview API (subject to changes)

## Troubleshooting

**"API key not found"**: Make sure to set the GOOGLE_API_KEY environment variable or pass it as a parameter.

**"Voice not supported"**: Use `--list-voices` to see all available voice options.

**"No audio data in response"**: Check your internet connection and API key validity.

**"Maximum 2 speakers supported"**: Multi-speaker mode only supports up to 2 speakers.
