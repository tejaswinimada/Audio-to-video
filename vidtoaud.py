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


