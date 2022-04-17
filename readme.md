Simple-VK-to-TG-export
=====

Those scripts generally download photos from vk wall and uploads them one by one to telegram channel.

At first you need to install dependencies:
```
python3 -m pip install -r requirements.txt
```

This telegram export contains from two files.
**downloader.py** - downloads all photos it can find from vk wall by owner id, it will create directory with owner_id as directory name.
**uploader.py** - checks for files in owner_id directory and uploads them to telegram channel. Upload limit is hardcoded to 1 photo per run right now.


Usage
====
```
downloader.py -t 'vk_bot_token' -o 'vk_wall_owner_id'

uploader.py -t 'telegram_bot_token' -c 'telegram_chat_id' -o 'vk_wall_owner_id'
```