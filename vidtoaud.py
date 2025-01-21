from moviepy import *
def extract_audio(video_file, output_audio_file):
    try:
        # Load the video file
        video = VideoFileClip(video_file)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to a file
        audio.write_audiofile(output_audio_file)
        
        print(f"Audio successfully extracted to {output_audio_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_file = "ranaha.mp4"  # Replace with your uploaded video file name
output_audio_file = "output_audio.mp3"  # Desired output audio file name ......code to convert the video into audio format.
extract_audio(video_file, output_audio_file)

#code to convert the audio into text format but not working.
# import speech_recognition as sr
# from pydub import AudioSegment

# def transcribe_audio(audio_file):
#     try:
#         # Convert MP3 to WAV if needed
#         if audio_file.endswith(".mp3"):
#             audio = AudioSegment.from_mp3(audio_file)
#             wav_file = audio_file.replace(".mp3", ".wav")
#             audio.export(wav_file, format="wav")
#         else:
#             wav_file = audio_file

#         # Initialize recognizer
#         recognizer = sr.Recognizer()

#         # Load the audio file
#         with sr.AudioFile(wav_file) as source:
#             print("Recognizing speech...")
#             audio_data = recognizer.record(source)
        
#         # Perform speech recognition
#         text = recognizer.recognize_google(audio_data)
#         return text
#     except Exception as e:
#         return f"An error occurred: {e}"

# # Example usage
# audio_file = "output_audio.mp3"  # Replace with your audio file
# transcribed_text = transcribe_audio(audio_file)
# print("Extracted Speech:\n", transcribed_text)
# import os
# import whisper

# def transcribe_audio_with_whisper(audio_file):
#     try:
#         # Set cache directory for Whisper model weights
#         os.environ["WHISPER_CACHE_DIR"] = "./cache"
        
#         # Load the Whisper model
#         model = whisper.load_model("base")
        
#         # Transcribe the audio file
#         print("Transcribing audio...")
#         result = model.transcribe(audio_file)
#         return result["text"]
#     except Exception as e:
#         return f"An error occurred: {e}"

# # Example usage
# audio_file = "output_audio.mp3"  # Replace with the correct path
# transcribed_text = transcribe_audio_with_whisper(audio_file)
# print("Extracted Speech:\n", transcribed_text)




# code to analyze the emotion of the context.simple
# from transformers import pipeline

# def analyze_emotion(text):
#     try:
#         # Load the pre-trained model for emotion analysis
#         emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
        
#         # Analyze the emotion of the text
#         results = emotion_analyzer(text)
        
#         # Print each emotion and its confidence
#         print("Emotion Analysis Results:")
#         for result in results:
#             print(f"Emotion: {result['label']}, Confidence: {result['score']:.2f}")
        
#         # Extract the dominant emotion
#         dominant_emotion = max(results, key=lambda x: x['score'])
#         print(f"\nDominant Emotion: {dominant_emotion['label']} with Confidence: {dominant_emotion['score']:.2f}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example text
# text = """
# i am in mixed emotion of happy  and joy
# """
# analyze_emotion(text)

