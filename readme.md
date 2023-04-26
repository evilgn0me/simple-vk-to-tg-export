Social Network Tools
=====

Repo contains from various scripts that I use to automatically manage various tasks in social networks.

At first you need to install dependencies:
```
python3 -m pip install -r requirements.txt
```

**vk_photo_downloader.py** - downloads all photos it can find from vk wall by owner id, it will create directory with owner_id as directory name.

**telegram_photo_uploader.py** - checks for files in owner_id directory and uploads them to telegram channel. Upload limit is hardcoded to 1 photo per run right now.

**vk_user_client_token.py** - needed to create user_client_token to use some specific vk api like photo posting.

**vk_album_reposter.py** - will check photos in group albums that are less than 5 like on them and repost them on group wall. Requires user_client_token

**vk_video_downloader.py** - will do same as vk_photo_downloader, but will download videos instead. You need to install [youtube-dl](https://github.com/ytdl-org/youtube-dl#installation) for this script to work.

Each script receives credentials command line arguments. 