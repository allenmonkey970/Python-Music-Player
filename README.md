# Python-Music-Player

## Prerequisites

1. **FFmpeg Installation:**

### How to Install FFmpeg on Windows

1. **Download FFmpeg:**
   - Visit the [FFmpeg download page](https://www.ffmpeg.org/download.html).
   - Navigate to the Windows builds from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
   - Download the `ffmpeg-git-full.7z` file.

2. **Extract the Files:**
   - Extract the downloaded `ffmpeg-git-full.7z` file.
   - Name the folder `ffmpeg`.
   - Move the extracted folder to `C:\`. (WINRAR may be required)

3. **Restart Your Computer:**
   - Restart your computer to ensure all changes take effect.

4. **Add FFmpeg to System Path:**
   - Open Advanced System Settings.
   - Click on the Environment Variables button.
   - In the System variables section, find the `Path` variable and click Edit.
   - Click New and add the path to the `bin` folder of your FFmpeg installation (e.g., `C:\ffmpeg\bin`).
   - Click OK to close all windows.

2. **Python Package Installation:**

```bash
pip install yt_dlp
pip install pygame
pip install asyncio
```

3. **Cookies Export:**
   - Install the [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) extension.
   - Go to YouTube and export the cookies.
   - Save the exported cookies to a file named `cookies.txt`.

## Usage

1. **Initialize the Player:**
   - The player uses the `pygame` library to handle audio playback.

2. **Directory Structure:**
   - Ensure the following directories exist and contain your .mp3 files:
     - `./assets/oldies`
     - `./assets/democrazy`
     - `./assets/heavy`
     - `./assets/downloads`

3. **Running the Player:**
   - Execute the `main.py` file to start the player.
   - The player will scan the directories and create playlists.

4. **Player Controls:**
   - **Press 'p'** to pause
   - **Press 'r'** to resume
   - **Press '-'** to lower volume
   - **Press '+'** to raise volume
   - **Press 'c'** to change playlist
   - **Press 'n'** to skip to the next song
   - **Press 'b'** to go back to the previous song
   - **Press 's'** to shuffle the playlist
   - **Press 'e'** to exit the program
   - **Press 'd'** to download music from YouTube

## Main Code File

The main code file (`main.py`) initializes the player, scans the directories for music files, and provides functions to manage playlists and control playback.

## YouTube Downloader Script

The `youtube_downloader.py` script contains functions to download audio from YouTube and search for videos based on user input. It uses `yt_dlp` for downloading and extracting audio, and `asyncio` for asynchronous I/O operations.
