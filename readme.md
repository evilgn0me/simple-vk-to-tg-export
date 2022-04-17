Simple-VK-to-TG-export
=====

I generally use that to export photos from vk wall to telegram channel.
At first you need to install dependencies:
```
python3 -m pip install -r requirements.txt
```

This telegram export contains from two files.
```
downloader.py - downloads all photos it can find from vk, it will create directory with owner_id as directory name.
uploader.py - checks for files in owner_id directory and uploads them to telegram channel
```

Usage
====
```
downloader.py -t 'vk_bot_token' -o 'vk_wall_owner_id'

uploader.py -t 'telegram_bot_token' -c 'telegram_chat_id' -o 'vk_wall_owner_id'
```