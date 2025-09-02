#!/usr/bin/env python3
"""
Gemini Text-to-Speech (TTS) Program
Uses Google's Gemini API to convert text to speech with
single or multi-speaker support.
"""

import os
import wave
import argparse
from typing import Optional, Dict
from google import genai
from google.genai import types


class GeminiTTS:
    """A class to handle Gemini API text-to-speech conversion."""
    
    # Available voice options
    VOICES = [
        'Zephyr', 'Puck', 'Charon', 'Kore', 'Fenrir', 'Leda', 'Orus', 'Aoede',
        'Callirrhoe', 'Autonoe', 'Enceladus', 'Iapetus', 'Umbriel', 'Algieba',
        'Despina', 'Erinome', 'Algenib', 'Rasalgethi', 'Laomedeia', 'Achernar',
        'Alnilam', 'Schedar', 'Gacrux', 'Pulcherrima', 'Achird',
        'Zubenelgenubi', 'Vindemiatrix', 'Sadachbia', 'Sadaltager', 'Sulafat'
    ]
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the GeminiTTS client.
        
        Args:
            api_key: Google AI API key. If not provided, will look for
                    GOOGLE_API_KEY env var.
        """
        if api_key:
            os.environ['GOOGLE_API_KEY'] = api_key
        elif not os.getenv('GOOGLE_API_KEY'):
            raise ValueError(
                "API key must be provided either as parameter or "
                "GOOGLE_API_KEY environment variable"
            )
        
        self.client = genai.Client()
    
    def save_wave_file(self, filename: str, pcm_data: bytes,
                       channels: int = 1, rate: int = 24000,
                       sample_width: int = 2) -> None:
        """
        Save PCM audio data as a WAV file.
        
        Args:
            filename: Output filename
            pcm_data: PCM audio data
            channels: Number of audio channels
            rate: Sample rate
            sample_width: Sample width in bytes
        """
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm_data)
        print(f"Audio saved to: {filename}")
    
    def single_speaker_tts(self, text: str, voice_name: str = 'Kore',
                           output_file: str = 'output_single.wav',
                           model: str = 'gemini-2.5-flash-preview-tts') -> str:
        """
        Convert text to speech with a single speaker.
        
        Args:
            text: Text to convert to speech
            voice_name: Voice to use (must be from VOICES list)
            output_file: Output filename
            model: Gemini model to use
            
        Returns:
            Path to the generated audio file
        """
        if voice_name not in self.VOICES:
            raise ValueError(
                f"Voice '{voice_name}' not supported. "
                f"Choose from: {', '.join(self.VOICES)}"
            )
        
        print(f"Generating single-speaker audio with voice '{voice_name}'...")
        
        response = self.client.models.generate_content(
            model=model,
            contents=text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voice_name,
                        )
                    )
                ),
            )
        )
        
        # Extract audio data with proper error handling
        if (not response.candidates or
                not response.candidates[0].content or
                not response.candidates[0].content.parts or
                not response.candidates[0].content.parts[0].inline_data):
            raise RuntimeError(
                "Failed to generate audio: No audio data in response"
            )
        
        audio_data = response.candidates[0].content.parts[0].inline_data.data
        if not audio_data:
            raise RuntimeError("Failed to generate audio: Empty audio data")
            
        self.save_wave_file(output_file, audio_data)
        return output_file
    
    def multi_speaker_tts(self, text: str, speakers: Dict[str, str],
                          output_file: str = 'output_multi.wav',
                          model: str = 'gemini-2.5-flash-preview-tts') -> str:
        """
        Convert text to speech with multiple speakers.
        
        Args:
            text: Text to convert (should include speaker names)
            speakers: Dict mapping speaker names to voice names
            output_file: Output filename
            model: Gemini model to use
            
        Returns:
            Path to the generated audio file
        """
        # Validate voices
        for speaker, voice in speakers.items():
            if voice not in self.VOICES:
                raise ValueError(
                    f"Voice '{voice}' for speaker '{speaker}' not supported. "
                    f"Choose from: {', '.join(self.VOICES)}"
                )
        
        if len(speakers) > 2:
            raise ValueError("Maximum 2 speakers supported")
        
        print(f"Generating multi-speaker audio with "
              f"{len(speakers)} speakers...")
        
        # Create speaker voice configs
        speaker_configs = []
        for speaker_name, voice_name in speakers.items():
            speaker_configs.append(
                types.SpeakerVoiceConfig(
                    speaker=speaker_name,
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voice_name,
                        )
                    )
                )
            )
        
        response = self.client.models.generate_content(
            model=model,
            contents=text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                        speaker_voice_configs=speaker_configs
                    )
                )
            )
        )
        
        # Extract audio data with proper error handling
        if (not response.candidates or
                not response.candidates[0].content or
                not response.candidates[0].content.parts or
                not response.candidates[0].content.parts[0].inline_data):
            raise RuntimeError(
                "Failed to generate audio: No audio data in response"
            )
        
        audio_data = response.candidates[0].content.parts[0].inline_data.data
        if not audio_data:
            raise RuntimeError("Failed to generate audio: Empty audio data")
            
        self.save_wave_file(output_file, audio_data)
        return output_file
    
    def generate_content(self, topic: str,
                         speakers: Optional[Dict[str, str]] = None,
                         generation_model: str = 'gemini-2.0-flash') -> str:
        """
        Generate content about a topic without converting to speech.
        
        Args:
            topic: Topic to generate content about
            speakers: Optional dict for multi-speaker format
            generation_model: Model to use for content generation
            
        Returns:
            Generated text content
        """
        print(f"Generating content about: {topic}")
        
        if speakers:
            speaker_names = list(speakers.keys())
            prompt = (
                f"Create a dialogue conversation about {topic}. "
                f"Use ONLY this exact format with no narrative text:\n\n"
                f"{speaker_names[0]}: Hello, let's discuss {topic}.\n"
                f"{speaker_names[1]}: Great idea! What's your "
                f"perspective?\n"
                f"{speaker_names[0]}: Well, I think...\n"
                f"{speaker_names[1]}: That's interesting...\n\n"
                f"Write 4-6 exchanges between {speaker_names[0]} and "
                f"{speaker_names[1]}. "
                f"Each line must start with the speaker name and colon. "
                f"NO story text, NO descriptions, ONLY dialogue lines."
            )
        else:
            prompt = (
                f"Generate a short, engaging explanation "
                f"(around 100 words) about {topic}."
            )
        
        # Generate the transcript
        transcript_response = self.client.models.generate_content(
            model=generation_model,
            contents=prompt
        )
        
        if transcript_response and transcript_response.text:
            return transcript_response.text.strip()
        else:
            raise Exception("Failed to generate content")

    def generate_and_speak(self, topic: str,
                           speakers: Optional[Dict[str, str]] = None,
                           output_file: str = 'generated_speech.wav',
                           generation_model: str = 'gemini-2.0-flash',
                           tts_model: str = 'gemini-2.5-flash-preview-tts'
                           ) -> str:
        """
        Generate content about a topic using one model, then convert to speech.
        
        Args:
            topic: Topic to generate content about
            speakers: Optional dict for multi-speaker
                     (speaker_name -> voice_name)
            output_file: Output filename
            generation_model: Model to use for content generation
            tts_model: Model to use for TTS
            
        Returns:
            Path to the generated audio file
        """
        print(f"Generating content about: {topic}")
        
        # Use the new generate_content method
        transcript = self.generate_content(topic, speakers, generation_model)
        print(f"Generated transcript:\n{transcript}\n")
        
        # Convert to speech
        if speakers:
            return self.multi_speaker_tts(transcript, speakers, output_file,
                                          tts_model)
        else:
            return self.single_speaker_tts(transcript, 'Kore', output_file,
                                           tts_model)


def main():
    """Main function to handle command line interface."""
    parser = argparse.ArgumentParser(
        description='Convert text to speech using Gemini API'
    )
    parser.add_argument('--text', '-t', type=str,
                        help='Text to convert to speech')
    parser.add_argument('--voice', '-v', type=str, default='Kore',
                        help='Voice to use for single speaker (default: Kore)')
    parser.add_argument('--output', '-o', type=str, default='output.wav',
                        help='Output filename (default: output.wav)')
    parser.add_argument('--multi-speaker', '-m', action='store_true',
                        help='Enable multi-speaker mode')
    parser.add_argument('--speakers', '-s', type=str, nargs='+',
                        help='Speaker configurations in format "Name:Voice" '
                             '(e.g., "Jane:Kore" "Joe:Puck")')
    parser.add_argument('--generate', '-g', type=str,
                        help='Generate content about this topic and '
                             'convert to speech')
    parser.add_argument('--list-voices', action='store_true',
                        help='List all available voices')
    parser.add_argument('--api-key', type=str,
                        help='Google AI API key (can also use '
                             'GOOGLE_API_KEY env var)')
    
    args = parser.parse_args()
    
    # List voices if requested
    if args.list_voices:
        print("Available voices:")
        for i, voice in enumerate(GeminiTTS.VOICES, 1):
            print(f"{i:2d}. {voice}")
        return
    
    try:
        # Initialize TTS client
        tts = GeminiTTS(api_key=args.api_key)
        
        if args.generate:
            # Generate content and convert to speech
            speakers_dict = None
            if args.multi_speaker and args.speakers:
                speakers_dict = {}
                for speaker_config in args.speakers:
                    if ':' not in speaker_config:
                        raise ValueError(
                            f"Invalid speaker format: {speaker_config}. "
                            f"Use 'Name:Voice'"
                        )
                    name, voice = speaker_config.split(':', 1)
                    speakers_dict[name.strip()] = voice.strip()
            
            tts.generate_and_speak(args.generate, speakers_dict, args.output)
            
        elif args.text:
            # Convert provided text to speech
            if args.multi_speaker and args.speakers:
                # Multi-speaker mode
                speakers_dict = {}
                for speaker_config in args.speakers:
                    if ':' not in speaker_config:
                        raise ValueError(
                            f"Invalid speaker format: {speaker_config}. "
                            f"Use 'Name:Voice'"
                        )
                    name, voice = speaker_config.split(':', 1)
                    speakers_dict[name.strip()] = voice.strip()
                
                tts.multi_speaker_tts(args.text, speakers_dict, args.output)
            else:
                # Single speaker mode
                tts.single_speaker_tts(args.text, args.voice, args.output)
        else:
            print("Please provide either --text or --generate option. "
                  "Use --help for more information.")
            
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
