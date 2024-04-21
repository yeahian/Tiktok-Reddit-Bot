import os
import subprocess

"""
      In this file, you can crop your existing background video so that it fits to the phones aspect ratio

      DIRECTIONS: change the end of the mpr4_path so that it pulls your video
      *It is recommended that you use a similar directory to keep all files in a similar location
"""


print("\n" + "-------------Beginning of program------------")

# Input the path of the existing MP4 file
mp4_path = "/Users/*****/Documents/Tiktok Bot/(Your video to be cropped).mp4"


# Destination folder for the cropped video
destination = "/Users/iandahlin/Documents/vs python/Tiktok Bot/ytDownloads/Cropped"

# Output file name for the cropped video
output_file = os.path.join(destination, os.path.splitext(os.path.basename(mp4_path))[0] + "_cropped.mp4")

# Get video height
result = subprocess.Popen(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=height', '-of', 'csv=p=0', mp4_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
video_height, err = result.communicate()
video_height = int(video_height)

# Calculate new width
new_width = int((video_height * 9) / 16)

# Crop the video to fit a phone screen in portrait mode using ffmpeg
subprocess.run(['ffmpeg', '-i', mp4_path, '-vf', f'crop={new_width}:{video_height}', '-c:a', 'copy', output_file])

print("Video cropped successfully and saved to:", output_file)
print("-------------End of program-------------" + "\n")
