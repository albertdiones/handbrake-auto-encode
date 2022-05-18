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
    outputDir = f"{directory}/{inputsConfig[inputsDir]['output']}";
    inputsDir = f"{directory}/{inputsDir}/";
    print(f"{inputsDir} target quality: {quality} output dir: {outputDir}")
    for file in os.listdir(inputsDir):

        if not re.search('\.(mp4|mov|mkv|m4v)$', file):
            continue

        print(f"Found file: {file}")

        video = f"{inputsDir}/{file}"

        newBaseName = os.path.basename(video)

        newFileName=f"{outputDir}/{newBaseName}"

        print(f"Encoding to {newFileName}")
        
        os.system('HandBrakeCLI -i "'+video+'" -o "'+newFileName+'" -q' + str(quality) + ' && mv "'+video+'" '+directory+'/trash/')
        encodedCount+=1
        


if  encodedCount==0:
    print("No video files found")
else:
    print(f"Encoded {encodedCount} videos")

