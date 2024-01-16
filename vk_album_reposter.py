#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import vk_api
import time
import random
import argparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("script_log.txt"),
        logging.StreamHandler()
    ]
)

def get_photos_with_less_likes(vk, group_id):
    albums = vk.photos.getAlbums(owner_id=f"-{group_id}")["items"]
    photos = []
    for album in albums:
        album_id = album["id"]
        offset = 0
        while True:
            photos_in_album = vk.photos.get(
                owner_id=f"-{group_id}",
                album_id=album_id,
                extended=1,
                offset=offset
            )
            items = photos_in_album["items"]
            if not items:
                break  # Break if no more photos in album
            for photo in items:
                likes = photo.get("likes", {}).get("count", 0)
                if likes < 5:
                    photos.append(photo["id"])
            offset += len(items)  # Increase offset for next batch
    return photos

def main():
    parser = argparse.ArgumentParser(description="Post photos with less than 5 likes to VK group wall.")
    parser.add_argument("-t", "--token", help="VK user access token")
    parser.add_argument("-g", "--group_id", help="VK group ID")
    args = parser.parse_args()

    vk_session = vk_api.VkApi(token=args.token)
    vk = vk_session.get_api()

    photos = get_photos_with_less_likes(vk, args.group_id)
    logging.info(f"Found photos {photos}")
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
        try:
            vk.wall.post(
                owner_id=-int(args.group_id),
                attachments=attachments,
                publish_date=int(post_time)
            )
            logging.info(f"Posted photo-{args.group_id}_{photo_id} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(post_time))}")
        except vk_api.exceptions.Captcha as e:  # Replace with the specific exception if different
            logging.error(f"Error posting photo-{args.group_id}_{photo_id}: Captcha needed")
            break  # Break the loop if a captcha is needed
        except Exception as e:
            logging.error(f"Error posting photo-{args.group_id}_{photo_id}: {e}")
        post_time += 12 * 3600


if __name__ == "__main__":
    main()