try:
    from pytube import YouTube
    from pytube import Playlist
    from tqdm import tqdm
except ModuleNotFoundError as err:
    print(err)

class Downloader:

    def video_downloader(self, link):
        yt = YouTube(link)
        self.stream = yt.streams.first()
        print(f'Downloading {self.stream.title}')
        for _ in tqdm(range(1)):
            self.stream.download()
        print(f'Download Completed {self.stream.title}')


    def playlist_downloader(self, link):
        self.p = Playlist(link)
        print(f'Downloading {self.p.title} playlist')
        bar = tqdm(total=len(self.p)) 
        for self.video in tqdm(self.p.videos):
            self.video.streams.first().download()
            bar.update(1)
        bar.close()
        print(f'Download Completed {self.p.title}')
