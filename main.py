from pygame import mixer
import random
import asyncio
import os
from youtube_downloader import url_download, search_and_download

# Initialize the mixer
mixer.init()

# Function to get all .mp3 files in a directory
async def get_music_files(directory):
    try:
        return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".mp3")]
    except FileNotFoundError:
        print(f"Directory {directory} not found.")
        return []

# Used directories for different playlists
directories = {
    "oldies": './assets/oldies',
    "democrazy": './assets/democrazy',
    "heavy": './assets/heavy',
    "downloads": './assets/downloads'
}

# Check and create directories if they don't exist
for directory in directories.values():
    os.makedirs(directory, exist_ok=True)

# Function to get all playlists
async def get_playlists(directories):
    playlists = {name: await get_music_files(directory) for name, directory in directories.items()}
    playlists["all"] = sum(playlists.values(), [])
    return playlists

# Function to update the downloads playlist
async def update_downloads_playlist(playlists):
    playlists["downloads"] = await get_music_files(directories["downloads"])
    playlists["all"] = sum(playlists.values(), [])
    print("Updated downloads playlist:", [os.path.basename(file) for file in playlists["downloads"]])

# Function to choose a playlist
def choice(playlists):
    while True:
        for name, files in playlists.items():
            print(f"{name} = {[os.path.basename(file) for file in files]}")

        user_choice = input("What playlist do you want to play: ").strip().lower()
        if user_choice in playlists and playlists[user_choice]:
            return playlists[user_choice]
        else:
            print("Playlist is empty or invalid. Please choose a different playlist.")

# Function to play music from the chosen playlist
async def music_play(playlist, playlists):
    if not playlist:
        print("The playlist is empty.")
        return

    volume = 0.5
    current_index = 0

    while True:
        print(f"Loading file: {playlist[current_index]}")
        mixer.music.load(playlist[current_index])
        mixer.music.play()
        mixer.music.set_volume(volume)

        while True:
            # Print options for user to control the music player
            print("Press 'p' to pause, 'r' to resume")
            print("Press '-' or '+' to lower or raise volume")
            print("Press 'c' to change playlist")
            print("Press 'n' to skip to the next song")
            print("Press 'b' to go back to the previous song")
            print("Press 's' to shuffle the playlist")
            print("Press 'e' to exit the program")
            print("Press 'd' to download music from YouTube")
            option = input("  ").strip().lower()

            # Handle user input for controlling the music player
            if option in ['p', 'pause']:
                mixer.music.pause()
            elif option in ['r', 'resume']:
                mixer.music.unpause()
            elif option in ['e', 'exit']:
                mixer.music.stop()
                return
            elif option == '-':
                volume = max(0, volume - 0.1)
                mixer.music.set_volume(volume)
            elif option == '+':
                volume = min(1, volume + 0.1)
                mixer.music.set_volume(volume)
            elif option in ['c', 'change']:
                playlist = choice(playlists)
                if not playlist:
                    print("The new playlist is empty.")
                    continue
                current_index = 0
                break
            elif option in ['n', 'next']:
                current_index = (current_index + 1) % len(playlist)
                break
            elif option in ['b', 'back']:
                current_index = (current_index - 1) % len(playlist)
                break
            elif option in ['s', 'shuffle']:
                random.shuffle(playlist)
                current_index = 0
                break
            elif option in ['d', 'download']:
                mixer.music.stop()
                use = input("Download from URL (Y or N): ").strip().lower()
                if use in ["y", "yes"]:
                    url = input("Enter the URL of the video (n to break): ")
                    if url.lower() not in ["n", "no"]:
                        try:
                            await url_download(url)
                        except Exception as e:
                            print(f"Error downloading from URL: {e}")
                else:
                    try:
                        await search_and_download()
                    except Exception as e:
                        print(f"Error searching and downloading: {e}")
                await update_downloads_playlist(playlists)
                playlist = playlists["downloads"]
                if not playlist:
                    print("The updated playlist is empty.")
                    continue
                current_index = 0

# Main function to start the music player
async def main():
    playlists = await get_playlists(directories)
    playlist = choice(playlists)
    await music_play(playlist, playlists)

if __name__ == "__main__":
    asyncio.run(main())
