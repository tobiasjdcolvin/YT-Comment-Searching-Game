import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def main():
    api_service_name = "youtube"
    api_version = "v3"
    winner_info = "winner_info.txt"
    found = False
    comment_texts = []

    # PUT YOUR API KEY HERE
    DEVELOPER_KEY = "YOUR API KEY"
    # SET THE SECRET PASSWORD OR PASSPHRASE HERE
    SECRET_PASSWORD = "PASSWORD"
    # PUT THE ID OF THE VIDEO HERE
    VID_ID = "VID ID"

    # Search through comments:
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=VID_ID,
        maxResults=100
    )
    response = request.execute()
    print("processed first 100 comments")

    # Can only process 100 comments at a time, so do until no more comments exist:
    while 'nextPageToken' in response:
        # Add the text from every reply comment to the comment_texts list
        for item in response['items']:
            comment_texts.append("COMMENT:\t" + item['snippet']['topLevelComment']['snippet']['textDisplay'] + f"\t\tAUTHOR OF COMMENT: {item['snippet']['topLevelComment']['snippet']['authorDisplayName']}" + f"\nLINK TO COMMENT: https://www.youtube.com/watch?v={VID_ID}&lc={item['snippet']['topLevelComment']['id']}")

        new_request = youtube.commentThreads().list(
        part="snippet",
        videoId=VID_ID,
        maxResults=100,
        pageToken=response['nextPageToken']
        )
        # This is a new API call for every 100 comments
        response = new_request.execute()
        print("processed 100 comments")

    # Add the text from every reply comment to the comment_texts list
    for item in response['items']:
        comment_texts.append("COMMENT:\t" + item['snippet']['topLevelComment']['snippet']['textDisplay'] + f"\t\tAUTHOR OF COMMENT: {item['snippet']['topLevelComment']['snippet']['authorDisplayName']}" + f"\nLINK TO COMMENT: https://www.youtube.com/watch?v={VID_ID}&lc={item['snippet']['topLevelComment']['id']}")

    for text in comment_texts:
        # Test for if the secret password is found
        if SECRET_PASSWORD.lower() in text.lower():
            found = True
            print("\nFOUND SECRET PASSWORD\n")
            with open("winner_info.txt", "w") as f:
                f.write(text)
            make_private(VID_ID)
            break
    
    if not found:
        print("\nSecret password was not found.\n")

# Make the video private if the secret password is found    
def make_private(id):
    scopes = ["https://www.googleapis.com/auth/youtube"]

    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"
    
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().update(
        part="status",
        body={
        "id": id,
        "status": {
            "privacyStatus": "private"
        }
        }
    )

    response = request.execute()

    print(response)
    


if __name__ == "__main__":
    main()