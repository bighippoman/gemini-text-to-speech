#!/bin/bash
# Gemini TTS Web Interface Launcher

echo "🎤 Gemini TTS Web Interface"
echo "=========================="

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run this from the project directory."
    exit 1
fi

# Check if API key is set
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  GOOGLE_API_KEY not set!"
    echo "🔑 Set your API key:"
    echo "   export GOOGLE_API_KEY='your_api_key_here'"
    echo "   📋 Get your key from: https://aistudio.google.com/"
    echo
    read -p "🚀 Continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Exiting..."
        exit 1
    fi
fi

echo "🚀 Starting web server..."
echo "📱 Open http://localhost:8080 in your browser"
echo "⏹️  Press Ctrl+C to stop"
echo

# Start the web server
.venv/bin/python web_server.py
