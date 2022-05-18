import os
import re
import yaml

directory=os.getcwd()


print(f"Working Dir: {directory}")

with open("config.yml", "r") as stream:
    try:
        inputsConfig = yaml.safe_load(stream)['video_inputs']
    except yaml.YAMLError as exception:
        print(exception)

encodedCount=0

for inputsDir in inputsConfig:
    quality = inputsConfig[inputsDir]['quality'];
    print(f"{inputsDir} target quality: {quality}")
    for file in os.listdir(f"{directory}/{inputsDir}/"):

        if not re.search('\.(mp4|mov|mkv|m4v)$', file):
            continue

        print(f"Found file: {file}")

        video = f"{directory}/inputs/{file}"

        newBaseName = os.path.basename(video)

        newFileName=f"{directory}/{newBaseName}"

        print(f"Encoding to {newFileName}")
        
        os.system('HandBrakeCLI -i "'+video+'" -o "'+newFileName+'" -q' + str(quality) + ' && mv "'+video+'" '+directory+'/trash/')
        encodedCount+=1
        


if  encodedCount==0:
    print("No video files found")
else:
    print(f"Encoded {encodedCount} videos")

