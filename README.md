# YouTube-Video-Downloader
A program that downloads YouTube videos or playlists.


## Installation

Clone the Repository;
```bash
$ git clone https://github.com/PrashantMhrzn/YouTube-Video-Downloader.git
```
Install the required modules;
```bash
$ pip/pip3 install -r requirements.txt
```
CD into the cloned directory;
```bash
$ cd  YouTube-Video-Downloader/
```
## Usage

```bash
$ python3 downloader.py -h                
usage: downloader.py [-h] [-v] [-p] [-m  [...]]

Downloads given video or a playtlist from youtube.

optional arguments:
  -h, --help            show this help message and exit
  -v , --video_link     Link of the video you want to download.
  -p , --playlist_link 
                        Link of the playlist you want to download.
  -m  [ ...], --multiple_link  [ ...]
                        Links of the videos you want to download.(Seperated with <space>)
```

## Example

Downloading a single video;
```bash
$ python3 downloader.py -v https://www.youtube.com/watch?v=qYnnCTfHsVM
Downloading Sam O Nella Uh Oh
100%|████████████████████████████████████████████████████| 1/1 [00:00<00:00,  5.77it/s]
Download Completed Sam O Nella Uh Oh
```
Downloading a playlist;
```bash
$ python3 downloader.py -p https://www.youtube.com/playlist?list=PLz5exA3L2fqiKT7jNn96Au5aoNRP11jli
Downloading samonella playlist
4it [00:13,  3.46s/it]███████████████████████████████████| 4/4 [00:13<00:00,  3.88s/it]
100%|████████████████████████████████████████████████████| 4/4 [00:13<00:00,  3.46s/it]
Download Completed samonella
```
Downloading multiple videos;
```bash
$ python3 downloader.py -m https://www.youtube.com/watch?v=qYnnCTfHsVM https://www.youtube.com/watch?v=_DFDTmcUXYs
Downloading Sam O Nella Uh Oh
100%|████████████████████████████████████████████████████| 1/1 [00:00<00:00,  5.95it/s]
Download Completed Sam O Nella Uh Oh
Downloading Sam O Nella- Once
100%|████████████████████████████████████████████████████| 1/1 [00:00<00:00,  8.01it/s]
Download Completed Sam O Nella- Once

```

## License
[MIT](https://github.com/PrashantMhrzn/YouTube-Video-Downloader/blob/main/LICENSE)
