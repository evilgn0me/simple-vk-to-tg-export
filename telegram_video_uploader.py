#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import telegram
import os
import sys
import getopt
import asyncio


async def main():
    tg_token = ''
    tg_chat_id = ''
    owner_id = ''
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "t:o:c:")
    except:
        print("Error")
    for opt, arg in opts:
        if opt in ["-t"]:
            tg_token = arg
        elif opt in ["-o"]:
            owner_id = arg
        elif opt in ["-c"]:
            tg_chat_id = arg

    video_dir = str(owner_id).lstrip('-') + '-videos'

    file_name = str(video_dir) + '_last.txt'
    last = open(file_name, 'a+')
    count = 0
    for filename in os.listdir(video_dir):
        f = os.path.join(video_dir, filename)
        if os.path.isfile(f):
            if f in open(file_name).read():
                print('file exists in last')
            else:
                print('trying to upload ' + f)
                bot = telegram.Bot(token=tg_token)
                last.write(f + '\n')
                await bot.send_video(chat_id=tg_chat_id, video=open(f, 'rb'), supports_streaming=True)
                count = count + 1
                if count == 1:
                    print('count limit reached')
                    break

    last.close()


if __name__ == '__main__':
    asyncio.run(main())
