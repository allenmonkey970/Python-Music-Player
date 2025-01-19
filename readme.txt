### How to Install FFmpeg on Windows

1. Download FFmpeg:
   - Visit the [FFmpeg download page](https://www.ffmpeg.org/download.html).
   - Navigate to the Windows builds from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
   - Download the `ffmpeg-git-full.7z` file.

2. Extract the Files:
   - Extract the downloaded `ffmpeg-git-full.7z` file.
   - Name the folder ffmpeg
   - Move the extracted folder to `C:\`. (I use WINRAR not sure if required)

3. Restart Your Computer:
   - Restart your computer to ensure all changes take effect.

4. Add FFmpeg to System Path:
   - Open Advanced System Settings.
   - Click on the Environment Variables button.
   - In the System variables section, find the `Path` variable and click Edit.
   - Click New and add the path to the `bin` folder of your FFmpeg installation (e.g., `C:\ffmpeg\bin`).
   - Click OK to close all windows.


# pip installs
    - pip install yt_dlp
    - pip install pygame
    - pip install asyncio