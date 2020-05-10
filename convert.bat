mkdir outputs
for %%f in (*.*) do  ffmpeg -i "%%f" "outputs/%%f.mp3"