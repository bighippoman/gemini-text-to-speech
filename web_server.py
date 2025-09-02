#!/usr/bin/env python3
"""
Flask Web Server for Gemini TTS
Provides a web API for the text-to-speech functionality.
"""

import os
import base64
import tempfile
from typing import Dict
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from gemini_tts import GeminiTTS

app = Flask(__name__)
CORS(app)

# Store TTS clients per session (in a real app, use proper session management)
tts_clients: Dict[str, GeminiTTS] = {}


def get_or_create_tts_client(api_key: str) -> GeminiTTS:
    """Get or create a TTS client for the given API key."""
    # Use a hash of the API key as the client ID for basic security
    client_id = str(hash(api_key))
    
    if client_id not in tts_clients:
        try:
            tts_clients[client_id] = GeminiTTS(api_key=api_key)
        except Exception as e:
            raise Exception(f"Failed to initialize TTS client: {str(e)}")
    
    return tts_clients[client_id]


@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')


@app.route('/api/voices', methods=['GET'])
def get_voices():
    """Get list of available voices."""
    return jsonify({
        'success': True,
        'voices': GeminiTTS.VOICES
    })


@app.route('/api/tts/single', methods=['POST'])
def single_speaker_tts():
    """Convert text to speech with single speaker."""
    try:
        data = request.get_json()
        api_key = data.get('api_key', '').strip()
        text = data.get('text', '').strip()
        voice = data.get('voice', 'Kore')
        
        if not api_key:
            return jsonify({
                'success': False,
                'error': 'API key is required'
            }), 400
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'Text is required'
            }), 400
        
        # Get or create TTS client for this API key
        tts_client = get_or_create_tts_client(api_key)
        
        # Generate audio in a temporary file
        with tempfile.NamedTemporaryFile(suffix='.wav',
                                         delete=False) as tmp_file:
            output_path = tts_client.single_speaker_tts(
                text=text,
                voice_name=voice,
                output_file=tmp_file.name
            )
            
            # Read the audio file and encode as base64
            with open(output_path, 'rb') as audio_file:
                audio_data = audio_file.read()
                audio_b64 = base64.b64encode(audio_data).decode('utf-8')
            
            # Clean up temporary file
            os.unlink(output_path)
            
            return jsonify({
                'success': True,
                'audio_data': audio_b64,
                'message': f'Generated with voice: {voice}'
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/tts/multi', methods=['POST'])
def multi_speaker_tts():
    """Convert text to speech with multiple speakers."""
    try:
        data = request.get_json()
        api_key = data.get('api_key', '').strip()
        text = data.get('text', '').strip()
        speakers = data.get('speakers', {})
        
        if not api_key:
            return jsonify({
                'success': False,
                'error': 'API key is required'
            }), 400
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'Text is required'
            }), 400
        
        if not speakers or len(speakers) == 0:
            return jsonify({
                'success': False,
                'error': 'Speakers configuration is required'
            }), 400
        
        # Get or create TTS client for this API key
        tts_client = get_or_create_tts_client(api_key)
        
        # Generate audio in a temporary file
        with tempfile.NamedTemporaryFile(suffix='.wav',
                                         delete=False) as tmp_file:
            output_path = tts_client.multi_speaker_tts(
                text=text,
                speakers=speakers,
                output_file=tmp_file.name
            )            # Read the audio file and encode as base64
            with open(output_path, 'rb') as audio_file:
                audio_data = audio_file.read()
                audio_b64 = base64.b64encode(audio_data).decode('utf-8')
            
            # Clean up temporary file
            os.unlink(output_path)
            
            return jsonify({
                'success': True,
                'audio_data': audio_b64,
                'message': f'Generated with {len(speakers)} speakers'
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate', methods=['POST'])
def generate_and_speak():
    """Generate content about a topic and optionally convert to speech."""
    try:
        data = request.get_json()
        api_key = data.get('api_key', '').strip()
        topic = data.get('topic', '').strip()
        speakers = data.get('speakers')
        generate_only = data.get('generate_only', False)
        
        if not api_key:
            return jsonify({
                'success': False,
                'error': 'API key is required'
            }), 400
        
        if not topic:
            return jsonify({
                'success': False,
                'error': 'Topic is required'
            }), 400
        
        # Get or create TTS client for this API key
        tts_client = get_or_create_tts_client(api_key)
        
        if generate_only:
            # Just generate content, don't convert to speech
            generated_text = tts_client.generate_content(topic, speakers)
            return jsonify({
                'success': True,
                'message': 'Content generated successfully',
                'generated_text': generated_text
            })
        
        # Generate audio in a temporary file
        with tempfile.NamedTemporaryFile(suffix='.wav',
                                         delete=False) as tmp_file:
            output_path = tts_client.generate_and_speak(
                topic=topic,
                speakers=speakers,
                output_file=tmp_file.name
            )
            
            # Read the audio file and encode as base64
            with open(output_path, 'rb') as audio_file:
                audio_data = audio_file.read()
                audio_b64 = base64.b64encode(audio_data).decode('utf-8')
            
            # Clean up temporary file
            os.unlink(output_path)
            
            return jsonify({
                'success': True,
                'audio_data': audio_b64,
                'message': f'Generated content about: {topic}'
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'success': True,
        'message': 'Gemini TTS API is running',
        'api_key_set': bool(os.getenv('GOOGLE_API_KEY'))
    })


if __name__ == '__main__':
    print("Starting Gemini TTS Web Server...")
    print("Open http://localhost:8080 in your browser")
    print("Press Ctrl+C to stop the server")
    
    # Check if API key is set
    if not os.getenv('GOOGLE_API_KEY'):
        print("\nWARNING: GOOGLE_API_KEY environment variable not set!")
        print("The web interface will prompt you to set it.")
    
    app.run(debug=True, host='0.0.0.0', port=8080)
