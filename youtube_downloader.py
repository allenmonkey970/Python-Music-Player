import os  # Importing the os module for file and directory operations
import yt_dlp as youtube_dl  # Importing yt_dlp for downloading and extracting audio from YouTube
import asyncio  # Importing asyncio for asynchronous I/O operations
from concurrent.futures import ThreadPoolExecutor  # Importing ThreadPoolExecutor for running tasks in separate threads

# Common options for youtube_dl
YDL_OPTS = {
    'format': 'bestaudio/best',  # Download the best available audio quality
    'outtmpl': 'assets/downloads/%(title)s.%(ext)s',  # Template for output file names
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
        'preferredcodec': 'mp3',  # Convert audio to MP3 format
        'preferredquality': '192',  # Set audio quality to 192 kbps
    }],
    'n_threads': 8,  # Number of threads to use for downloading
}

# Asynchronous function to download audio from a given URL
async def url_download(url):
    if url.lower() in ["n", "no"]:  # Check if the user input is "n" or "no" to cancel download
        print("Not downloaded")
        return

    try:
        with youtube_dl.YoutubeDL(YDL_OPTS) as ydl:
            info_dict = ydl.extract_info(url, download=True)  # Download the audio and get info
            title = info_dict.get('title', 'Unknown Title')  # Get the title of the downloaded file
            file_path = os.path.join('assets', 'downloads', f'{title}.mp3')

            # Check if the file was downloaded successfully and is not empty
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                print(f"Title: {title}")
                print("Download completed and verified successfully!")
            else:
                print("The downloaded file is corrupted or empty.")
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any errors encountered during download

# Asynchronous function to search for videos and download the selected one
async def search_and_download():
    while True:
        search_query = input("Enter the search query (or -1 to exit): ")  # Get search query from user
        if search_query == "-1":  # Exit the loop if user inputs "-1"
            break

        opts = YDL_OPTS.copy()  # Copy the common options
        opts.update({'default_search': 'ytsearch5'})  # Set options to search for the top 5 results on YouTube

        try:
            with youtube_dl.YoutubeDL(opts) as ydl:
                info_dict = ydl.extract_info(search_query, download=False)  # Search without downloading
                results = info_dict.get('entries', [])  # Get the list of search results

                if not results:  # If no results are found
                    print("No results found.")
                    continue

                # Display search results
                for index, video in enumerate(results):
                    print(f'{index + 1}. Title: {video["title"]}')
                    print(f'   URL: {video["webpage_url"]}')
                    print(f'   Duration: {video["duration"]} seconds')
                    print('---')

                choice = input("Enter the number of the video to download (-1 to exit): ")  # Get user choice
                if choice == "-1":  # Exit if user inputs "-1"
                    print("Not downloaded")
                    return

                try:
                    choice = int(choice) - 1  # Convert user choice to zero-based index
                    if 0 <= choice < len(results):  # Check if choice is valid
                        await url_download(results[choice]['webpage_url'])  # Download the selected video
                        return
                    else:
                        print("Invalid choice. Not downloaded.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")  # Print any errors encountered during search

# Function to run the asynchronous search_and_download function in a new event loop
def run_search_and_download():
    loop = asyncio.new_event_loop()  # Create a new event loop
    asyncio.set_event_loop(loop)
    loop.run_until_complete(search_and_download())  # Run the asynchronous function until complete

# Main entry point of the script
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=1) as executor:  # Use a ThreadPoolExecutor to run the function in a separate thread
        future = executor.submit(run_search_and_download)  # Submit the function to the executor
        future.result()  # Wait for the thread to complete
