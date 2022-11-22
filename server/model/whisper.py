# Set up whipser
import whisper
model = whisper.load_model('small.en')


def downloadFile(url):
    # somehowdownload


def getTranscript(url):
    downloadFile(url)  # & store & convert

    # Transcribe
    out = model.transcribe('clip.mp3')
    # Format Text
    text = out['text'].strip()
    splittext = text.split(".")
    for x in range(5, len(splittext), 5):
        splittext[x] = "\n\n"+splittext[x].lstrip()
    text = ".".join(splittext)

    # Write to file
    with open("subs.txt", "w") as text_file:
        print(text, file=text_file)

    # :)
    return {
        text: out['text'].strip(),
        size: len(splittext)
    }
