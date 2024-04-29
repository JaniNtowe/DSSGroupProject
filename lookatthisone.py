# client ID and secret which is required in order to pull data
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

# creating the spoptipy object that has the method to call the audio features
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
    # the endpoint that specifies what action we are trying to do 
    # - pulling the items of the playlist
    # by inputing a string of the spotifyPlaylistID, we can specify which
    # playlist we are trying to pull the items from
    url = "https://api.spotify.com/v1/playlists/" + spotifyPlaylistID + "/tracks"
    # generates an authorization header using the generated token
    headers = getAuthheader(token)
    # requesting the data from Spotify
    result = get(url, headers = headers)
    # turning the results into a json file
    playlist_data = result.json()
    items = playlist_data.get("items", [])
    # getting the track URI of each items pulled from the playlist
    trackURI = [item["track"]["uri"] for item in items]
    myList = []
    # creating an array of the result of calling the audio features of 
    # each item of the playlist
    for x in range(len(trackURI)):
        myList.append(sp.audio_features(trackURI[x]))
    return myList

# calling the method that creates the token
token = getToken()

# getting the list result of the audiofeatures of every song returned
audioFeatures = getData(token, "1YEEcmJEoPN3rMYmidOH7w")

# because audioFeatures returns an array of lists of data, specifying that the 
# desired audio features are in the first dictionary
firstTrack = audioFeatures[0]

# making the column headers the keys of the dictionary
fieldnames = list(firstTrack[0].keys())  

# specifying the name of the output file
csv_file_path = "output.csv"

# writing the data into the csv file
with open(csv_file_path, mode="w", newline="") as file:
    # making the dictionary keys the header of each column
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  
    for x in range(len(audioFeatures)):
        # writing the data in
        writer.writerows(audioFeatures[x])

