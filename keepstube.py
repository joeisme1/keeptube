import pytube
link = input("enter video URL: ")
yt = pytube.YouTube (link)
videos = yt.streams.all()
s = 1
for v in videos:
	print(str(s)+", "+str(v))
	s += 1
	
n = int(1)
vid = videos[n-1]
print("enter destination: ")
destination = input()
vid.download(destination)
print("success!")