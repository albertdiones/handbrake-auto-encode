import os
import re

directory=os.getcwd()


print(f"Working Dir: {directory}")

encodedCount=0

for file in os.listdir(f"{directory}/inputs/"):

    if not re.search('\.(mp4|mov|mkv|m4v)$', file):
        continue

    print(f"Found file: {file}")

    video = f"{directory}/inputs/{file}"

    newBaseName = os.path.basename(video)

    newFileName=f"{directory}/{newBaseName}"

    print(f"Encoding to {newFileName}")
    
    os.system('HandBrakeCLI -i "'+video+'" -o "'+newFileName+'" -q30 && mv "'+video+'" '+directory+'/trash/')
    encodedCount+=1
    


if  encodedCount==0:
    print("No video files found")
else:
    print(f"Encoded {encodedCount} videos")

