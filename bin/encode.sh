
DIR=$( cd -- "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && cd ..  && pwd )


#echo "Working Dir: $DIR"

encodedCount=0
for video in $DIR/inputs/*.*; do
    echo "Found file: $video"
    newFileName="$DIR/"$(basename $video)
    echo "Encoding to $newFileName"
    HandBrakeCLI -i "$video" -o "$newFileName" -q30 && mv "$video" $DIR/trash/
    encodedCount=(encodedCount+1)
done

if [ $encodedCount==0 ]; then
    echo "No video files found"
else
    echo "Encoded $encodedCount videos"
fi