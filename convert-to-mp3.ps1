dir e:\YouTubeDownloads\*.mp4 | foreach-object { 
    $newname = $_.Name.Remove($_.Name.Length - $_.Extension.Length) + ".mp3"; 
.\ffmpeg.exe -i  $_ e:\YouTubeDownloads\$newname 
}
