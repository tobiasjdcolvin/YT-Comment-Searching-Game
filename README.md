# YouTube Video Comments Searching Game
A program utilizing the YouTube Data API that searches all of the comments of a YouTube video for a secret passphrase, and if found, makes the video private.

Demo: [https://youtu.be/b6WbJzR1cIc?si=ee56IfPnNM0QRYiH](https://youtu.be/b6WbJzR1cIc?si=ee56IfPnNM0QRYiH)

## How to use:
1. Sign in to the Google Cloud console, create a new project and enable the YouTube Data API v3
2. Go to the Credentials tab and create an API key as well as set up and create an OAuth 2.0 Client ID
3. Clone this repo
4. Download the Oath client, and store it in the same directory as the cloned repo as "client_secret.json"
5. Make sure you have Python3 installed, and if you haven't already, install virtualenv with "pip install virtualenv"
6. Navigate to the directory the cloned repo is stored in, and run "virtualenv my_env"
7. If you are on Linux or Mac, activate the virtual env using "source my_env/bin/activate", if on Windows, do "cd my_env" and then "Scripts\activate"
8. Run "pip install google_auth_oauthlib", and "pip install google-api-python-client"
9. Copy your API key and put it in the yt_api_test.py file, assigning it to the DEVELOPER_KEY constant
10. Choose a password or phrase to search for, and assign it to the SECRET_PASSWORD constant in yt_api_test.py
11. Find the video ID of the video you want to use this program for, and assign the id to the VID_ID constant in yt_api_test.py
12. Run the program with python3 yt_api_test.py
13. If the password was found, look in the winner_info.txt file to find information regarding the comment that was found, along with a link to that comment
