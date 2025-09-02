#!/usr/bin/env python3
"""
Quick test script for Gemini TTS setup.
Run this to verify your installation and API key are working.
"""

import os
import sys
from gemini_tts import GeminiTTS


def test_installation():
    """Test if the installation is working properly."""
    print("=== Gemini TTS Installation Test ===\n")
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check if google-genai is installed
    try:
        import google.genai  # noqa: F401
        print("✓ google-genai package is installed")
    except ImportError:
        print("✗ google-genai package not found")
        print("Please install with: pip install google-genai")
        return False
    
    # Check API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("✗ GOOGLE_API_KEY environment variable not set")
        api_key = input("Enter your API key to test: ").strip()
        if not api_key:
            print("API key is required for testing.")
            return False
    else:
        print("✓ GOOGLE_API_KEY environment variable is set")
    
    # Test TTS initialization
    try:
        tts = GeminiTTS(api_key=api_key)
        print("✓ GeminiTTS client initialized successfully")
    except Exception as e:
        print(f"✗ Failed to initialize GeminiTTS: {e}")
        return False
    
    # Test basic functionality (optional)
    test_basic = input("\nRun basic TTS test? (y/n, default: n): ")
    test_basic = test_basic.strip().lower()
    if test_basic in ['y', 'yes']:
        try:
            print("Generating test audio...")
            result = tts.single_speaker_tts(
                text="This is a test of the Gemini text-to-speech system.",
                voice_name='Kore',
                output_file='test_output.wav'
            )
            print(f"✓ Test audio generated successfully: {result}")
        except Exception as e:
            print(f"✗ Test failed: {e}")
            return False
    
    print("\n✓ All tests passed! Your Gemini TTS setup is ready to use.")
    return True


if __name__ == "__main__":
    test_installation()
