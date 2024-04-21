from gtts import gTTS 
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import random
import os



#The text that you want to convert to audio
'''
    THIS IS THE INFORMATION TO BE CHANGED FOR EACH SPECIFIC VIDEO

    TODO - change the redditStringInput to the reddit post text
         - change the mp4 to whichever background video you would like

    (Other Changes)
        - Use tiktokCropper.py to make the video the correct aspect ratio

    CapCut
        - Auto Captions
        - Basic -> Font: 15, First text Preset
        - Animation -> Spring
        *Captions have not been integrated into the program yet but it is being looked into
                    
'''

def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path}")

#deleting old audio files
delete_file_if_exists("/Users/*****/Documents/vs python/Tiktok Bot/testingSpedUp.mp3")

redditStringInput = "Part 2, Not the A hole. Naming a child is a two yes and one no situation. Means you need two times yes for a name to be it and one no to make sure that name is not the name you choose. Works both ways if you’d ask me. Also, I am not a fan of naming the first name of a child after a parent. Because then the child will always be compared to their parents and need to fight harder to be their own person. I have less problems with the middle name being connected to someone else (parents, grandparents) because that is only a formal name and not used in everyday business.  Why is he dead set on Stuarta? I mean, there are so many beautiful names but he only wants to name his daughter after him? Why not after the mother? Like your name junior. It is a bit misogynistic to only want to name the baby after the father. Whose last name will the baby get? His as well? Maybe you could find a way, like name the baby with the same first letter as your husband (Stella, Sally, Sanne, etc). Make sure the baby has a middle name (if she shares the same last name as her father). Because it will be annoying for simple things like mail and stuff."




#mp3 should never change, mp4 is the background video which will if you choose
mp3_path = "/Users/*****/Documents/vs python/Tiktok Bot/testing.mp3"
mp4_path = "/Users/*****/Documents/vs python/Tiktok Bot/ytDownloads/(Your video here).mp4"


clip_output_path = "/Users/*****/Documents/vs python/Tiktok Bot/clipGeneration/random_clip.mp4"



'''
                                    THE SECTION BELOW IS MEANT TO CHOOSE THE ACCENT
                                    AND CHANGE THE SPEED OF THE AUDIO CLIP (mp3)
'''


#specifying the accent and other values to determine the voice of the bot, and finally saving the video
language = 'en-au'
mySound = gTTS(text=redditStringInput, lang=language, slow=False) 
mySound.save("testing.mp3") 

def spedUP(audioInput, audioOutput, speedRate=1.1):
    # Loading the audio file
    audio = AudioSegment.from_file(audioInput, format="mp3")

    # Speeding up the audio
    increasedSpeedAudio = audio.speedup(playback_speed=speedRate)

    # Saving the file
    increasedSpeedAudio.export(audioOutput, format="mp3")



# Specify the input and output paths for the respective files *DO NOT CHANGE
mp3_input_path = "/Users/*****/Documents/vs python/Tiktok Bot/testing.mp3"
mp3_output_path = "/Users/*****/Documents/vs python/Tiktok Bot/testingSpedUp.mp3"

#calling the function to make the changes
spedUP(mp3_input_path, mp3_output_path)
print(" -----Audio has been sped up.")


'''
                THIS SECTION FINDS THE DURATION OF THE VIDEO SO THAT WE CAN SELECT A RANDOM CLIP
                FROM THE MP4 FILE WHICH IS THE SAME LENGTH TO AVOID REPETITITION
'''


def getVideoDuration(audio_path):
    # Loading the audio file
    audio = AudioSegment.from_file(audio_path)

    # Get the duration in seconds (made so that it finds duration to the thousandth place)
    mp3Duration = len(audio) / 1000.0
    return mp3Duration


# Get the duration of the audio file
duration = getVideoDuration(mp3_output_path)
print(f" -----The audio is {duration} seconds.")




original_clip = VideoFileClip(mp4_path)
frame_rate = original_clip.fps
total_frames = int(original_clip.duration * frame_rate)
start_frame = random.randint(0, total_frames - int(duration * frame_rate))
start_time = start_frame / frame_rate

# Extract the random clip from the original video
random_clip = original_clip.subclip(start_time, start_time + duration)

# Write the random clip to the specified output path
random_clip.write_videofile(clip_output_path, codec="libx264", audio_codec="aac")

# Close the original and random clips
original_clip.close()
random_clip.close()

print(f" ----Random clip has been generated and saved to: {clip_output_path}")




'''
                        PUTTING THE TWO FILES TOGETHER WITH THE MP3 OVER THE MP4

'''

#loading the clips together so we get the mp3 audio and mp4 video
vidClip = VideoFileClip(clip_output_path)
audioClip = AudioFileClip(mp3_output_path)

vidWithAudio = CompositeVideoClip([vidClip.set_audio(audioClip)])

outputPath = "/Users/*****/Documents/vs python/Tiktok Bot/tiktokOutputs/combined_audio_and_video.mp4"
vidWithAudio.write_videofile(outputPath, codec="libx264", audio_codec="aac")

print(" -----Video with audio has been created:", outputPath)





