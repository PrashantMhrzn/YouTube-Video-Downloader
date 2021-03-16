import argparse
from utils import Downloader


parser = argparse.ArgumentParser(description='Downloads given video or a playtlist from youtube.')
parser.add_argument('-v', '--video_link', metavar='', help='Link of the video you want to download.')
parser.add_argument('-p', '--playlist_link',  metavar='', help='Link of the playlist you want to download.')
parser.add_argument('-m', '--multiple_link',  nargs='+', metavar='', help='Links of the videos you want to download.(Seperated with <space>)')
args = parser.parse_args()

d = Downloader()

if args.video_link:
    try:
        d.video_downloader(args.video_link)
    except:
        print('Enter a valid link!!')

elif args.playlist_link:
    try:
        d.playlist_downloader(args.playlist_link)
    except:
        print('Enter a valid link!!')

elif args.multiple_link:
    for item in args.multiple_link:
        try:
            d.video_downloader(item)
        except:
            print('Enter a valid link!!')

else:
    print('Required argument [-v] or [-p], -h for help.')
