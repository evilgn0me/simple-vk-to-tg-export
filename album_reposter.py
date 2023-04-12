#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import vk_api
import time
import random
import argparse


def get_photos_with_less_likes(vk, group_id):
    albums = vk.photos.getAlbums(owner_id=f"-{group_id}")["items"]
    photos = []
    for album in albums:
        album_id = album["id"]
        photos_in_album = vk.photos.get(
            owner_id=f"-{group_id}", album_id=album_id, extended=1
        )["items"]
        for photo in photos_in_album:
            likes = photo.get("likes", {}).get("count", 0)
            if likes < 5:
                photos.append(photo["id"])
    return photos


def main():
    parser = argparse.ArgumentParser(description="Post photos with less than 5 likes to VK group wall.")
    parser.add_argument("-t", "--token", help="VK user access token")
    parser.add_argument("-g", "--group_id", help="VK group ID")
    args = parser.parse_args()

    vk_session = vk_api.VkApi(token=args.token)
    vk = vk_session.get_api()

    photos = get_photos_with_less_likes(vk, args.group_id)
    random.shuffle(photos)

    current_time = time.time()
    tomorrow = time.localtime(current_time + 86400)
    post_time = time.mktime(
        (tomorrow.tm_year, tomorrow.tm_mon, tomorrow.tm_mday, 10, 0, 0, 0, 0, -1)
    )
    if post_time < current_time:
        post_time = time.mktime(
            (tomorrow.tm_year, tomorrow.tm_mon, tomorrow.tm_mday, 18, 0, 0, 0, 0, -1)
        )

    while photos:
        photo_id = photos.pop()
        attachments = f"photo-{args.group_id}_{photo_id}"
        vk.wall.post(
            owner_id=-int(args.group_id),
            attachments=attachments,
            publish_date=int(post_time)
        )
        post_time += 12 * 3600

if __name__ == "__main__":
    main()
