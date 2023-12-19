import googleapiclient.discovery

api_key = 'AIzaSyAk1laDO18UKtMOPd2N4CiOvpMQ5xt4oIg'
video_id = 'Lj5Ye1o3OWg'

def fetch_comments(api_key, video_id, max_results=100, max_pages=None):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    page_token = None
    page_count = 0

    # Specify the full path of the file
    file_path = r'C:\Users\hp\Desktop\Code\Python\text.txt'  # Change this to your desired file path

    with open(file_path, 'w', encoding='utf-8') as file:
        while True:
            request = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                maxResults=max_results,
                pageToken=page_token
            )

            try:
                response = request.execute()
                comments = response.get('items', [])
                if not comments:
                    print("No comments found.")
                    break

                for comment in comments:
                    text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
                    file.write(text + '\n')
                    print(text)

                page_count += 1
                print(f"Fetched page {page_count}")

                page_token = response.get('nextPageToken')
                if not page_token or (max_pages and page_count >= max_pages):
                    break

            except Exception as e:
                print(f"An error occurred: {e}")
                break

    print(f'Comments written to {file_path}')

# Adjust parameters as needed
fetch_comments(api_key, video_id, max_results=10, max_pages=1)
