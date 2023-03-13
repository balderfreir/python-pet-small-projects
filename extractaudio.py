from pytube import YouTube
import pytube
import os

def main():
    video_url = input('Enter YouTube video URL: ')

    path = os.getcwd() + '/'

    name = pytube.extract.video_id(video_url)
    YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
    location = path + name
    renametomp3 = path + name + '.mp3'

    os.system('mv {0} {1}'.format(location, renametomp3))

if __name__ == '__main__':
    main()