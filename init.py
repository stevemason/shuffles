"""Reset auth starting from new authorisation code from Spotify."""
import requests
from sys import exit
from urllib.parse import urlencode
from config import client_id, client_secret, redirect_uri, https_proxy, use_proxy, verify_cert
from error import problem_check


def reinitialize(code):
    """Reset auth starting from new authorisation code from Spotify."""
    if use_proxy == True:
        proxy = {"https": https_proxy}
    else:
        proxy = None

    data = {"grant_type": "authorization_code",
            "code": code, "redirect_uri": redirect_uri}

    try:
        response = requests.post("https://accounts.spotify.com/api/token", proxies=proxy,
                                 verify=verify_cert, auth=(client_id, client_secret), data=data)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    problem_check(response)  # type: ignore

    rj = response.json()
    access_token = rj["access_token"]
    refresh_token = rj["refresh_token"]

    with open("access_token", 'w') as writer:
        writer.write(access_token)

    with open("refresh_token", 'w') as writer:
        writer.write(refresh_token)


def user_auth():
    """Generate Spotify user auth request URI."""
    scopes = "playlist-modify-private playlist-read-private"
    user_auth_uri = "https://accounts.spotify.com/authorize?" + \
        urlencode({"response_type": "code", "client_id": client_id,
                  "scope": scopes, "redirect_uri": redirect_uri})
    print(user_auth_uri)
