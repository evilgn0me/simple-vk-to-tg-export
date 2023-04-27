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

    image_dir = str(owner_id).lstrip('-')

    file_name = str(image_dir) + '_last.txt'
    last = open(file_name, 'a+')
    count=0
    for filename in os.listdir(image_dir):
        f = os.path.join(image_dir, filename)
        if os.path.isfile(f):
            if f in open(file_name).read():
                print('file exits in last')
            else:
                bot = telegram.Bot(token=tg_token)
                await bot.sendPhoto(chat_id=tg_chat_id, photo=open(f, 'rb'))
                last.write(f + '\n')
                count = count + 1
                if count == 1:
                   print('count limit reached')
                   break

    last.close()
             
                 
if __name__ == '__main__':
    asyncio.run(main())