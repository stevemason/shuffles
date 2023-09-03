"""Shuffle playlist randomly."""
import requests
from secrets import randbelow
from urllib.parse import urlencode
from config import https_proxy, client_id, client_secret, use_proxy, verify_cert
from error import problem_check


def shuffle(playlist):
    """Shuffle playlist randomly."""
    if use_proxy == True:
        proxy = {"https": https_proxy}
    else:
        proxy = None

    tracks_no = get_tracks(playlist, proxy)
    move_tracks(tracks_no, playlist, proxy)
    print("Shuffles completed")


def get_tracks(playlist, proxy):
    """Return number of tracks in given playlist."""
    params = {"fields": "name,tracks.total"}

    uri = "https://api.spotify.com/v1/playlists/" + \
        playlist+"?"+urlencode(params)

    for _ in range(2):  # be ready to make the request a 2nd time if token has expired
        with open("access_token", 'r') as reader:
            access_token = reader.readline()
        headers = {"Authorization": "Bearer "+access_token}

        try:
            response = requests.get(uri, headers=headers,
                                    proxies=proxy, verify=verify_cert)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        if response.status_code == 401:
            refresh()
        else:
            break

    problem_check(response)  # type: ignore

    rj = response.json()  # type: ignore
    playlist_name = rj["name"]
    print("Shuffling playlist: "+playlist_name)
    return rj["tracks"]["total"]


def move_tracks(tracks_no, playlist, proxy):
    """Shuffle (move) tracks in given playlist, based on Fisher-Yates shuffle algorithm."""
    uri = "https://api.spotify.com/v1/playlists/" + \
        playlist+"/tracks"

    for track in range(tracks_no, 1, -1):  # work back from the end of the playlist
        for _ in range(2):  # be ready to make the request a 2nd time if token has expired
            with open("access_token", 'r') as reader:
                access_token = reader.readline()
            headers = {"Authorization": "Bearer "+access_token}
            # replace track at current position with random track from tracks up to and including this one
            data = {"range_start": randbelow(track), "insert_before": track}

            try:
                response = requests.put(uri, headers=headers,
                                        proxies=proxy, verify=verify_cert, json=data)
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)

            if response.status_code == 401:
                refresh()
            else:
                break
        problem_check(response)  # type: ignore


def refresh():
    """Refresh access token."""
    with open("refresh_token", 'r') as reader:
        refresh_token = reader.readline()
    refresh_uri = "https://accounts.spotify.com/api/token"

    if use_proxy == True:
        proxy = {"https": https_proxy}
    else:
        proxy = None

    data = {"grant_type": "refresh_token", "refresh_token": refresh_token}

    try:
        response = requests.post(refresh_uri, proxies=proxy, data=data,
                                 verify=verify_cert, auth=(client_id, client_secret))
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    problem_check(response)  # type: ignore

    rj = response.json()
    access_token = rj["access_token"]
    with open("access_token", 'w') as writer:
        writer.write(access_token)
