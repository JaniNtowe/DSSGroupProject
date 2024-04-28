CLIENT_ID = "d366004c041d48358884e2251d4265e9"
CLIENT_SECRET = "0b27658e6d8b4ff0bf09d6bcf0c9806b"
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
import requests
from requests import get
from requests import post
import json
import csv

from dotenv import load_dotenv

load_dotenv()

client_id1 = CLIENT_ID
client_secret1 = CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(
    client_id = client_id1,
    client_secret = client_secret1
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
def getToken():
    authString = client_id1 + ":" + client_secret1
    authBytes = authString.encode("utf-8")
    authBase64 = str(base64.b64encode(authBytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + authBase64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def getAuthheader(token):
    return {"Authorization": "Bearer " + token}

def getData(token, spotifyPlaylistID):
    url = "https://api.spotify.com/v1/playlists/" + spotifyPlaylistID + "/tracks"
    headers = getAuthheader(token)
    result = get(url, headers = headers)
    # if result.status_code == 200:
    playlist_data = result.json()
    items = playlist_data.get("items", [])
    # title = [item["track"]["name"] for item in items]
    # artist = [artist["name"] for item in items for artist in item["track"]["artists"]]
    trackURI = [item["track"]["uri"] for item in items]
    myList = []
    # titles = []
    # artists = []
    for x in range(len(trackURI)):
        myList.append(sp.audio_features(trackURI[x]))
    #     titles.append(title[x])
    #     artists.append(artist[x])
    #     print(title[x] + " by " + artist[x])
    #     print(sp.audio_features(trackURI[x]))
    # return myList, titles, artists
    return myList
    # else:
    #     print("Error")
    #     return[]
    # json_result = json.loads(result.content)
    # for i in range(len(json_result)):
    #     print(json_result[i])
    # print(json_result)
    # print(items)


token = getToken()
print(getData(token, "1YEEcmJEoPN3rMYmidOH7w"))

audioFeatures = getData(token, "1YEEcmJEoPN3rMYmidOH7w")
# audioFeatures, titles, names = getData(token, "5gVlReMeM1oXksvVNUAVtF")
# audioFeatures = data[0]
# titles = data[1]
# names = data[2]

# Specify the field names (column headers)
firstTrack = audioFeatures[0]
fieldnames = list(firstTrack[0].keys())  # Assuming all dictionaries have the same keys
# fieldnames.append("name")
# fieldnames.append("title")

# fieldnames += ["titles", "names"]     # Add "titles" and "names" to the fieldnames list

# Specify the CSV file path
csv_file_path = "output.csv"

# Write the data to the CSV file
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row with field names
    for x in range(len(audioFeatures)):
        writer.writerows(audioFeatures[x])
    # for row, title in zip(audioFeatures, titles):
    #     row["title"] = title
    #     writer.writerow(row)





# with open("spotify_data.json", "w") as json_file:
#     json.dump(getData(token, "209PxUBxiXpVNX77OUEgCN"), json_file)

# json_data = getData(token, "209PxUBxiXpVNX77OUEgCN")
# columns = list(json_data[0].keys())

# Specify the output CSV file path
# csv_file_path = "audio_features.csv"
# array_of_dicts = getData(token, "209PxUBxiXpVNX77OUEgCN")
# fieldnames = array_of_dicts[0].keys()
# with open(csv_file_path, mode="w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()  # Write the header row with field names
#     writer.writerows(array_of_dicts)

# # Write JSON data to CSV file
# with open(csv_file_path, 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=columns)
#
#     # Write header row
#     writer.writeheader()

# Write data rows
# for item in json_data:
#     writer.writerow(item)


# def json_to_csv():
#     with open("spotify_data.json", "r") as json_file:
#         data = json.load(json_file)
#
#     # Extract relevant information from JSON data
#     # Modify this part according to your JSON structure
#     extracted_data = []
#     for item in data["items"]:
#         track_name = item["track"]["name"]
#         artist_name = item["track"]["artists"][0]["name"]
#         audio_features = sp.audio_features(item["track"]["uri"])  # Assuming sp is your Spotify API object
#         if audio_features:
#             audio_features = audio_features[0]  # Assuming audio_features is a list with a single dictionary
#             # Append track name, artist name, and audio features to extracted data
#             extracted_data.append((track_name, artist_name, audio_features))
#
#     # Write extracted data to CSV file
#     with open("spotify_data.csv", "w", newline="", encoding="utf-8") as csv_file:
#         writer = csv.writer(csv_file)
#         # Write header
#         writer.writerow(["Track Name", "Artist Name", "Audio Features"])
#         # Write rows
#         for row in extracted_data:
#             writer.writerow(row)



# json_to_csv()
