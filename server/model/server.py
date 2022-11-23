#!/usr/bin/env python
from pywhisper import main as whisper

model = "small"
isHTML = True

link = "https://www.youtube.com/watch?v=UF8uR6Z6KLc"
result = whisper(link, model)
print(result)
