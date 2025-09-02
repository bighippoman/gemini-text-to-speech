# 🌐 Gemini TTS Web Interface

## Quick Start (3 Steps!)

### 1. Set Your API Key
```bash
export GOOGLE_API_KEY='your_api_key_here'
```
Get your key from [Google AI Studio](https://aistudio.google.com/)

### 2. Start the Web Server
```bash
# Option A: Use the launcher script
python launch_web.py

# Option B: Use the shell script  
./start_web.sh

# Option C: Start manually
python web_server.py
```

### 3. Open Your Browser
Go to: **http://localhost:8080**

## 🎯 Web Interface Features

### **Single Speaker Tab**
- ✅ Convert any text to speech
- 🎤 Choose from 30 different AI voices
- 🎨 Use style prompts like "Say cheerfully:" or "Whisper mysteriously:"
- ▶️ Instant audio playback in browser

### **Multi Speaker Tab** 
- 👥 Create conversations between 2 speakers
- 🎭 Assign different voices to each speaker
- 💬 Perfect for dialogues, interviews, podcasts

### **Generate Content Tab**
- ✨ AI generates content about any topic
- 🤖 Converts generated text to speech automatically  
- 👥 Option for single or multi-speaker output
- 📚 Great for educational content, explanations

## 🎤 Voice Characteristics

**Popular Voices:**
- **Puck** - Upbeat and energetic
- **Kore** - Firm and authoritative
- **Charon** - Informative and professional  
- **Enceladus** - Breathy (perfect for whispers)
- **Leda** - Youthful and friendly
- **Charon** - Clear and informative

**Style Examples:**
- "Say cheerfully: Welcome to our podcast!"
- "Whisper mysteriously: The secret will be revealed..."
- "Announce dramatically: Ladies and gentlemen..."
- "Explain calmly: Here's how this works..."

## 🚀 Usage Examples

### Single Speaker:
```
Text: "Say enthusiastically: Welcome to the future of AI!"
Voice: Puck (Upbeat)
```

### Multi Speaker Conversation:
```
Text: "Alice: Did you hear about the new AI breakthrough? 
       Bob: No, tell me more! 
       Alice: It's absolutely revolutionary!"
       
Speaker 1: Alice → Leda (Youthful)
Speaker 2: Bob → Puck (Upbeat)
```

### Generate Content:
```
Topic: "the mysteries of black holes"
Mode: Multi-speaker
Speaker 1: Dr. Sarah → Charon (Informative)  
Speaker 2: Alex → Fenrir (Excitable)
```

## 💡 Pro Tips

1. **Voice Selection**: Match voice personality to content style
2. **Multi-Speaker**: Use clear speaker names that match your text
3. **Style Control**: Include tone instructions in your text
4. **Generated Content**: Try specific topics for better results
5. **Audio Quality**: All audio is generated at 24kHz for crisp quality

## 🔧 Troubleshooting

**Can't connect to server?**
- Make sure the web server is running
- Check if port 8080 is available
- Try refreshing the browser

**API errors?**
- Verify your Google AI API key is correct
- Check your internet connection
- Make sure you have API quota remaining

**Audio not playing?**
- Check browser audio permissions
- Try a different browser (Chrome/Safari work best)
- Ensure speakers/headphones are connected

---

**🎉 That's it! You now have a beautiful web interface for Gemini TTS!**
