#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import getopt
import requests


def main():
    # Your VK application ID
    client_id = ""
    # Your VK application secret key
    app_secret_key = ""
    argv = sys.argv[1:]

    opts = []
    try:
        opts, args = getopt.getopt(argv, "c:k:")
    except:
        print("Error")
    for opt, arg in opts:
        if opt in ["-c"]:
            client_id = arg
        elif opt in ["-k"]:
            app_secret_key = arg

    # The permissions your application needs
    scope = "wall"

    # The URL to redirect the user to after they grant permission
    redirect_uri = "https://oauth.vk.com/blank.html"

    # The authorization URL to redirect the user to
    auth_url = f"https://oauth.vk.com/authorize?client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}&response_type=code&v=5.131"

    # Open the authorization URL in a web browser and wait for the user to grant permission
    print(auth_url)
    authorization_code = input("Enter the authorization code: ")

    # Exchange the authorization code for a user access token
    token_url = "https://oauth.vk.com/access_token"
    params = {
        "client_id": client_id,
        "client_secret": app_secret_key,
        "redirect_uri": redirect_uri,
        "code": authorization_code,
    }
    response = requests.post(token_url, params=params).json()
    user_access_token = response["access_token"]

    print(f"Your user access token is: {user_access_token}")


if __name__ == "__main__":
    main()
