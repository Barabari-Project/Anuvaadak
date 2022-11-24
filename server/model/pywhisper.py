from ydown import YoutubeDL
import pywhisper
import os


def download_video(url):
    URLS = [url]
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': 'output.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)

    return "output.mp3"


def AudiotoText(filename):
    model = pywhisper.load_model("base")
    result = model.transcribe(filename)
    print(result["text"])
    sonuc = result["text"]
    return sonuc


def main(link, model):
    print("URL: " + link)
    print("MODEL: " + model)

    print("Downloading video... Please wait.")
    try:
        filename = download_video(link)
        print("Downloaded video as " + filename)
    except:
        print("Not a valid link..")
        return
    try:
        mymodel = pywhisper.load_model(model)
        result = mymodel.transcribe(filename)
        print(result["text"])
        result = result["text"]
        os.remove(filename)
        print("Removed video and audio files")
        print("Done!")
        return result
    except Exception as e:
        print("Error transcribing audio to text")
        print(e)
        return


if __name__ == "__main__":
    main()
