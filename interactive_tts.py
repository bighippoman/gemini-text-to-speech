#!/usr/bin/env python3
"""
Interactive Gemini TTS Program
A simple interactive interface for text-to-speech conversion.
"""

import os
from gemini_tts import GeminiTTS


def main():
    """Run the interactive TTS interface."""
    print("=== Gemini Text-to-Speech Interactive Mode ===")
    print("Type 'help' for available commands, 'quit' to exit")
    
    # Check API key
    if not os.getenv('GOOGLE_API_KEY'):
        api_key = input("Enter your Google AI API key: ").strip()
        if not api_key:
            print("API key is required. Exiting.")
            return
        os.environ['GOOGLE_API_KEY'] = api_key
    
    try:
        tts = GeminiTTS()
        print("TTS client initialized successfully!\n")
    except Exception as e:
        print(f"Failed to initialize TTS client: {e}")
        return
    
    while True:
        try:
            command = input("\n> ").strip()
            
            if command.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            elif command.lower() == 'help':
                print_help()
            elif command.lower() == 'voices':
                print_voices()
            elif command.startswith('speak '):
                text = command[6:]
                simple_speak(tts, text)
            elif command.startswith('generate '):
                topic = command[9:]
                generate_content(tts, topic)
            else:
                print("Unknown command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def print_help():
    """Show available commands."""
    print("""
Available commands:
  speak <text>         - Convert text to speech
  generate <topic>     - Generate content and convert to speech
  voices               - List all available voices
  help                 - Show this help
  quit/exit/q          - Exit

Examples:
  speak Hello, this is a test!
  generate space exploration
""")


def print_voices():
    """Show all available voices."""
    print("\nAvailable voices:")
    for i, voice in enumerate(GeminiTTS.VOICES, 1):
        print(f"{i:2d}. {voice}")


def simple_speak(tts: GeminiTTS, text: str):
    """Convert text to speech."""
    if not text:
        print("Please provide text to convert.")
        return
    
    voice = input("Voice (default Kore): ").strip() or 'Kore'
    filename = input("Output file (default speech.wav): ").strip()
    output_file = filename or 'speech.wav'
    
    try:
        result = tts.single_speaker_tts(text, voice, output_file)
        print(f"✓ Generated: {result}")
    except Exception as e:
        print(f"✗ Error: {e}")


def generate_content(tts: GeminiTTS, topic: str):
    """Generate content and convert to speech."""
    if not topic:
        print("Please provide a topic.")
        return
    
    filename = input("Output file (default generated.wav): ").strip()
    output_file = filename or 'generated.wav'
    
    try:
        result = tts.generate_and_speak(topic, None, output_file)
        print(f"✓ Generated: {result}")
    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
