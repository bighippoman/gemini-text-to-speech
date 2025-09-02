#!/usr/bin/env python3
"""
Demo script showing how to use the Gemini TTS program.
This script shows the commands you would run 
(without actually calling the API).
"""


def show_demo():
    """Show demonstration of how to use the TTS program."""
    print("=== Gemini TTS Demo ===")
    print("Here's how to use the Gemini Text-to-Speech program:\n")
    
    print("1. SETUP:")
    print("   First, get your API key from https://aistudio.google.com/")
    print("   Then set it as an environment variable:")
    print("   export GOOGLE_API_KEY='your_api_key_here'\n")
    
    print("2. BASIC USAGE EXAMPLES:")
    print()
    
    print("   # Convert simple text to speech:")
    print("   python gemini_tts.py --text 'Hello, welcome to AI text-to-speech!' --voice Puck")
    print()
    
    print("   # Create a conversation between two speakers:")
    print("   python gemini_tts.py \\")
    print("     --text 'Jane: Hi there! Joe: Hello Jane, how are you doing today?' \\")
    print("     --multi-speaker \\")
    print("     --speakers 'Jane:Kore' 'Joe:Puck' \\")
    print("     --output conversation.wav")
    print()
    
    print("   # Generate content about a topic and convert to speech:")
    print("   python gemini_tts.py --generate 'the future of artificial intelligence'")
    print()
    
    print("   # Generate a conversation between experts:")
    print("   python gemini_tts.py \\")
    print("     --generate 'quantum computing' \\")
    print("     --multi-speaker \\")
    print("     --speakers 'Dr.Smith:Charon' 'Prof.Lee:Leda'")
    print()
    
    print("3. INTERACTIVE MODE:")
    print("   python interactive_tts.py")
    print("   Then use commands like:")
    print("   > speak Hello world!")
    print("   > multi Jane:Kore Joe:Puck Jane: Hi! Joe: Hello!")
    print("   > generate space exploration")
    print("   > voices")
    print("   > quit")
    print()
    
    print("4. AVAILABLE VOICES:")
    print("   Run 'python gemini_tts.py --list-voices' to see all 30 voices")
    print("   Popular choices:")
    print("   - Puck (Upbeat)")
    print("   - Kore (Firm)")
    print("   - Charon (Informative)")
    print("   - Enceladus (Breathy - good for whispers)")
    print("   - Leda (Youthful)")
    print()
    
    print("5. STYLE CONTROL:")
    print("   You can control the speech style with natural language:")
    print("   python gemini_tts.py --text 'Say cheerfully: Have a great day!'")
    print("   python gemini_tts.py --text 'Whisper mysteriously: The secret is...'")
    print()
    
    print("6. PROGRAMMATIC USAGE:")
    print("   from gemini_tts import GeminiTTS")
    print("   tts = GeminiTTS()")
    print("   tts.single_speaker_tts('Hello!', 'Puck', 'output.wav')")
    print()
    
    print("For more examples, check out examples.py")
    print("For testing your setup, run: python test_setup.py")


if __name__ == "__main__":
    show_demo()
