#!/usr/bin/env python3
"""
Example usage of the Gemini TTS program.
This script demonstrates various ways to use the text-to-speech functionality.
"""

from gemini_tts import GeminiTTS
import os


def example_single_speaker():
    """Example of single-speaker text-to-speech."""
    print("=== Single Speaker Example ===")
    
    # Initialize TTS (make sure you have GOOGLE_API_KEY set)
    tts = GeminiTTS()
    
    # Simple text-to-speech
    text = "Say cheerfully: Have a wonderful day!"
    output_file = tts.single_speaker_tts(
        text=text,
        voice_name='Puck',  # Upbeat voice
        output_file='cheerful_greeting.wav'
    )
    print(f"Generated: {output_file}\n")


def example_multi_speaker():
    """Example of multi-speaker text-to-speech."""
    print("=== Multi Speaker Example ===")
    
    tts = GeminiTTS()
    
    # Multi-speaker conversation
    conversation = """TTS the following conversation between Jane and Joe:
    Jane: How's it going today Joe?
    Joe: Not too bad, how about you?
    Jane: Pretty good! Just working on some exciting AI projects.
    Joe: That sounds fascinating! Tell me more."""
    
    speakers = {
        'Jane': 'Kore',   # Firm voice
        'Joe': 'Puck'   # Upbeat voice
    }
    
    output_file = tts.multi_speaker_tts(
        text=conversation,
        speakers=speakers,
        output_file='conversation.wav'
    )
    print(f"Generated: {output_file}\n")


def example_styled_speech():
    """Example of styled speech with prompts."""
    print("=== Styled Speech Example ===")
    
    tts = GeminiTTS()
    
    # Spooky whisper example
    spooky_text = """Say in a spooky whisper:
    "By the pricking of my thumbs...
    Something wicked this way comes\""""
    
    output_file = tts.single_speaker_tts(
        text=spooky_text,
        voice_name='Enceladus',  # Breathy voice works well for whispers
        output_file='spooky_whisper.wav'
    )
    print(f"Generated: {output_file}\n")


def example_generated_content():
    """Example of generating content first, then converting to speech."""
    print("=== Generated Content Example ===")
    
    tts = GeminiTTS()
    
    # Generate and speak about a topic (single speaker)
    output_file = tts.generate_and_speak(
        topic="the benefits of renewable energy",
        output_file='renewable_energy.wav'
    )
    print(f"Generated: {output_file}\n")
    
    # Generate and speak with multiple speakers
    speakers = {
        'Dr. Sarah': 'Charon',  # Informative voice
        'Mike': 'Puck'          # Upbeat voice
    }
    
    output_file = tts.generate_and_speak(
        topic="artificial intelligence and machine learning",
        speakers=speakers,
        output_file='ai_discussion.wav'
    )
    print(f"Generated: {output_file}\n")


def main():
    """Run all examples."""
    # Check if API key is set
    if not os.getenv('GOOGLE_API_KEY'):
        print("Please set your GOOGLE_API_KEY environment variable first:")
        print("export GOOGLE_API_KEY='your_api_key_here'")
        return
    
    try:
        print("Running Gemini TTS examples...\n")
        
        example_single_speaker()
        example_multi_speaker()
        example_styled_speech()
        example_generated_content()
        
        print("All examples completed successfully!")
        print("Check the generated .wav files in the current directory.")
        
    except Exception as e:
        print(f"Error running examples: {e}")


if __name__ == "__main__":
    main()
