import pytube

url = input('url do video: ')
yt = pytube.Youtube(url)
audio = yt.streams.get_by_gtag(140)
audio.download()
print('Audio baixado com sucesso!')
