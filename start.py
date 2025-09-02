#!/usr/bin/env python3
"""
One-Click Gemini TTS Web Interface Launcher
The easiest way to start using Gemini TTS with a web interface.
"""

import os
import sys
import webbrowser
import subprocess
import time
from threading import Timer


def main():
    """Launch the web interface with one command."""
    print("🎤 Gemini TTS - One-Click Web Interface")
    print("=" * 45)
    print()
    
    # Check if we're in the right directory
    if not os.path.exists('gemini_tts.py'):
        print("❌ Please run this from the Gemini TTS project directory")
        sys.exit(1)
    
    print("🚀 Starting web interface...")
    print("📱 Your browser will open automatically")
    print("🌐 Manual URL: http://localhost:8080")
    print()
    print("📋 You'll need your Google AI API key from:")
    print("   https://aistudio.google.com/")
    print()
    print("⏹️  Press Ctrl+C in terminal to stop the server")
    print("=" * 45)
    
    # Open browser after 3 seconds
    def open_browser():
        time.sleep(2)
        webbrowser.open('http://localhost:8080')
        print("🎉 Web interface opened in your browser!")
    
    Timer(1.0, open_browser).start()
    
    # Start the web server
    try:
        subprocess.run([
            '.venv/bin/python',
            'web_server.py'
        ], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to start web server")
    except KeyboardInterrupt:
        print("\n👋 Web server stopped. Goodbye!")


if __name__ == "__main__":
    main()
