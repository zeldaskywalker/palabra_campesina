from django.urls import path
import json
import requests

import os

def get_stories_all():
    # AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")
    AUTHORIZATION_TOKEN = 'mm7iccB819ZEZwnmTadyksgCrz5HfZvc'
    AUTH_STRING = "Token " + AUTHORIZATION_TOKEN
    data = requests.get(
        "https://api.baserow.io/api/database/rows/table/392019/?user_field_names=true",
        headers={
            "Authorization": AUTH_STRING
            }).json()

    return data["results"]

def get_story(row_id):
    AUTHORIZATION_TOKEN = 'mm7iccB819ZEZwnmTadyksgCrz5HfZvc'
    # AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")
    AUTH_STRING = "Token " + AUTHORIZATION_TOKEN
    request_string = "https://api.baserow.io/api/database/rows/table/392019/" + str(row_id) + "/?user_field_names=true"
    data = requests.get(
        request_string,
        headers={
            "Authorization": AUTH_STRING
            }).json()

    return data


def get_gallery_all_images():
    AUTHORIZATION_TOKEN = 'mm7iccB819ZEZwnmTadyksgCrz5HfZvc'
    # AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")
    AUTH_STRING = "Token " + AUTHORIZATION_TOKEN
    data = requests.get(
        "https://api.baserow.io/api/database/rows/table/392021/?user_field_names=true",
        headers={
            "Authorization": AUTH_STRING
            }).json()

    return data["results"]

def get_gallery_image_singular(row_id):
    AUTHORIZATION_TOKEN = 'mm7iccB819ZEZwnmTadyksgCrz5HfZvc'
    # AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")
    AUTH_STRING = "Token " + AUTHORIZATION_TOKEN
    request_string = "https://api.baserow.io/api/database/rows/table/392021/" + str(row_id) + "/?user_field_names=true"
    data = requests.get(
        request_string,
        headers={
            "Authorization": AUTH_STRING
            }).json()

    return data