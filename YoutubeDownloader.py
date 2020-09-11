import pytube

def menu():
    while True:
        try:
            x = int(input("Enter 1 to proceed with software || Enter 2 to exit software: "))
            if x == 1 or x == 2:
                break
        except ValueError:
            print("Enter 1 or 2 please")
    print("")
    return x

class Downloader:
    def __init__(self):
        self.audioOnly = 0
        self.path = ""
        self.itag = 0

    def inputLink(self):
        while True:
            self.link = input("Please copy and paste the link of the youtube video here : ")
            try:
                self.yt = pytube.YouTube(self.link)
            except KeyError:
                print("Sorry. The video chosen is protected from download")
                print("Try entering another link")
                print("")
                continue
            except pytube.exceptions.RegexMatchError:
                print("Please enter a valid youtube video link")
                print("")
                continue
            except Exception:
                print("Please enter a valid youtube video link")
                continue
            break

    def inputSpecsOfVideo(self):
        while True:
            try:
                self.audioOnly = int(input("Enter 1 to Download track with audio only || Enter 2 to Download Regular video with audio: "))
            except ValueError:
                pass
            if self.audioOnly == 1 or self.audioOnly == 2:
                break
            else:
                print("Enter 1 or 2 please")
        print("")
        self.path = input("Enter the path to where you want to store the download: ")
        print("")
    
    def evaluateInput(self):
        if self.audioOnly is 1:
            self.stream = self.yt.streams.filter(only_audio = True)
        else:
            self.stream = self.yt.streams.filter(progressive = True)

    def inputVersion(self):
        while True:
            try:
                print("")
                for i in self.stream:
                    print(i)
                print(" ")
                self.itag = int(input("Enter the itag of the version you want to download: "))
                print("")
                break
            except ValueError:
                print("Enter a valid itag please")

    def install(self):
        try:
            load = self.yt.streams.get_by_itag(self.itag)
            load.download(self.path)
            print("Download complete")
            print("")
        except AttributeError:
            print("No version with itag "+ str(self.itag))
            print(" ")
            return False
        return True

print("Welcome to the YouTube Video Downloader")
print("")
while True:
    if menu() is 1:   
        obj = Downloader()
        obj.inputLink()
        obj.inputSpecsOfVideo()
        obj.evaluateInput()
        while True:
            obj.inputVersion()
            if obj.install():
                break
    
    else:
        break


    


