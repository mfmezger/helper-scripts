# imports
from moviepy.editor import VideoFileClip


# main method
def main():

    # Open the video file
    video = VideoFileClip("Coaching Corner Teaser - Folge 1.mp4")

    # Extract the audio
    audio = video.audio

    # Write the audio to a file
    audio.write_audiofile("audio.mp3")


if __name__ == "__main__":
    main()
